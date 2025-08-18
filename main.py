import streamlit as st

# MBTI 유형 및 추천 직업 딕셔너리
mbti_jobs = {
    "ISTJ": ["회계사", "감리자", "군인"],
    "ISFJ": ["간호사", "사회복지사", "교사"],
    "INFJ": ["심리상담가", "작가", "사회운동가"],
    "INTJ": ["연구원", "엔지니어", "컴퓨터 프로그래머"],
    "ISTP": ["기술자", "기계공학자", "파일럿"],
    "ISFP": ["예술가", "디자이너", "사진작가"],
    "INFP": ["작가", "상담사", "비영리 기관 종사자"],
    "INTP": ["과학자", "기술 전문가", "분석가"],
    "ESTP": ["영업 전문가", "위기관리자", "비즈니스 컨설턴트"],
    "ESFP": ["연예인", "이벤트 플래너", "항공승무원"],
    "ENFP": ["광고기획자", "콘텐츠 크리에이터", "교육자"],
    "ENTP": ["창업가", "변호사", "기술 혁신가"],
    "ESTJ": ["경영자", "행정가", "경찰관"],
    "ESFJ": ["간호사", "교사", "인사 담당자"],
    "ENFJ": ["멘토", "지도자", "사회사업가"],
    "ENTJ": ["경영자", "전략 기획자", "법률가"]
}

st.title("MBTI 기반 직업 추천 진로 교육 사이트")

# 사용자에게 MBTI 유형 선택받기
mbti_select = st.selectbox("당신의 MBTI 유형을 선택하세요.", list(mbti_jobs.keys()))

if st.button("추천 직업 보기"):
    recommended_jobs = mbti_jobs.get(mbti_select, [])
    if recommended_jobs:
        st.success(f"{mbti_select} 유형에 적합한 직업들:")
        for job in recommended_jobs:
            st.write(f"- {job}")
    else:
        st.write("추천 직업이 없습니다.")

