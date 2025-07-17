import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from pymongo import MongoClient
from config_rules import config_rules

# 將 config_rules 轉為 json 格式
rules_json = json.dumps(config_rules, ensure_ascii=False)
rules_dict = json.loads(rules_json)

# MongoDB Atlas 連線
MONGODB_URI = "mongodb+srv://patrick89818pp:890818pp@cluster0.jliqnkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)
db = client["store"]
col = db["config_rules"]

# 寫入 MongoDB（以 rule 類型為唯一鍵）
for rule_type, rules in rules_dict.items():
    col.update_one({"rule_type": rule_type}, {"$set": {"rule_type": rule_type, "rules": rules}}, upsert=True)

print("所有規則已轉為 JSON 並存入 MongoDB store.config_rules！")
