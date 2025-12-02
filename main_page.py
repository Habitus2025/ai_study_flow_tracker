import streamlit as st

# ============================
# 🌟 기본 설정
# ============================
st.set_page_config(
    page_title="AI Study Flow Tracker",
    page_icon="📚",
    layout="wide"
)

# ============================
# 🌟 버튼을 카드처럼 보이게 하는 CSS
# ============================
st.markdown(
    """
    <style>
    /* st.button 을 카드처럼 보이게 공통 스타일 적용 */
    div.stButton > button {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 20px 10px;
        border: 1px solid #eeeeee;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        font-size: 15px;
        font-weight: 500;
        color: #333333;
        height: 190px;
        white-space: pre-line;  /* \\n 줄바꿈 허용 */
    }
    div.stButton > button:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        transform: translateY(-3px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================
# 🌟 상단 제목 영역
# ============================
st.markdown("## 📚 AI Study Flow Tracker")
st.write("공부 흐름을 기록하고 분석하는 스마트 학습 도우미")
st.write("---")

# ============================
# 🌟 카드 3개 컬럼 배치
# ============================
col1, col2, col3 = st.columns(3)

# 1) Start Study Session 카드
with col1:
    label1 = "🎥\nStart Study Session\n\nAI가 실시간으로 집중도를 분석합니다"
    if st.button(label1, key="start_session", use_container_width=True):
        # 👉 /Users/yoonjo/my_app/pages/1_Start_Study_Sesssion.py
        st.switch_page("pages/1_Start_Study_Session.py")

# 2) Study Report & Analysis 카드
with col2:
    label2 = "📊\nStudy Report & Analysis\n\n오늘의 집중 패턴과 통계를 한눈에 보기"
    if st.button(label2, key="stats_report", use_container_width=True):
        # 👉 /Users/yoonjo/my_app/pages/2_Study_Report_Analysis.py
        st.switch_page("pages/2_Study_Report_Analysis.py")

# 3) Community 카드
with col3:
    label3 = "👥\nCommunity\n\n공부 인증하고 다른 사용자들과 소통하기"
    if st.button(label3, key="community", use_container_width=True):
        # 👉 /Users/yoonjo/my_app/pages/3_Community.py
        st.switch_page("pages/3_Community.py")

