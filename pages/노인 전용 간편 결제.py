
import streamlit as st

# ==================================
# 1. 기본 설정
# ==================================

st.set_page_config(
    page_title="편한결제",
    page_icon="💳",
    layout="centered"
)

# ==================================
# 2. 디자인
# ==================================

st.markdown("""
<style>
.stApp {
    background-color: #EAF2FA;
}

h1, h2, h3, p, label {
    color: #174A78;
}

div.stButton > button {
    width: 100%;
    min-height: 65px;
    background-color: white;
    color: #174A78;
    border: 1px solid #D7E0E8;
    border-radius: 15px;
    font-size: 19px;
    font-weight: bold;
}

div.stButton > button:hover {
    border: 2px solid #1769AA;
    color: #1769AA;
}

div[data-testid="stForm"] {
    background-color: white;
    padding: 18px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)


# ==================================
# 3. 화면 상태
# ==================================

if "page" not in st.session_state:
    st.session_state.page = "홈"

if "payment_method" not in st.session_state:
    st.session_state.payment_method = "QR코드"

if "transfer_info" not in st.session_state:
    st.session_state.transfer_info = None


# ==================================
# 4. 공통 함수
# ==================================

def move_page(page):
    st.session_state.page = page
    st.rerun()


def back_home():
    if st.button("← 처음으로"):
        st.session_state.transfer_info = None
        move_page("홈")


# ==================================
# 5. 상단 로고
# ==================================

st.title("💳 편한결제")
st.caption("누구나 쉽고 편하게")
st.divider()


# ==================================
# 6. 홈 화면
# ==================================

def home():

    st.subheader("안녕하세요!")
    st.write("편한결제에 오신 것을 환영합니다.")

    st.markdown("""
    ### 💰 내 잔액
    # 125,000원
    """)

    st.caption("편리하고 간단한 결제 생활을 시작해 보세요.")

    st.divider()

    st.subheader("무엇을 도와드릴까요?")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("💳 결제하기"):
            move_page("결제")

    with c2:
        if st.button("💸 송금하기"):
            move_page("송금")

    c3, c4 = st.columns(2)

    with c3:
        if st.button("📋 사용 내역"):
            move_page("내역")

    with c4:
        if st.button("☎️ 도움 요청"):
            move_page("도움")

    st.divider()

    st.subheader("편한결제 이용 안내")
    st.write("✔ 큰 글씨로 쉽게 확인할 수 있어요.")
    st.write("✔ 간단한 메뉴로 편리하게 이용할 수 있어요.")
    st.write("✔ 누구나 쉽게 사용할 수 있어요.")


# ==================================
# 7. 결제 화면
# ==================================

def payment():

    st.title("💳 결제하기")
    st.write("원하는 결제 방식을 선택해 주세요.")

    method = st.radio(
        "결제 방식",
        ["QR코드", "바코드", "NFC"],
        horizontal=True,
        key="payment_method"
    )

    st.divider()

    if method == "QR코드":

        st.subheader("▦ QR코드 결제")

        st.info("아래는 결제 화면을 보여 주기 위한 예시입니다.")

        st.markdown("""
        <div style="
            background:white;
            border-radius:18px;
            padding:35px;
            text-align:center;
            border:2px solid #D7E0E8;
        ">
            <div style="font-size:75px;">▦</div>
            <div style="font-size:22px; color:#174A78;">
                QR 결제 예시 화면
            </div>
            <div style="font-size:15px; color:#58738D;">
                실제로 스캔할 수 있는 QR코드는 아닙니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("1. 결제할 가게의 QR코드를 확인합니다.")
        st.write("2. 결제 앱에서 QR 결제를 선택합니다.")
        st.write("3. 금액을 확인한 뒤 결제를 진행합니다.")

    elif method == "바코드":

        st.subheader("▥ 바코드 결제")

        st.markdown("""
        <div style="
            background:white;
            border-radius:18px;
            padding:35px;
            text-align:center;
            border:2px solid #D7E0E8;
        ">
            <div style="font-size:65px;">▥ ▥ ▥</div>
            <div style="font-size:22px; color:#174A78;">
                바코드 결제 예시
            </div>
            <div style="font-size:15px; color:#58738D;">
                시연용 화면입니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("1. 결제할 때 바코드 방식을 선택합니다.")
        st.write("2. 화면의 바코드를 직원에게 보여 줍니다.")
        st.write("3. 금액을 확인합니다.")

    else:

        st.subheader("📡 NFC 간편결제")

        st.markdown("""
        <div style="
            background:white;
            border-radius:18px;
            padding:35px;
            text-align:center;
            border:2px solid #D7E0E8;
        ">
            <div style="font-size:65px;">📱</div>
            <div style="font-size:22px; color:#174A78;">
                NFC 결제 화면
            </div>
            <div style="font-size:15px; color:#58738D;">
                휴대전화를 결제 단말기에 가까이 대는 방식입니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("1. NFC 결제 방식을 선택합니다.")
        st.write("2. 휴대전화를 결제 단말기에 가까이 댑니다.")
        st.write("3. 결제 금액을 확인합니다.")

    st.caption("※ QR·바코드·NFC 모두 화면 시연용이며 실제 결제는 지원하지 않습니다.")

    back_home()


# ==================================
# 8. 송금 화면
# ==================================

def transfer():

    st.title("💸 송금하기")
    st.write("받는 분과 송금 금액을 입력해 주세요.")

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

            submitted = st.form_submit_button(
                "송금 정보 확인",
                use_container_width=True
            )

            if submitted:

                if not name.strip():
                    st.warning("받는 사람 이름을 입력해 주세요.")

                else:
                    st.session_state.transfer_info = {
                        "bank": bank,
                        "name": name.strip(),
                        "amount": int(amount)
                    }
                    st.rerun()

    else:

        info = st.session_state.transfer_info

        st.subheader("송금 정보 확인")

        st.info("아래 내용이 맞는지 확인해 주세요.")

        st.write("**은행:**", info["bank"])
        st.write("**받는 사람:**", info["name"])
        st.write("**송금 금액:**", f'{info["amount"]:,}원')

        st.warning(
            "시연용 화면입니다. 실제 계좌번호를 입력하거나 "
            "실제 송금이 이루어지지 않습니다."
        )

        if st.button("확인 완료", use_container_width=True):
            st.success("송금 정보 확인이 완료되었습니다!")
            st.session_state.transfer_info = None

        if st.button("다시 입력하기", use_container_width=True):
            st.session_state.transfer_info = None
            st.rerun()

    back_home()


# ==================================
# 9. 사용 내역
# ==================================

def history():

    st.title("📋 사용 내역")

    st.info("아직 등록된 사용 내역이 없습니다.")

    st.write("앞으로의 결제 내역을 이곳에서 확인할 수 있습니다.")

    back_home()


# ==================================
# 10. 도움 요청
# ==================================

def help_page():

    st.title("☎️ 도움 요청")

    st.write("어떤 도움이 필요하신가요?")
    st.write("궁금한 항목을 선택하면 사용 방법을 알려드립니다.")

    question = st.selectbox(
        "질문 선택하기",
        [
            "결제는 어떻게 하나요?",
            "QR코드는 어떻게 사용하나요?",
            "바코드는 어떻게 사용하나요?",
            "NFC 결제는 무엇인가요?",
            "송금은 어떻게 하나요?",
            "사용 내역은 어디서 확인하나요?"
        ]
    )

    st.divider()

    if question == "결제는 어떻게 하나요?":

        st.subheader("💳 결제 방법")
        st.write("1. 홈 화면에서 결제하기를 누릅니다.")
        st.write("2. QR코드, 바코드, NFC 중 하나를 선택합니다.")
        st.write("3. 안내에 따라 결제 화면을 확인합니다.")

    elif question == "QR코드는 어떻게 사용하나요?":

        st.subheader("▦ QR코드 사용 방법")
        st.write("1. 결제 화면에서 QR코드를 선택합니다.")
        st.write("2. 가게의 QR코드를 확인합니다.")
        st.write("3. 결제 금액을 확인합니다.")

    elif question == "바코드는 어떻게 사용하나요?":

        st.subheader("▥ 바코드 사용 방법")
        st.write("1. 결제 화면에서 바코드를 선택합니다.")
        st.write("2. 바코드 화면을 직원에게 보여 줍니다.")
        st.write("3. 결제 내용을 확인합니다.")

    elif question == "NFC 결제는 무엇인가요?":

        st.subheader("📡 NFC 사용 방법")
        st.write("NFC는 휴대전화를 결제 단말기에 가까이 대어 정보를 주고받는 방식입니다.")
        st.write("실제 사용에는 NFC 기능과 결제 서비스 연결이 필요합니다.")

    elif question == "송금은 어떻게 하나요?":

        st.subheader("💸 송금 방법")
        st.write("1. 홈 화면에서 송금하기를 누릅니다.")
        st.write("2. 은행과 받는 사람 이름을 입력합니다.")
        st.write("3. 송금 금액을 입력하고 내용을 확인합니다.")

    elif question == "사용 내역은 어디서 확인하나요?":

        st.subheader("📋 사용 내역 확인")
        st.write("홈 화면에서 사용 내역을 누르면 확인할 수 있습니다.")

    st.divider()

    st.success("도움이 되었나요? 편한결제를 이용해 주셔서 감사합니다.")

    back_home()


# ==================================
# 11. 화면 실행
# ==================================

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
