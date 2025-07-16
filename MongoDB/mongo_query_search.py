from pymongo import MongoClient

# MongoDB Atlas 連線
MONGODB_URI = "mongodb+srv://patrick89818pp:890818pp@cluster0.jliqnkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)
col = client["store"]["client_info"]

print("請輸入 MongoDB 查詢指令（如 {'name': '王小萍'}）：")
query_str = input()

try:
    query = eval(query_str)
    results = list(col.find(query))
    print(f"查詢結果共 {len(results)} 筆：")
    for doc in results:
        print(doc)
except Exception as e:
    print(f"查詢失敗：{e}")

col = client["store"]["config_rules"]

print("請輸入要查詢的規則類型（如 財產保險規則）：")
query_type = input()

result = col.find_one({"rule_type": query_type})
if result:
    result.pop('_id', None)
    print("查詢結果：")
    print(result)
else:
    print("查無此規則類型！")
