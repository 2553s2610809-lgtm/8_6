
import streamlit as st
from datetime import datetime

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="편한결제",
    page_icon="💳",
    layout="wide"
)

BG = "#EAF2FA"
BLUE = "#1769AA"
DARK_BLUE = "#174A78"
TEXT_BLUE = "#58738D"
SILVER = "#D7E0E8"

# -----------------------------
# 데이터 저장
# -----------------------------
if "balance" not in st.session_state:
    st.session_state.balance = 125000

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {
            "kind": "결제",
            "name": "동네 마트",
            "amount": -5000,
            "time": "오늘 오후 2:10"
        },
        {
            "kind": "결제",
            "name": "동네 약국",
            "amount": -8000,
            "time": "오늘 오전 11:30"
        }
    ]

if "page" not in st.session_state:
    st.session_state.page = "홈"

# -----------------------------
# 디자인 CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #EAF2FA;
}

header[data-testid="stHeader"] {
    background-color: #EAF2FA;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 1200px;
}

h1, h2, h3, p, label {
    color: #174A78;
}

.balance-card {
    background: white;
    padding: 28px;
    border-radius: 22px;
    margin: 15px 0;
}

.balance-title {
    color: #58738D;
    font-size: 20px;
}

.balance-number {
    color: #174A78;
    font-size: 36px;
    font-weight: bold;
    margin: 8px 0;
}

.balance-info {
    color: #58738D;
    font-size: 17px;
}

div.stButton > button {
    width: 100%;
    min-height: 125px;
    border-radius: 20px;
    border: none;
    background-color: white;
    color: #174A78;
    font-size: 23px;
    font-weight: bold;
}

div.stButton > button:hover {
    border: 2px solid #1769AA;
    color: #1769AA;
}

div[data-testid="stForm"] {
    background: white;
    padding: 22px;
    border-radius: 20px;
}

input {
    font-size: 20px !important;
}

div[data-testid="stMarkdownContainer"] p {
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 상단 로고
# -----------------------------
st.markdown("""
<div style="
    display:flex;
    align-items:center;
    gap:15px;
    margin-bottom:20px;
">
    <div style="
        background:#1769AA;
        color:white;
        padding:13px 20px;
        border-radius:16px;
        font-size:30px;
    ">▣</div>

    <div>
        <div style="
            font-size:27px;
            font-weight:bold;
            color:#174A78;
        ">편한결제</div>

        <div style="
            font-size:17px;
            color:#58738D;
        ">누구나 쉽고 편하게</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 공통 함수
# -----------------------------
def go_home():
    st.session_state.page = "홈"


def add_transaction(kind, name, amount):
    st.session_state.balance += amount

    st.session_state.transactions.insert(0, {
        "kind": kind,
        "name": name,
        "amount": amount,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    })


def back_button():
    if st.button("← 처음으로", key="back"):
        go_home()
        st.rerun()


# -----------------------------
# 홈 화면
# -----------------------------
def home():

    st.markdown(f"""
    <div class="balance-card">
        <div class="balance-title">내 잔액</div>
        <div class="balance-number">
            {st.session_state.balance:,}원
        </div>
        <div class="balance-info">
            ♢ 안전하게 관리되는 내 돈
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▧\n결제하기\nQR코드로 간편하게",
                     key="pay_home"):
            st.session_state.page = "결제"
            st.rerun()

    with col2:
        if st.button("➤\n송금하기\n소중한 분께 간편하게",
                     key="send_home"):
            st.session_state.page = "송금"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        if st.button("▤\n사용 내역\n돈 쓴 기록 확인",
                     key="history_home"):
            st.session_state.page = "내역"
            st.rerun()

    with col4:
        if st.button("☏\n도움받기\n사용 방법 안내",
                     key="help_home"):
            st.session_state.page = "도움"
            st.rerun()

    st.caption("시연용 앱 · 실제 금융기관과 연결되어 있지 않습니다.")


# -----------------------------
# 결제 화면
# -----------------------------
def payment():

    st.title("💳 결제하기")
    st.write("결제할 곳과 금액을 입력해 주세요.")

    st.write(f"현재 잔액: **{st.session_state.balance:,}원**")

    with st.form("payment_form"):

        shop = st.text_input("가게 이름")
        amount = st.number_input(
            "결제 금액 (원)",
            min_value=0,
            step=1000
        )

        submitted = st.form_submit_button(
            "결제 확인",
            use_container_width=True
        )

        if submitted:

            if not shop.strip():
                st.warning("가게 이름을 입력해 주세요.")

            elif amount <= 0:
                st.warning("결제 금액을 입력해 주세요.")

            elif amount > st.session_state.balance:
                st.error("잔액이 부족합니다.")

            else:
                st.session_state.pending = {
                    "kind": "결제",
                    "name": shop.strip(),
                    "amount": int(amount)
                }

    if "pending" in st.session_state:
        item = st.session_state.pending

        if item["kind"] == "결제":
            st.warning(
                f"{item['name']}에서 "
                f"{item['amount']:,}원을 결제할까요?"
            )

            c1, c2 = st.columns(2)

            with c1:
                if st.button("최종 결제하기"):
                    if item["amount"] <= st.session_state.balance:
                        add_transaction(
                            "결제",
                            item["name"],
                            -item["amount"]
                        )
                        del st.session_state.pending
                        st.success("결제가 완료되었습니다!")
                        st.rerun()

            with c2:
                if st.button("취소"):
                    del st.session_state.pending
                    st.rerun()

    back_button()


# -----------------------------
# 송금 화면
# -----------------------------
def transfer():

    st.title("➤ 송금하기")
    st.write("받는 분과 금액을 입력해 주세요.")

    st.write(f"현재 잔액: **{st.session_state.balance:,}원**")

    with st.form("transfer_form"):

        recipient = st.text_input("받는 분 이름")

        amount = st.number_input(
            "송금 금액 (원)",
            min_value=0,
            step=1000
        )

        submitted = st.form_submit_button(
            "송금 확인",
            use_container_width=True
        )

        if submitted:

            if not recipient.strip():
                st.warning("받는 분 이름을 입력해 주세요.")

            elif amount <= 0:
                st.warning("송금 금액을 입력해 주세요.")

            elif amount > st.session_state.balance:
                st.error("잔액이 부족합니다.")

            else:
                st.session_state.pending = {
                    "kind": "송금",
                    "name": recipient.strip(),
                    "amount": int(amount)
                }

    if "pending" in st.session_state:
        item = st.session_state.pending

        if item["kind"] == "송금":
            st.warning(
                f"{item['name']}님에게 "
                f"{item['amount']:,}원을 송금할까요?"
            )

            c1, c2 = st.columns(2)

            with c1:
                if st.button("최종 송금하기"):
                    if item["amount"] <= st.session_state.balance:
                        add_transaction(
                            "송금",
                            item["name"],
                            -item["amount"]
                        )
                        del st.session_state.pending
                        st.success("송금 처리가 완료되었습니다!")
                        st.rerun()

            with c2:
                if st.button("취소"):
                    del st.session_state.pending
                    st.rerun()

    back_button()


# -----------------------------
# 사용 내역 화면
# -----------------------------
def history():

    st.title("📋 사용 내역")
    st.write("최근 결제 및 송금 기록입니다.")

    for item in st.session_state.transactions:

        with st.container(border=True):

            c1, c2 = st.columns([3, 1])

            with c1:
                st.subheader(
                    f"{item['kind']} · {item['name']}"
                )
                st.caption(item["time"])

            with c2:
                st.markdown(
                    f"### {item['amount']:+,}원"
                )

    back_button()


# -----------------------------
# 도움받기 화면
# -----------------------------
def help_page():

    st.title("☎ 도움받기")
    st.write("편한결제를 사용하는 방법을 안내해 드립니다.")

    tips = [
        ("1. 결제하기",
         "가게 이름과 금액을 입력하고 결제 확인을 누르세요."),

        ("2. 송금하기",
         "받는 분 이름과 금액을 입력한 뒤 내용을 확인하세요."),

        ("3. 사용 내역",
         "결제와 송금 기록을 확인할 수 있습니다."),

        ("4. 안전하게 사용하기",
         "확인 화면에서 이름과 금액을 꼭 살펴보세요.")
    ]

    for title, description in tips:

        with st.container(border=True):
            st.subheader(title)
            st.write(description)

    back_button()


# -----------------------------
# 화면 이동
# -----------------------------
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
