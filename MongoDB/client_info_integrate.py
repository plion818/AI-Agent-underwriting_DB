import json
from pymongo import MongoClient

# MongoDB Atlas 連線
MONGODB_URI = "mongodb+srv://patrick89818pp:890818pp@cluster0.jliqnkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)
db = client["store"]
col = db["client_info"]

# 讀取客戶基本資訊
with open("客戶基本資訊/基本資訊.json", "r", encoding="utf-8") as f:
    basic_info = json.load(f)

# 讀取客戶過往紀錄
with open("客戶過往紀錄/過往紀錄.json", "r", encoding="utf-8") as f:
    history_info = json.load(f)

# 建立 id 到過往紀錄的對照表
history_map = {h["customer_id"]: h for h in history_info}

for customer in basic_info:
    cid = customer["customer_id"]
    # 先用基本資訊，再合併過往紀錄（重複欄位以基本資訊為主）
    merged = customer.copy()
    if cid in history_map:
        for k, v in history_map[cid].items():
            if k not in merged:
                merged[k] = v
    # 寫入 MongoDB（以 customer_id 為唯一鍵）
    col.update_one({"customer_id": cid}, {"$set": merged}, upsert=True)

print("所有客戶資訊已依順序整合並存入 MongoDB store.client_info！")
