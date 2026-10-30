
import streamlit as st

st.set_page_config(
    page_title="편한결제",
    page_icon="💳",
    layout="centered"
)

# 디자인
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
    min-height: 60px;
    background-color: white;
    color: #174A78;
    border-radius: 15px;
    border: 1px solid #D7E0E8;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.title("💳 편한결제")
st.write("누구나 쉽고 편하게")
st.divider()

# 잔액
st.subheader("💰 내 잔액")
st.title("125,000원")
st.caption("나의 결제 정보를 확인해 보세요.")

st.divider()

# 결제
st.header("💳 결제하기")
st.write("원하는 결제 방식을 선택하세요.")

method = st.radio(
    "결제 방식",
    ["QR코드", "바코드", "NFC"],
    horizontal=True,
    key="method"
)

if method == "QR코드":
    st.info("▦ QR코드 결제 화면")
    st.write("가게의 QR코드를 확인하고 결제하는 방식입니다.")

elif method == "바코드":
    st.info("▥ 바코드 결제 화면")
    st.write("화면의 바코드를 직원에게 보여 주는 방식입니다.")

else:
    st.info("📱 NFC 결제 화면")
    st.write("휴대전화를 결제 단말기에 가까이 대는 방식입니다.")

st.caption("※ 결제 기능은 설명용이며 실제 결제는 되지 않습니다.")

st.divider()

# 송금
st.header("💸 송금하기")

bank = st.selectbox(
    "은행 선택",
    ["국민은행", "신한은행", "우리은행", "하나은행", "농협은행", "카카오뱅크"]
)

account = st.text_input("계좌번호", placeholder="예시 계좌번호")
recipient = st.text_input("받는 사람")

amount = st.number_input(
    "송금 금액",
    min_value=1000,
    step=1000
)

if st.button("송금 정보 확인"):
    if not account.strip() or not recipient.strip():
        st.warning("계좌번호와 받는 사람을 입력해 주세요.")
    else:
        st.success("송금 정보 확인 화면")
        st.write("은행:", bank)
        st.write("계좌번호:", account)
        st.write("받는 사람:", recipient)
        st.write("금액:", f"{amount:,.0f}원")
        st.info("시연용 화면입니다. 실제 송금은 이루어지지 않습니다.")

st.divider()

# 사용 내역
st.header("📋 사용 내역")
st.info("아직 등록된 사용 내역이 없습니다.")

st.divider()

# 도움말
st.header("☎️ 도움 요청")

question = st.selectbox(
    "궁금한 내용을 선택하세요.",
    [
        "결제하는 방법",
        "QR코드 사용 방법",
        "바코드 사용 방법",
        "NFC 사용 방법",
        "송금하는 방법",
        "사용 내역 확인 방법"
    ]
)

manuals = {
    "결제하는 방법":
        "결제하기에서 원하는 결제 방식을 선택하고 안내를 확인하세요.",
    "QR코드 사용 방법":
        "QR코드 방식을 선택한 뒤 가게의 QR코드를 확인하세요.",
    "바코드 사용 방법":
        "바코드 방식을 선택한 뒤 화면을 직원에게 보여 주세요.",
    "NFC 사용 방법":
        "NFC 기능이 있는 휴대전화를 결제 단말기에 가까이 대는 방식입니다.",
    "송금하는 방법":
        "은행, 계좌번호, 받는 사람과 금액을 입력한 뒤 정보를 확인하세요.",
    "사용 내역 확인 방법":
        "사용 내역 메뉴에서 결제 및 송금 기록을 확인할 수 있습니다."
}

st.success(manuals[question])

st.divider()

st.caption("편한결제 | 누구나 쉽고 편하게")
st.caption("이 앱은 학교 과제 및 화면 시연을 위한 모형입니다.")
