import streamlit as st
from agent_api_client import call_agent_api, extract_final_results

# --- Page Configuration ---
st.set_page_config(
    page_title="智慧核保分析小幫手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<h2 style='color:#005A9C;'>🧠 智慧核保小幫手</h2>
<p style='color:#4B5563;'>請在下方輸入您的訊息，系統會將內容傳送給 AI Agent 並回覆結果。</p>
""", unsafe_allow_html=True)

if "helper_result" not in st.session_state:
    st.session_state.helper_result = None
if "helper_input" not in st.session_state:
    st.session_state.helper_input = ""

user_input = st.text_area("請輸入您的訊息", key="helper_input", placeholder="請輸入...", height=68)
if st.button("送出", key="helper_send_btn") and user_input.strip():
    payload = user_input.strip()  # 只傳字串
    api_response = call_agent_api(payload)
    result = extract_final_results(api_response)
    # 只取需要的欄位
    filtered = {}
    if isinstance(result, dict):
        filtered['total_score'] = result.get('total_score', 'N/A')
        filtered['grade'] = result.get('grade', 'N/A')
        filtered['專家綜合說明'] = result.get('專家綜合說明', '無說明')
    else:
        filtered = {'total_score': 'N/A', 'grade': 'N/A', '專家綜合說明': '無說明'}
    st.session_state.helper_result = filtered
    st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h4>回傳結果</h4>", unsafe_allow_html=True)
res = st.session_state.helper_result

# 風險評級顏色對應
risk_color_map = {
    'A+': '#28A745',  # 綠色
    'A': '#20B2AA',  # 青綠色
    'B': '#FFC107',  # 黃色
    'C': '#FF7043',  # 橘色
    'D': '#DC3545'   # 紅色
}
grade = res.get('grade', 'N/A') if res else 'N/A'
grade_color = risk_color_map.get(str(grade), '#6C757D')

if res:
    st.markdown(f"""
    <div style='background:#E9F5FF; border-radius:12px; padding:18px 24px; margin-bottom:16px;'>
      <div style='font-size:1.45em; color:#005A9C; font-weight:bold;'>綜合評估總分：<span style='font-size:1.5em;'>{res.get('total_score','N/A')}</span></div>
      <div style='font-size:1.45em; font-weight:bold; margin-top:8px; color:{grade_color};'>風險評級：<span style='font-size:1.3em;'>{grade}</span></div>
      <div style='margin-top:18px; color:#343a40; font-size:1.45em; font-weight:bold;'>🧐 希望專家綜合說明:</div>
      <div style='font-size:1.18em; margin-top:6px;'>{res.get('專家綜合說明','無說明')}</div>
    </div>
    """, unsafe_allow_html=True)
