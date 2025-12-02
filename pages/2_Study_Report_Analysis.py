import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ==============================
# 페이지 설정
# ==============================
st.set_page_config(page_title="Study Report & Analysis", page_icon="📊")

# ==============================
# 상단 타이틀 + 설명
# ==============================
st.title("📊 Study Report & Analysis")

st.markdown(
    """
    <div style='font-size:18px; color:#5f6f7a; margin-top:-8px; margin-bottom:18px;'>
        오늘 학습 세션에 대한 실제 분석 리포트입니다.<br>
        아래 데이터는 영상 기반 라벨링 결과를 활용하여 자동 생성되었습니다 😊
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# 실제 데이터 불러오기
# ==============================
DATA_PATH = "pages/labels_revised_video_30.csv"   # 파일은 같은 폴더에 두면 됨
df = pd.read_csv(DATA_PATH)

# 최종 집중도 점수 (0~1)
focus_scores = df["final"].values

# 시간 생성 (segment 하나 = 20초 가정 → 필요하면 조정 가능)
start_time = datetime.now().replace(minute=0, second=0, microsecond=0)
times = [start_time + timedelta(seconds=20 * i) for i in range(len(focus_scores))]

df_focus = pd.DataFrame({"time": times, "focus": focus_scores})

# ==============================
# 집중도 요약 통계
# ==============================
avg_focus = np.mean(focus_scores)
max_focus = np.max(focus_scores)
min_focus = np.min(focus_scores)

col1, col2, col3 = st.columns(3)

col1.metric("평균 집중도", f"{avg_focus:.2f}")
col2.metric("최고 집중도", f"{max_focus:.2f}")
col3.metric("최저 집중도", f"{min_focus:.2f}")

st.markdown("---")

# ==============================
# 집중도 변화 시각화
# ==============================
st.subheader("📈 시간대별 집중도 변화")
st.line_chart(df_focus.set_index("time"))

st.markdown(
    """
    <div style='margin-top:10px; font-size:14px; color:#4b5563;'>
        실시간 집중도 변화를 파악해보세요!<br>
        특정 구간에서 급격히 떨어지는 구간이 있다면, 휴식 혹은 자세 교정이 필요했을 수 있어요 😊
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==============================
# 라벨링 기반 자동 분석 (phone, seat, blink 등)
# ==============================

st.subheader("🧠 학습 행동 패턴 분석")

phone_issue_rate = (df["phone_face"] < 0.3).mean()
seat_depart_rate = df["seat_departed"].mean()
high_blink_rate = (df["blink_rate_proxy"] > 0.25).mean()
perclos_mean = df["perclos_raw"].mean()

# 휴대폰 문제
if phone_issue_rate > 0.25:
    st.write("📱 **휴대폰이 얼굴과 너무 가까운 시간이 많았어요.** 집중 흐름을 자주 끊었을 가능성이 있어요.")
else:
    st.write("📱 휴대폰 사용이 집중도에 크게 영향을 주지 않았어요!")

# 자리 이탈
if seat_depart_rate > 0.1:
    st.write("🚶 **자리 이탈이 자주 감지되었어요.** 일정 시간마다 자세를 점검해보면 좋아요.")
else:
    st.write("🚶 자리이탈 없이 안정적으로 학습했어요!")

# 깜빡임/피로도
if perclos_mean > 0.35:
    st.write("😴 **눈 깜빡임이 많고 졸음 지수가 높아요.** 조명이 어둡거나 피로 누적일 수 있어요.")
else:
    st.write("😴 눈 깜빡임, 졸음 지표 모두 정상 범위예요!")

st.markdown("---")

# ==============================
# LLM 스타일 자연어 리포트 (실제 데이터 기반)
# ==============================
st.subheader("📝 오늘의 학습 리포트")

focus_trend = "안정적" if avg_focus > 0.6 else "다소 변동적"
strength = "꾸준한 집중력 유지" if max_focus > 0.8 else "중간 이상의 집중도 유지"
weakness = "휴대폰 간섭" if phone_issue_rate > 0.25 else "피로 누적 가능성"

report_text = f"""
오늘 학습 세션의 전체적인 집중도는 **{avg_focus:.2f}** 점으로, 전반적으로 {focus_trend}인 흐름을 보였어요.

특히 **최고 집중도는 {max_focus:.2f}점**으로, {strength}가 돋보였습니다.  
다만 `{weakness}`로 인한 일시적인 집중 저하 구간이 존재했어요.

좌석 이탈 비율은 **{seat_depart_rate*100:.1f}%**, 휴대폰 문제 비율은 **{phone_issue_rate*100:.1f}%**,  
깜빡임 기반 피로 지표(PERCLOS)는 평균 **{perclos_mean:.2f}** 로 측정되었습니다.

종합적으로 오늘의 학습은  
✨ *“안정적으로 집중력을 유지한 세션이었으며, 자세·휴대폰 관련 습관만 조금 더 보완하면 더 높은 효율을 기대할 수 있어요!”*  
"""

st.markdown(
    f"""
    <div style='background-color:#f1f5f9; padding:18px; border-radius:12px; font-size:16px; line-height:1.6;'>
        {report_text}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==============================
# 월간/주간 트렌드 (실제 데이터 스케일에 맞춘 확장형)
# ==============================
st.subheader("📅 집중도 추세 (확장 분석 예시)")

# 주간 버전: 실제 데이터가 30분(30 segments) 정도라고 가정 → 7일 분포 생성
weekly_focus = pd.Series(focus_scores).rolling(3, min_periods=1).mean()
st.line_chart(weekly_focus)

st.markdown(
    """
    <div style='margin-top:10px; font-size:14px; color:#4b5563;'>
        이동 평균을 기반으로 주간 집중도 흐름을 표현한 그래프입니다.<br>
        특정 구간의 안정성 또는 급락 구간을 빠르게 파악할 수 있어요 😊
    </div>
    """,
    unsafe_allow_html=True
)
