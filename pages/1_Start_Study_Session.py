import streamlit as st

st.set_page_config(page_title="Start Study Session")

st.title("🎥 Start Study Session")
st.write("학습 세션을 촬영하고, 실시간으로 시선·자세를 추적하여 집중효율을 분석합니다.")

st.markdown("""
### 📌 공부 세션 시작하기
아래에서 학습을 위한 세션을 시작할 수 있습니다.
- 웹캠 촬영
- 영상 파일 업로드
- 추출된 특징 요약 확인
""")

st.divider()

# -----------------------
# 세션 선택
# -----------------------
st.subheader("1) 세션 방식 선택")

option = st.radio(
    "촬영 방식 선택",
    ["📷 WebCam으로 촬영", "📁 영상 파일 업로드"],
    horizontal=True
)

if option == "📷 WebCam으로 촬영":
    st.info("웹캠 촬영 기능은 실제 앱에서는 WebRTC 기반으로 동작합니다.")
    st.button("▶ Start Camera Session")

else:
    uploaded = st.file_uploader("영상 파일을 업로드하세요 (.mp4, .mov 등)", type=["mp4", "mov"])
    if uploaded:
        st.video(uploaded)
        st.success("파일 업로드 완료!")

st.divider()

# -----------------------
# 세션 메타데이터 입력
# -----------------------
st.subheader("2) 학습 세션 정보 입력")

col1, col2 = st.columns(2)

with col1:
    subject = st.text_input("세션 이름 (예: Math Study #1)")
with col2:
    duration = st.number_input("예상 학습 시간 (분)", min_value=1, max_value=300)

st.divider()

# -----------------------
# 시작 버튼
# -----------------------
st.subheader("3) 세션 시작")

start = st.button("🚀 Start Study Session", use_container_width=True)
if start:
    st.success("학습 세션이 시작되었습니다! 분석 페이지에서 결과를 확인하세요.")

