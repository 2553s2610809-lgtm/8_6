
import streamlit as st

# =================================
# 1. 기본 설정
# =================================

st.set_page_config(
    page_title="편한결제",
    page_icon="💳",
    layout="centered"
)

# =================================
# 2. 디자인
# =================================

st.markdown("""
<style>
.stApp {
    background-color: #EAF2FA;
}

h1, h2, h3 {
    color: #174A78;
}

div.stButton > button {
    width: 100%;
    height: 70px;
    border-radius: 15px;
    background-color: white;
    color: #174A78;
    border: 1px solid #D7E0E8;
    font-size: 19px;
    font-weight: bold;
}

div.stButton > button:hover {
    border: 2px solid #1769AA;
    color: #1769AA;
}

</style>
""", unsafe_allow_html=True)

# =================================
# 3. 화면 상태
# =================================

if "page" not in st.session_state:
    st.session_state.page = "홈"

if "transfer_info" not in st.session_state:
    st.session_state.transfer_info = None


# =================================
# 4. 화면 이동 함수
# =================================

def go(page):
    st.session_state.page = page
    st.rerun()


def back_home():
    if st.button("🏠 홈으로 돌아가기"):
        st.session_state.transfer_info = None
        go("홈")


# =================================
# 5. 상단 로고
# =================================

st.title("💳 편한결제")
st.caption("누구나 쉽고 편하게")
st.divider()


# =================================
# 6. 홈 화면
# =================================

def home():

    st.subheader("안녕하세요!")
    st.write("편한결제를 이용해 주셔서 감사합니다.")

    st.markdown("""
    ### 💰 내 잔액
    # 125,000원
    """)

    st.caption("나의 결제 정보를 간편하게 확인하세요.")

    st.divider()

    st.subheader("원하는 메뉴를 선택해 주세요.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💳 결제하기"):
            go("결제")

    with col2:
        if st.button("💸 송금하기"):
            go("송금")

    col3, col4 = st.columns(2)

    with col3:
        if st.button("📋 사용 내역"):
            go("내역")

    with col4:
        if st.button("☎️ 도움 요청"):
            go("도움")

    st.divider()

    st.subheader("편한결제 이용 안내")
    st.write("✔ 큰 글씨로 쉽게 확인할 수 있어요.")
    st.write("✔ 간단한 메뉴로 편리하게 이용할 수 있어요.")
    st.write("✔ 누구나 쉽게 사용할 수 있어요.")

    st.caption("편한결제는 앱 화면 시연을 위한 모형입니다.")


# =================================
# 7. 결제 화면
# =================================

def payment():

    st.title("💳 결제하기")
    st.write("원하는 결제 방법을 선택해 주세요.")

    method = st.radio(
        "결제 방식",
        ["QR코드", "바코드", "NFC"],
        horizontal=True
    )

    st.divider()

    if method == "QR코드":

        st.subheader("▦ QR코드 결제")

        st.info("QR코드를 이용한 결제 화면입니다.")

        st.markdown("""
        <div style="
            background:white;
            padding:35px;
            border-radius:15px;
            text-align:center;
            color:#174A78;
        ">
            <div style="font-size:90px;">▦</div>
            <div style="font-size:22px;">QR 결제 예시</div>
            <div>화면 시연용 이미지입니다.</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("① 가게의 QR코드를 확인합니다.")
        st.write("② 결제할 금액을 확인합니다.")
        st.write("③ 결제를 진행합니다.")

    elif method == "바코드":

        st.subheader("▥ 바코드 결제")

        st.markdown("""
        <div style="
            background:white;
            padding:35px;
            border-radius:15px;
            text-align:center;
            color:#174A78;
        ">
            <div style="font-size:70px;">▥ ▥ ▥</div>
            <div style="font-size:22px;">바코드 결제 예시</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("① 바코드 결제를 선택합니다.")
        st.write("② 결제 화면을 직원에게 보여 줍니다.")
        st.write("③ 금액을 확인합니다.")

    else:

        st.subheader("📡 NFC 간편결제")

        st.markdown("""
        <div style="
            background:white;
            padding:35px;
            border-radius:15px;
            text-align:center;
            color:#174A78;
        ">
            <div style="font-size:70px;">📱</div>
            <div style="font-size:22px;">NFC 결제 예시</div>
            <div>휴대전화를 단말기에 가까이 대는 방식입니다.</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("① NFC 결제를 선택합니다.")
        st.write("② 휴대전화를 결제 단말기에 가까이 댑니다.")
        st.write("③ 결제 내용을 확인합니다.")

    st.warning("QR·바코드·NFC는 화면 시연용이며 실제 결제는 지원하지 않습니다.")

    back_home()


# =================================
# 8. 송금 화면
# =================================

def transfer():

    st.title("💸 송금하기")
    st.write("받는 사람과 송금 정보를 입력해 주세요.")

    if st.session_state.transfer_info is None:

        with st.form("transfer_form"):

            bank = st.selectbox(
                "은행 선택",
                [
                    "국민은행",
                    "신한은행",
                    "우리은행",
                    "하나은행",
                    "농협은행",
                    "카카오뱅크"
                ]
            )

            account = st.text_input(
                "계좌번호",
                placeholder="예: 000-0000-0000"
            )

            name = st.text_input(
                "받는 사람 이름",
                placeholder="예: 홍길동"
            )

            amount = st.number_input(
                "송금 금액",
                min_value=1000,
                max_value=1000000,
                step=1000
            )

            submit = st.form_submit_button(
                "송금 정보 확인",
                use_container_width=True
            )

            if submit:

                if not account.strip() or not name.strip():
                    st.warning("계좌번호와 받는 사람 이름을 입력해 주세요.")

                else:
                    st.session_state.transfer_info = {
                        "bank": bank,
                        "account": account,
                        "name": name,
                        "amount": int(amount)
                    }
                    st.rerun()

    else:

        info = st.session_state.transfer_info

        st.subheader("송금 정보 확인")

        st.write("은행:", info["bank"])
        st.write("계좌번호:", info["account"])
        st.write("받는 사람:", info["name"])
        st.write("송금 금액:", f'{info["amount"]:,}원')

        st.warning("실제 송금은 이루어지지 않는 시연용 화면입니다.")

        if st.button("확인 완료"):
            st.success("송금 정보 확인이 완료되었습니다!")
            st.session_state.transfer_info = None

        if st.button("다시 입력하기"):
            st.session_state.transfer_info = None
            st.rerun()

    back_home()


# =================================
# 9. 사용 내역
# =================================

def history():

    st.title("📋 사용 내역")

    st.info("아직 등록된 사용 내역이 없습니다.")

    st.write("결제 및 송금 이용 내역을 확인하는 메뉴입니다.")

    back_home()


# =================================
# 10. 도움 요청
# =================================

def help_page():

    st.title("☎️ 도움 요청")

    st.write("궁금한 내용을 선택해 주세요.")

    question = st.selectbox(
        "도움이 필요한 항목",
        [
            "결제하는 방법",
            "QR코드 사용 방법",
            "바코드 사용 방법",
            "NFC 사용 방법",
            "송금하는 방법",
            "사용 내역 확인 방법"
        ]
    )

    st.divider()

    manuals = {
        "결제하는 방법": [
            "1. 홈 화면에서 결제하기를 누릅니다.",
            "2. 원하는 결제 방식을 선택합니다.",
            "3. 안내에 따라 결제 내용을 확인합니다."
        ],
        "QR코드 사용 방법": [
            "1. 결제 화면에서 QR코드를 선택합니다.",
            "2. 가게의 QR코드를 확인합니다.",
            "3. 결제 금액을 확인합니다."
        ],
        "바코드 사용 방법": [
            "1. 결제 화면에서 바코드를 선택합니다.",
            "2. 바코드를 직원에게 보여 줍니다.",
            "3. 결제 내용을 확인합니다."
        ],
        "NFC 사용 방법": [
            "1. NFC 결제 방식을 선택합니다.",
            "2. 휴대전화를 결제 단말기에 가까이 댑니다.",
            "3. 결제 내용을 확인합니다."
        ],
        "송금하는 방법": [
            "1. 홈 화면에서 송금하기를 누릅니다.",
            "2. 은행과 계좌번호를 입력합니다.",
            "3. 받는 사람과 금액을 확인합니다."
        ],
        "사용 내역 확인 방법": [
            "1. 홈 화면으로 돌아갑니다.",
            "2. 사용 내역을 누릅니다.",
            "3. 이용 내역을 확인합니다."
        ]
    }

    st.subheader("📖 사용 설명서")

    for step in manuals[question]:
        st.write("✔ " + step)

    st.divider()

    st.success("도움이 되었나요? 편한결제를 이용해 주셔서 감사합니다.")

    back_home()


# =================================
# 11. 실제 화면 표시
# =================================

if st.session_state.page == "홈":
    home()

elif st.session_state.page == "결제":
    payment()

elif st.session_state.page == "송금":
    transfer()

elif st.session_state.page == "내역":
    history()

elif st.session_state.page == "도움":
    help_page()
