
import streamlit as st

# 기본 설정
st.set_page_config(
    page_title="편한결제",
    page_icon="💳",
    layout="centered"
)

# 배경 및 디자인
st.markdown("""
<style>
.stApp {
    background-color: #EAF2FA;
}

h1, h2, h3, p {
    color: #174A78;
}

div.stButton > button {
    width: 100%;
    height: 75px;
    background-color: white;
    color: #174A78;
    border: 1px solid #D7E0E8;
    border-radius: 15px;
    font-size: 20px;
    font-weight: bold;
}

div.stButton > button:hover {
    border: 2px solid #1769AA;
    color: #1769AA;
}
</style>
""", unsafe_allow_html=True)

# 로고와 제목
st.title("💳 편한결제")
st.write("누구나 쉽고 편하게")

st.divider()

# 잔액 표시
st.subheader("내 잔액")

st.markdown("""
### 125,000원
""")

st.caption("나의 결제 정보를 한눈에 확인해 보세요.")

st.divider()

# 메뉴
st.subheader("무엇을 도와드릴까요?")

col1, col2 = st.columns(2)

with col1:
    if st.button("💳 결제하기"):
        st.info("결제 서비스 준비 중입니다.")

with col2:
    if st.button("💸 송금하기"):
        st.info("송금 서비스 준비 중입니다.")

col3, col4 = st.columns(2)

with col3:
    if st.button("📋 사용 내역"):
        st.info("아직 등록된 사용 내역이 없습니다.")

with col4:
    if st.button("☎️ 도움받기"):
        st.info("도움이 필요하시면 안내 데스크에 문의해 주세요.")

st.divider()

# 하단 안내
st.subheader("편한결제 이용 안내")

st.write("✔️ 큰 글씨로 쉽게 확인할 수 있어요.")
st.write("✔️ 간단한 메뉴로 편리하게 이용할 수 있어요.")
st.write("✔️ 누구나 쉽게 사용할 수 있도록 만들었어요.")

st.caption("편한결제 · 누구나 쉽고 편하게")
