# 🛡️ 智慧核保風險評估平台

本專案是一個基於 Python 和 Streamlit 构建的智慧核保風險評估平台原型。它旨在利用 AI 技術，整合客戶多維度數據，提供全面的客戶風險畫像與智能分析，從而輔助保險機構實現更精準、高效的核保決策。

## ✨ 核心功能

*   **客戶風險畫像**: 整合客戶基本資訊與歷史記錄，構建客戶的 360° 風險視圖。
*   **AI 智能分析**: 內建可配置的 AI 分析引擎（模擬），能根據預設規則評估客戶的風險等級。
*   **即時決策輔助**: 快速生成包含風險評分、評級、詳細規則合規情況、優缺點分析及專家建議的核保報告。
*   **友好的用戶介面**: 通過 Streamlit 實現了直觀易用的 Web 介面，方便用戶操作和查看分析結果。
*   **歷史紀錄查詢**: 提供歷史分析結果查詢頁面，方便追溯。
*   **MongoDB 整合**: 包含將客戶資料與規則庫整合進 MongoDB 的腳本，並提供簡易的查詢 API。
*   **向量搜尋**: 包含使用 Hugging Face 模型將客戶姓名轉換為向量並存入 MongoDB，以進行向量搜尋的腳本。

## 🛠️ 技術棧

*   **Python**: 主要編程語言。
*   **Streamlit**: 用於快速搭建數據應用的 Web 框架。
*   **Pandas**: 用於數據處理（主要在數據展示部分）。
*   **JSON**: 用於存儲客戶數據、分析結果和配置。
*   **MongoDB**: 用於儲存客戶資料與規則庫。
*   **FastAPI**: 用於建立簡易的查詢 API。
*   **Hugging Face Transformers**: 用於生成文字向量。

## 📂 專案結構

```
.
├── home.py                     # Streamlit 應用程式主入口，平台首頁
├── pages/
│   ├── analysis_page.py        # 核心分析頁面，用於客戶選擇、資料展示及 AI 分析
│   ├── history.py              # 歷史分析結果查詢頁面
│   └── smart_agent_helper.py   # 智慧核保分析小幫手頁面
├── MongoDB/
│   ├── client_info_integrate.py # 將客戶基本資訊與過往紀錄整合並存入 MongoDB
│   ├── config_rules_to_mongo.py # 將規則庫存入 MongoDB
│   ├── mongo_query_search.py   # 簡易的 MongoDB 查詢腳本
│   ├── vector_db.py            # 將客戶姓名轉換為向量並存入 MongoDB
│   └── vector_search.py        # 向量搜尋腳本
├── utils.py                    # 存放共享的輔助工具函數
├── assets/
│   └── styles.css              # 存放全局自定義 CSS 樣式
├── agent_api_client.py         # 模擬 AI Agent API 的客戶端交互邏輯
├── config_rules.py             # AI 分析引擎的規則配置（模擬）
├── search_api.py               # 提供客戶資料與規則庫的查詢 API
├── 中文規則對應.py             # 中英文欄位名稱及規則名稱的對照表
├── 客戶基本資訊/
│   ├── 基本資訊.json           # 模擬的客戶基本資料存儲
│   └── Example.py              # 範例資料格式
├── 客戶過往紀錄/
│   └── 過往紀錄.json           # 模擬的客戶歷史記錄存儲
├── Results/                      # 存放 AI 分析完成後生成的 JSON 結果檔案
│   └── history/                  # 存放智慧核保分析小幫手的歷史分析結果
├── requirements.txt            # 專案所需的 Python 依賴包
├── README.md                   # 專案說明文件 (本文件)
└── .env                        # (可選) 環境變數設定檔 (例如 API 金鑰)
```

**主要組件說明:**

*   **`home.py`**: 應用程式的著陸頁，提供平台介紹和進入分析功能的入口。
*   **`pages/analysis_page.py`**:
    *   允許用戶通過下拉選單選擇客戶。
    *   展示選定客戶的基本資料和歷史記錄。
    *   提供觸發 AI 風險分析的按鈕。
    *   詳細展示 AI 分析結果，包括總分、評級、規則合規表、優缺點和建議等。
*   **`pages/history.py`**: 展示 `Results/history` 資料夾中的歷史分析結果。
*   **`pages/smart_agent_helper.py`**: 提供一個簡易的介面，讓使用者輸入文字，呼叫 AI Agent 並顯示結果。
*   **`MongoDB/`**:
    *   `client_info_integrate.py`: 將 `客戶基本資訊` 和 `客戶過往紀錄` 的 JSON 檔案整合成單一的客戶資料，並存入 MongoDB。
    *   `config_rules_to_mongo.py`: 將 `config_rules.py` 中的規則庫存入 MongoDB。
    *   `mongo_query_search.py`: 一個簡單的命令列工具，用於查詢 MongoDB 中的客戶資料和規則。
    *   `vector_db.py` and `vector_search.py`: 使用 Hugging Face 模型進行向量搜尋的範例。
*   **`utils.py`**: 包含如安全獲取巢狀字典值 (`get_nested_value`)、從 `config_rules.py` 提取規則描述、類別和必要性信息的函數。
*   **`assets/styles.css`**: 集中管理應用的自定義 CSS，以確保視覺風格的統一性和易維護性。
*   **`agent_api_client.py`**: 模擬了與後端 AI 分析服務的 API 通信。`call_agent_api` 函數接收客戶數據和規則配置，並返回模擬的分析結果。
*   **`config_rules.py`**: 定義了 AI 分析引擎所依據的規則庫，包括不同險種類別的規則、關鍵字、描述、分數和必要性等。
*   **`search_api.py`**: 使用 FastAPI 建立的一個簡單 API，用於查詢 MongoDB 中的客戶資料和規則庫。
*   **`中文規則對應.py`**: 提供了 `all_field_zh` 字典，用於將程式碼中使用的英文欄位名和規則關鍵字對應到前端顯示的中文名稱。
*   **數據文件 (`.json`)**:
    *   `客戶基本資訊/基本資訊.json`: 存儲一個客戶列表，每個客戶包含姓名、年齡、職業等基本屬性。
    *   `客戶過往紀錄/過往紀錄.json`: 存儲客戶的歷史行為數據，如信用評等、保單歷史、理賠記錄等。
    *   `Results/result_*.json`: 每次 AI 分析完成後，結果會保存為一個 JSON 文件，以客戶 ID 命名。

## 🚀 安裝與運行

1.  **環境準備**:
    *   確保已安裝 Python (建議版本 3.9 或更高)。
    *   (可選) 建議創建並激活一個虛擬環境:
        ```bash
        python -m venv venv
        source venv/bin/activate  # Linux/macOS
        # venv\Scripts\activate   # Windows
        ```

2.  **安裝依賴**:
    在專案根目錄下，運行以下命令安裝 `requirements.txt` 中列出的所有依賴包：
    ```bash
    pip install -r requirements.txt
    ```
    主要依賴包括 `streamlit`, `pandas`, `pymongo`, `fastapi`, `uvicorn`, `python-dotenv`, `requests`。

3.  **設定環境變數**:
    將 `.env.example` 檔案（如果有的話，如果沒有請手動建立）複製為 `.env`，並填寫以下內容：
    ```
    API_URL=your_agent_api_url
    API_TOKEN=your_api_token
    HF_API_KEY=your_huggingface_api_key
    MONGODB_URI=your_mongodb_uri
    ```

4.  **運行應用**:
    在專案根目錄下，執行以下命令啟動 Streamlit 應用：
    ```bash
    streamlit run home.py
    ```
    應用程式通常會在瀏覽器的 `http://localhost:8501` 地址打開。

5.  **運行 API (可選)**:
    如果你想使用 `search_api.py` 提供的 API，請在另一個終端機視窗中執行：
    ```bash
    uvicorn search_api:app --reload
    ```

## ⚙️ 程式碼運作流程簡介

1.  **啟動與首頁 (`home.py`)**:
    *   用戶首先訪問 `home.py`，這裡展示了平台的介紹和一個 "開始分析之旅" 的按鈕。
    *   頁面加載 `assets/styles.css` 中的樣式。

2.  **進入分析頁面 (`pages/analysis_page.py`)**:
    *   點擊首頁按鈕後，用戶被導航到 `analysis_page.py`。
    *   此頁面同樣會加載 `assets/styles.css`。
    *   **客戶數據加載**:
        *   `load_data()` 函數 (使用 `@st.cache_data` 緩存) 從 `客戶基本資訊/基本資訊.json` 和 `客戶過往紀錄/過往紀錄.json` 讀取所有客戶的資料。
        *   用戶可以從下拉選單中選擇一個客戶。
    *   **客戶資料展示**:
        *   選中客戶後，其基本資訊和過往記錄會通過 `display_basic_info()` 和 `display_records()` 函數進行格式化（使用 `utils.py` 中的 `get_nested_value` 和 `中文規則對應.py` 中的 `all_field_zh`）並展示在可折疊的區域中。

3.  **AI 智能分析**:
    *   用戶點擊 "執行 AI 分析" 按鈕。
    *   **數據準備**: 將選中客戶的基本資訊和過往記錄合併。
    *   **API 調用 (模擬)**: 調用 `agent_api_client.py` 中的 `call_agent_api` 函數，傳入客戶數據和從 `config_rules.py` 中讀取的規則配置。此函數模擬 AI 引擎的處理過程，根據規則對客戶數據進行評分。
    *   **結果處理與儲存**: `call_agent_api` 返回的原始結果通過 `extract_final_results` 提取核心內容，然後通過 `save_results` 將格式化後的分析報告（包含總分、評級、各項規則得分、優缺點、建議等）保存到 `Results/result_{客戶ID}.json` 文件中。

4.  **AI 分析結果展示**:
    *   分析完成或用戶選擇查看歷史報告後，系統會從對應的 `Results/result_{客戶ID}.json` 文件讀取數據。
    *   結果會結構化地展示出來：
        *   **總覽**: 總分和風險評級。
        *   **分數評級區間**: 一個參考表格。
        *   **規則合規詳細情況**: 一個詳細的表格（HTML 通過 `st.components.v1.html` 渲染），展示每條規則的評分情況、規則描述（來自 `config_rules.py`，通過 `utils.py` 中的輔助函數獲取，並使用 `中文規則對應.py` 進行中文化）、必要性等。此表格的樣式（在用戶要求下）是內嵌在其 HTML 生成邏輯中的。
        *   **專家洞察**: 優點、風險、建議和專家綜合說明，以卡片形式展示。

5.  **樣式與工具函數**:
    *   整個應用的基礎樣式由 `assets/styles.css` 提供。
    *   通用的 Python 邏輯由 `utils.py` 提供，增加了程式碼的模組性和可維護性。

## 💡 (可選) 未來展望

*   對接真實的後端 AI 分析服務。
*   實現用戶身份驗證和權限管理。
*   增加更複雜的數據可視化圖表。
*   完善錯誤處理和日誌記錄。
*   提供更詳細的規則配置界面。

---

希望這份 README 對您有所幫助！
