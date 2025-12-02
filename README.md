# 📚 AI Study Flow Tracker

## 프로젝트 목적
  본 연구는 학습자의 자세, 시선, 행동 패턴을 기반으로 집중도를 정량적으로 평가하고, 세션 종료 후 LLM 기반 개인화 학습 코칭 리포트를 자동 생성하는 **AI Study Tracker 시스템**을 개발하였다. MediaPipe와 ViT-Gaze를 활용해 **포즈·시선·눈 깜빡임** 등 미세 행동 특징을 추출하고, segment-level rule 기반 분류기와 개인화 임계치 조정 알고리즘을 결합하여 사용자별 집중 상태를 효율적으로 분류하였다. 성능 검증을 위해 시스템의 추정 결과를 사람 라벨(Ground Truth) 과 비교한 결과, 폰 사용 100.00%, 졸음 91.67%, 자리 이탈 100.00%의 정확도를 보였으며, 전체 평균 정확도는 **97.22%**로 확인되었다. 본 시스템은 행동 기반 집중도 분석과 LLM 코칭을 통합함으로써, <em>학습자의 습관 개선과 학습 효율 향상에 기여할 수 있는 지능형 학습지원 도구</em>로서의 가능성을 제시한다.

## System Architecture
<div align="center">

<pre>
[Video Stream]
        ↓ (frame sampling)

[Pose/Gaze Extractor]
        ↓ (keypoint, EAR, gaze, phone-use signals)

[Feature Aggregator]
        ↓ (stability filtering + time-series features)

[Segment-level Concentration Model]
        ↓ (rule-based + personal threshold adaptation)

[LLaMA Coach]
        ↓ (session summary, improvement strategies)

[Dashboard Visualization]
</pre>

</div>


## Code Description

### data_preprocessing/data_labeling
- 자세/시선 키포인트 추출
- 추출된 키포인트 기반 피처 추출
- 개인화 적용
- 자동 라벨링과 groundtruth 비교

### LLaMA/model
- 사용자 집중 분석 리포트 생성
