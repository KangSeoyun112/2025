import streamlit as st
from PIL import Image
import random

# -------------------------------
# 페이지 설정
# -------------------------------
st.set_page_config(page_title="학습 방법 추천 앱", page_icon="📚", layout="wide")

st.title("📚 나에게 맞는 학습 방법 찾기")
st.write("""
이 앱은 학습자의 **스타일**과 **목표**를 입력받아, 가장 적합한 학습 방법을 추천해줍니다.
""")

# -------------------------------
# 사이드바 입력
# -------------------------------
st.sidebar.header("📌 나의 학습 정보 입력")
name = st.sidebar.text_input("이름을 입력하세요:")
subject = st.sidebar.selectbox("공부할 과목을 선택하세요", ["수학", "영어", "과학", "역사", "프로그래밍"])
style = st.sidebar.radio("학습 스타일", ["시각형 (Visual)", "청각형 (Auditory)", "운동감각형 (Kinesthetic)", "읽기/쓰기형 (Reading/Writing)"])
goal = st.sidebar.selectbox("목표", ["시험 대비", "장기적 이해", "프로젝트 수행", "기초 개념 익히기", "창의적 문제 해결"])

# -------------------------------
# 추천 알고리즘 (다양화)
# -------------------------------
def recommend_method(subject, style, goal):
    if style == "시각형 (Visual)":
        if goal == "시험 대비":
            return [
                "마인드맵과 요약 노트를 활용해 시각적으로 정리하세요.",
                "색깔 펜과 하이라이트로 중요한 부분을 강조하세요.",
                "과목별 개념도를 만들어 전체 구조를 파악하세요."
            ], "visual_map.jpg"
        elif goal == "창의적 문제 해결":
            return [
                "디자인 씽킹 보드나 아이디어 스케치를 활용하세요.",
                "비주얼 브레인스토밍을 통해 다양한 아이디어를 연결해보세요."
            ], "visual_creative.jpg"
        else:
            return [
                "인포그래픽, 도표, 색상 강조 자료를 활용하세요.",
                "영상 강의와 그림 자료를 반복 시청하세요."
            ], "visual_study.jpg"

    elif style == "청각형 (Auditory)":
        if goal == "장기적 이해":
            return [
                "스터디 그룹 토론이나 강의 녹음을 통해 반복 학습하세요.",
                "자신의 목소리로 개념을 설명하고 녹음해 들어보세요."
            ], "auditory_group.jpg"
        elif goal == "시험 대비":
            return [
                "암기할 내용을 노래 가사처럼 만들어 외워보세요.",
                "강의나 설명을 여러 번 들어보세요."
            ], "auditory_exam.jpg"
        else:
            return [
                "팟캐스트, 오디오 강의로 학습하세요.",
                "학습 내용을 친구에게 설명하며 대화형으로 복습하세요."
            ], "auditory_learning.jpg"

    elif style == "운동감각형 (Kinesthetic)":
        if goal == "프로젝트 수행":
            return [
                "실습 중심 프로젝트나 실험을 통해 배우세요.",
                "직접 손으로 코드를 작성하거나 실험을 진행하세요."
            ], "kinesthetic_project.jpg"
        else:
            return [
                "카드 정리, 퀴즈, 모형 만들기 등 활동 기반 학습을 해보세요.",
                "실제 사례를 적용하며 배우세요."
            ], "kinesthetic_learning.jpg"

    elif style == "읽기/쓰기형 (Reading/Writing)":
        if goal == "기초 개념 익히기":
            return [
                "교재를 꼼꼼히 읽고 노트 필기를 정리하세요.",
                "배운 내용을 글로 요약해 블로그나 일지에 기록하세요."
            ], "reading_basic.jpg"
        else:
            return [
                "문제집 풀이와 서술형 답안을 작성해보세요.",
                "자신만의 요약집을 만들어 반복 학습하세요."
            ], "reading_study.jpg"

    return ["일반적인 학습 방법을 참고하세요."], "default.jpg"

# -------------------------------
# 추천 결과 출력
# -------------------------------
if name:
    st.subheader(f"👩‍🎓 {name} 님을 위한 맞춤 학습 방법")
    methods, img_file = recommend_method(subject, style, goal)
    for m in methods:
        st.success(m)
    img = Image.open(f"images/{img_file}")  # images 폴더에 미리 이미지 저장 필요
    st.image(img, caption=f"추천 학습 이미지 - {style}", use_column_width=True)

# -------------------------------
# 추가 기능: 랜덤 학습 명언
# -------------------------------
quotes = [
    "공부는 끝없는 여행이다. - 익명",
    "노력은 배신하지 않는다. - 손흥민",
    "성공은 작은 습관의 반복이다. - 아리스토텔레스",
    "배우기를 멈추면 성장을 멈춘다. - 익명",
    "성공은 준비된 자에게 온다. - 파스퇴르",
    "오늘의 노력은 내일의 자산이다. - 익명"
]
if st.button("오늘의 학습 명언 보기"):
    st.info(random.choice(quotes))
