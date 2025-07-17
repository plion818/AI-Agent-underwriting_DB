@echo off
call conda activate torchenv
echo 等待 15 秒啟動服務...
timeout /t 15
start cmd /k "uv run langflow run > log\langflow.log 2>&1"
echo 啟動 langflow...
timeout /t 5
start cmd /k "uvicorn search_api:app --reload > log\api.log 2>&1"
start cmd /k "streamlit run home.py > log\streamlit.log 2>&1"
