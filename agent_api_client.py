import os
import json
import logging
import requests
import re
from dotenv import load_dotenv

# 設定 logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 讀取 .env 檔案
load_dotenv()

def call_agent_api(customer_data: dict, rules: dict, timeout: int = 60):
    """
    自動化呼叫 AGENT API，傳送客戶資訊與規則，回傳 API 結果或 None。
    timeout: 逾時秒數，預設 60 秒
    """
    api_url = os.getenv("API_URL")
    api_token = os.getenv("API_TOKEN")
    if not api_url:
        logger.error("缺少 API_URL，請確認 .env 檔案設定。")
        return None

    # 只傳送客戶名字，並包裝成 input_value JSON 字串
    input_content = {"customer_name": customer_data.get("customer_name") if isinstance(customer_data, dict) else str(customer_data)}
    payload = {
        "input_value": json.dumps(input_content, ensure_ascii=False),
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {}
    }
    headers = {'Content-Type': 'application/json'}
    if api_token:
        headers['Authorization'] = f'Bearer {api_token}'

    try:
        response = requests.post(api_url, json=payload, headers=headers, timeout=timeout)
        logger.info(f"API 回應狀態碼: {response.status_code}")
        logger.debug(f"API 回應內容: {response.text}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"API 呼叫失敗：{e}")
        return None

# 自動解析最終回傳小工具

def extract_final_results(api_response):
    """
    從Langflow智慧核保API回傳物件中自動萃取'擷取結果'與'分析'內容
    Args:
        api_response (dict): API呼叫回傳的原始JSON物件
    Returns:
        dict: {"extracted": {...}, "analysis": {...}} 或 None
    """
    text = ""
    try:
        # 多層message
        text = (
            api_response["outputs"][0]
            ["outputs"][0]
            ["results"]["message"]["text"]
        )
        # 去掉 markdown 或 codeblock
        # 改用非貪婪模式，支援多層巢狀或多個 code block
        match = re.search(r"```json\s*([\s\S]*?)\s*```", text)
        json_text = match.group(1) if match else text
        result = json.loads(json_text)
        result = json.loads(json_text)
        return result
    except Exception as e:
        logger.error(f"解析API回應內容失敗：{e}")
        logger.error(f"解析失敗內容原文: {text}")
        return None


def save_results(data, customer_id, filename_prefix="result"):
    """
    將資料以 .json 格式儲存於 Results 資料夾，檔名格式: {prefix}_{customer_id}.json，若已存在則覆蓋
    """
    results_dir = os.path.join(os.path.dirname(__file__), "Results")
    os.makedirs(results_dir, exist_ok=True)
    filename = f"{filename_prefix}_{customer_id}.json"
    filepath = os.path.join(results_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"結果已儲存於 {filepath}")
    except Exception as e:
        logger.error(f"儲存結果失敗: {e}")

if __name__ == "__main__":

    # 讀入規則
    import sys
    import config_rules
    rules = None
    for var in dir(config_rules):
        if not var.startswith("__"):
            value = getattr(config_rules, var)
            if isinstance(value, dict):
                rules = value
                break
    if rules is None:
        raise ValueError('config_rules.py 未找到任何 dict 規則變數')

    # 取得客戶名字（命令列參數優先，否則互動輸入）
    if len(sys.argv) > 1:
        customer_name = sys.argv[1]
    else:
        customer_name = input("請輸入要查詢的客戶名字：").strip()

    # 取得 timeout（可選，命令列第2參數，否則預設60秒）
    if len(sys.argv) > 2:
        try:
            timeout = int(sys.argv[2])
        except ValueError:
            print("timeout 參數需為整數，將使用預設60秒")
            timeout = 60
    else:
        timeout = 60

    # 呼叫 API 並顯示
    input_content = {"customer_name": customer_name}
    result = call_agent_api(input_content, None, timeout=timeout)
    print("="*30)
    print("本次傳送 payload：")
    payload = {
        "input_value": json.dumps(input_content, ensure_ascii=False),
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {}
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    print("="*30)
    if result:
        # Canvas小工具自動解析
        final_result = extract_final_results(result)
        print("="*30)
        if final_result:
            print("【自動解析最終擷取結果與分析】")
            print(json.dumps(final_result, ensure_ascii=False, indent=2))
            # 儲存結果
            save_results(final_result, customer_name)
        else:
            print("❌ 解析 API 回傳內容失敗，請檢查結構或日誌")
    else:
        logger.warning("API 未取得回應或發生錯誤。")
