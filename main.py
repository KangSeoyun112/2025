import streamlit as st

# 페이지 설정
st.set_page_config(page_title="학습 방법 추천 앱", page_icon="📚", layout="centered")

# 제목
st.title("📚 맞춤형 학습 방법 추천 앱")
st.write("당신의 학습 스타일과 목표에 따라 최적의 학습 방법을 추천해드립니다!")

# 사용자 입력
st.subheader("1️⃣ 기본 정보 입력")
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이를 입력하세요", min_value=10, max_value=80, step=1)
goal = st.selectbox("학습 목표를 선택하세요", ["시험 대비", "취업 준비", "자기계발", "기타"])

st.subheader("2️⃣ 학습 스타일 진단")
style = st.radio("당신은 어떤 방식으로 학습하는 걸 좋아하나요?", 
                 ["시각적 (이미지, 다이어그램)", "청각적 (강의, 오디오)", "실습 중심 (직접 해보기)", "읽기/쓰기"])

time = st.slider("하루에 학습 가능한 시간은 몇 시간인가요?", 0, 10, 2)

motivation = st.selectbox("현재 학습 동기 수준은 어떤가요?", ["매우 낮음", "보통", "높음", "매우 높음"])

# 추천 알고리즘 (간단한 예시)
def recommend_learning(style, goal, time, motivation):
    rec = []
    
    if style == "시각적 (이미지, 다이어그램)":
        rec.append("마인드맵, 인포그래픽, 유튜브 강의 활용")
    elif style == "청각적 (강의, 오디오)":
        rec.append("팟캐스트, 오디오북, 강의 녹음 반복 청취")
    elif style == "실습 중심 (직접 해보기)":
        rec.append("프로젝트 기반 학습, 문제 풀이 중심 학습")
    else:
        rec.append("노트 필기, 요약 정리, 블로그 글 작성")

    if goal == "시험 대비":
        rec.append("기출문제 풀이 + 시간 제한 모의고사 진행")
    elif goal == "취업 준비":
        rec.append("면접 스터디, 포트폴리오 제작")
    elif goal == "자기계발":
        rec.append("책 읽기, 온라인 강의 수강")
    else:
        rec.append("관심 분야의 자유 탐구")

    if time < 2:
        rec.append("짧고 집중적인 학습(예: Pomodoro 기법)")
    else:
        rec.append("체계적 커리큘럼 계획 세우기")

    if motivation in ["매우 낮음", "보통"]:
        rec.append("학습 파트너 구하기, 보상 시스템 활용")
    else:
        rec.append("스스로 목표 설정 및 성취감 활용")

    return rec

# 결과 출력
if st.button("✨ 학습 방법 추천받기"):
    recommendations = recommend_learning(style, goal, time, motivation)
    st.subheader(f"🎯 {name}님을 위한 추천 학습 방법")
    for r in recommendations:
        st.markdown(f"- {r}")

