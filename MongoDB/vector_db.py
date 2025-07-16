import json
import requests
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Hugging Face API 設定
API_URL = "https://api-inference.huggingface.co/models/BAAI/bge-base-zh"
load_dotenv()
API_KEY = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}

# MongoDB Atlas 連線
MONGODB_URI = "mongodb+srv://patrick89818pp:890818pp@cluster0.jliqnkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "store"
COLLECTION_NAME = "customer_embeddings"

# 讀取客戶資訊
with open("客戶基本資訊/基本資訊.json", "r", encoding="utf-8") as f:
    customers = json.load(f)

# 取得名字 embedding（呼叫 Hugging Face API）
def get_embedding(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    response.raise_for_status()
    embedding = response.json()[0]  # API 回傳為 list
    return embedding

# 連線 MongoDB
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

for customer in customers:
    name_text = customer["name"]
    embedding = get_embedding(name_text)
    doc = {
        "customer_id": customer["customer_id"],
        "info": customer,
        "embedding": embedding
    }
    collection.update_one({"customer_id": customer["customer_id"]}, {"$set": doc}, upsert=True)
print("所有客戶名字的 Embedding 及完整資訊已成功存入 MongoDB！")
