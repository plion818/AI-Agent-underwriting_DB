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
client = MongoClient("mongodb+srv://patrick89818pp:890818pp@cluster0.jliqnkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
col = client["store"]["customer_embeddings"]

# 讓使用者輸入要查詢的名字
query_name = input("請輸入要查詢的客戶名字：")

# 取得查詢 embedding（呼叫 Hugging Face API）
def get_embedding(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    response.raise_for_status()
    embedding = response.json()[0]
    return embedding

query_embedding = get_embedding(query_name)

print("查詢前送給資料庫的資料格式：")
print({
    "embedding": query_embedding,
    "維度": len(query_embedding)
})

# 向量查詢 pipeline，查詢 embedding 欄位
pipeline = [
    {
        "$vectorSearch": {
            "index": "vector_index",
            "path": "embedding",
            "queryVector": query_embedding,
            "numCandidates": 5,
            "limit": 1
        }
    }
]

results = list(col.aggregate(pipeline))
if results:
    print("查詢結果：")
    print(results[0]["info"])
else:
    print("查無相符客戶！")
