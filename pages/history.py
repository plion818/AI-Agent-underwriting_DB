import streamlit as st
import os
import json

# --- 載入 CSS ---
def load_css(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass
load_css("assets/styles.css")

st.markdown("""
    <div style="position: relative;">
        <a href="/" target="_self">
            <button class="page-header-action-button">🏠</button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#005A9C;'>🧠 歷史分析結果</h2>", unsafe_allow_html=True)

history_dir = os.path.join('Results', 'history')
files = sorted([f for f in os.listdir(history_dir) if f.endswith('.json')], reverse=True)

if not files:
    st.info("目前沒有歷史分析結果。")
else:
    risk_color_map = {
        'A+': '#28A745',
        'A': '#20B2AA',
        'B': '#FFC107',
        'C': '#FF7043',
        'D': '#DC3545'
    }
    bg_colors = ['#E9F5FF', '#E6FFEA', '#FFF9E6', '#FFE6E6']
    for idx, file in enumerate(files):
        filepath = os.path.join(history_dir, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            res = json.load(f)
        grade = res.get('grade', 'N/A')
        grade_color = risk_color_map.get(str(grade), '#6C757D')
        bg_color = bg_colors[idx % 4]
        st.markdown(f"""
        <div style='background:{bg_color}; border-radius:12px; padding:18px 24px; margin-bottom:16px;'>
          <div style='font-size:1.1em; color:#005A9C; font-weight:bold;'>檔案：{file}</div>
          <div style='font-size:1.45em; color:#005A9C; font-weight:bold;'>綜合評估總分：<span style='font-size:1.5em;'>{res.get('total_score','N/A')}</span></div>
          <div style='font-size:1.45em; font-weight:bold; margin-top:8px; color:{grade_color};'>風險評級：<span style='font-size:1.3em;'>{grade}</span></div>
          <div style='margin-top:18px; color:#343a40; font-size:1.45em; font-weight:bold;'>🧐 希望專家綜合說明:</div>
          <div style='font-size:1.18em; margin-top:6px;'>{res.get('專家綜合說明','無說明')}</div>
        </div>
        """, unsafe_allow_html=True)
