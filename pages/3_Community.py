

import streamlit as st
from datetime import datetime

# ==============================
# 페이지 설정
# ==============================
st.set_page_config(page_title="Community", page_icon="👥")

# ==============================
# 상단 제목 + 파스텔 분위기
# ==============================
st.title("👥 Community Space")

st.markdown(
    """
    <div style='font-size:20px; color:#5f6f7a; margin-top:-8px; margin-bottom:14px; padding:8px 0;'>
        공부 메이트들과 함께 소통하며 성장하세요 🤍
    </div>
    """,
    unsafe_allow_html=True
)

# 파스텔톤 접속자 박스
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #D8EEFF 0%, #C9F6E8 40%, #E8FCD9 100%);
        padding: 16px 22px;
        border-radius: 16px;
        display: inline-block;
        font-size:18px;
        font-weight:600;
        color:#3a4a55;
        box-shadow: 0px 6px 12px rgba(0,0,0,0.05);
        margin-bottom: 28px;
        border: 1px solid rgba(255,255,255,0.7);
    ">
        👥 현재 접속자: <span style="color:#2f7a52;">7,042명</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# 세션 상태 초기화
# ==============================
if "posts" not in st.session_state:
    st.session_state.posts = [
        {"user": "익명1", "text": "오늘 3시간 공부했어요!🔥", "time": "10:21"},
        {"user": "익명2", "text": "LLM 파인튜닝 진짜 어렵네요ㅠㅠ", "time": "11:03"},
    ]

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"user": "익명A", "text": "다들 오늘 공부 얼마나 했나요? 👀", "time": "14:01"},
        {"user": "익명B", "text": "저는 2시간 했어요! 집중 잘됨!", "time": "14:05"},
        {"user": "익명C", "text": "저 집중이 너무 안돼요 ㅠㅠ", "time": "14:10"},
    ]

# ==============================
# 페이지 레이아웃
# ==============================
left, right = st.columns([2, 1])

# ==========================================================
# 📌 LEFT — 커뮤니티 익명 게시판
# ==========================================================
with left:
    st.header("📚 커뮤니티 익명 게시판")

    new_post = st.text_area("✏️ 새 글 작성하기", height=100)

    if st.button("업로드"):
        if new_post.strip():
            st.session_state.posts.insert(0, {
                "user": "익명 사용자",
                "text": new_post,
                "time": datetime.now().strftime("%H:%M")
            })
            st.rerun()

    st.write("---")
    st.subheader("📌 최신 글")

    for post in st.session_state.posts:
        st.markdown(
            f"<div style='padding:12px; margin-bottom:10px; background:#F0FAFF; border-radius:10px;'>"
            f"<b>{post['user']}</b> ({post['time']})<br>{post['text']}</div>",
            unsafe_allow_html=True
        )


# ==========================================================
# 📌 RIGHT — 실시간 오픈채팅방 (카톡형 말풍선)
# ==========================================================
with right:
    st.header("💬 실시간 오픈채팅방")

    # 채팅 CSS
    st.markdown(
        """
        <style>
        .chat-container {
            background: #ffffff;
            padding: 10px;
            border-radius: 12px;
            height: 450px;
            overflow-y: auto;
            border: 1px solid #d9d9d9;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.03);
        }
        .message {
            margin-bottom: 12px;
            padding: 8px 12px;
            border-radius: 14px;
            max-width: 80%;
            line-height: 1.4;
            word-wrap: break-word;
        }
        .my-message {
            background: #C9F6E8;
            float: right;
            clear: both;
        }
        .other-message {
            background: #D8EEFF;
            float: left;
            clear: both;
        }
        .username {
            font-size: 12px;
            color: #5f6f7a;
            margin-bottom: 4px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 채팅 메시지 렌더링
    html = "<div class='chat-container'>"
    for msg in st.session_state.chat_messages:
        cls = "my-message" if msg["user"] == "익명 사용자" else "other-message"
        html += (
            f"<div class='message {cls}'>"
            f"<div class='username'>{msg['user']} ({msg['time']})</div>"
            f"{msg['text']}</div>"
        )
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    st.write("---")

    # 메시지 입력 + 전송
    chat_text = st.text_input("메시지를 입력하세요", key="chat_input", placeholder="메시지를 입력하세요…")

    if st.button("전송"):
        if chat_text.strip():
            st.session_state.chat_messages.append({
                "user": "익명 사용자",
                "text": chat_text,
                "time": datetime.now().strftime("%H:%M")
            })
            st.rerun()
