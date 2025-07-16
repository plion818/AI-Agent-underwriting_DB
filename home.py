import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="智慧核保風險評估平台",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed" # 首頁通常不需要一直顯示側邊欄
)

def load_css(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_name}")
        return ""

css_styles = load_css("assets/styles.css")
if css_styles:
    st.markdown(f"<style>{css_styles}</style>", unsafe_allow_html=True)

# --- Header Section ---
# Apply the .title class for the main title
st.markdown("<div class='title'>智慧核保風險評估平台</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='description'>"
    "運用先進 AI 技術，提供全面、即時的客戶風險畫像與智能分析，"
    "助力保險機構實現更精準、高效的核保決策。"
    "</div>",
    unsafe_allow_html=True
)

# --- Features Section ---
st.markdown("<h2 style='text-align: center; color: #003366; margin-bottom: 2rem;'>核心功能特色</h2>", unsafe_allow_html=True)

cols = st.columns(3, gap="large")

with cols[0]:
    st.markdown(
        """
        <div class="feature-card">
            <div>
                <h3><span class="icon">👤</span>客戶風險畫像</h3>
                <p>整合多維度數據，構建客戶360°風險視圖，深入洞察潛在風險，為每一位客戶提供精準的風險評級。</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with cols[1]:
    st.markdown(
        """
        <div class="feature-card">
            <div>
                <h3><span class="icon">💡</span>AI 智能分析</h3>
                <p>強大的 AI 引擎，自動化評估數個風險因子，提供客觀、科學的分析結果，有效識別高風險案件。</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with cols[2]:
    st.markdown(
        """
        <div class="feature-card">
            <div>
                <h3><span class="icon">📊</span>即時決策輔助</h3>
                <p>快速生成清晰易懂的核保建議與風險報告，顯著提升人工審核效率，優化整體業務處理流程。</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Call to Action Button ---
if st.button("🚀 開始分析之旅"):
    st.switch_page("pages/analysis_page.py")

# --- Floating Action Button ---
st.markdown(
    """
    <a href="/smart_agent_helper" target="_self" class="floating-action-button" title="使用智慧核保分析小幫手">
        <span class="fab-icon">🤖</span>
        <span class="fab-text">分析小幫手</span>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='text-align:center; color: #888;'>© 2024 智慧核保解決方案</p>", unsafe_allow_html=True)
