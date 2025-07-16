from fastapi import FastAPI, Query
from pymongo import MongoClient
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# MongoDB Atlas 連線
MONGODB_URI = "mongodb+srv://patrick89818pp:890818pp@cluster0.jliqnkt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URI)
client_info_col = client["store"]["client_info"]
config_rules_col = client["store"]["config_rules"]

@app.get("/search")
def search(q: str = Query(..., description="客戶名字查詢")):
    results = list(client_info_col.find({"name": q}))
    for doc in results:
        doc.pop('_id', None)
    return JSONResponse(content={"results": results})

@app.get("/config_rule_search")
def config_rule_search(q: str = Query(..., description="規則類型查詢（如 財產保險規則）")):
    result = config_rules_col.find_one({"rule_type": q})
    if result:
        result.pop('_id', None)
        return JSONResponse(content=result)
    else:
        return JSONResponse(content={"error": "查無此規則類型"}, status_code=404)

# FastAPI 啟動方式：
# uvicorn search_api:app --reload
