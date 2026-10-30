
import streamlit as st
from datetime import datetime

# ==========================================
# 1. 기본 설정
# ==========================================

st.set_page_config(
    page_title="편한결제",
    page_icon="💳",
    layout="wide"
)

# ==========================================
# 2. 디자인 설정
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #EAF2FA;
}

header[data-testid="stHeader"] {
    background-color: #EAF2FA;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, label {
    color: #174A78;
}

.balance-card {
    background: white;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid #D7E0E8;
    margin: 20px 0;
}

.balance-title {
    color: #58738D;
    font-size: 22px;
}

.balance-number {
    color: #174A78;
    font-size: 42px;
    font-weight: bold;
    margin: 10px 0;
}

.balance-info {
    color: #58738D;
    font-size: 17px;
}

div.stButton > button {
    width: 100%;
    min-height: 85px;
    border-radius: 18px;
    border: 1px solid #D7E0E8;
    background-color: white;
    color: #174A78;
    font-size: 22px;
    font-weight: bold;
}

div.stButton > button:hover {
    border: 2px solid #1769AA;
    background-color: #F4F9FF;
    color: #1769AA;
}

div[data-testid="stForm"] {
    background: white;
    padding: 22px;
    border-radius: 20px;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    font-size: 20px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. 데이터 저장
# ==========================================

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

if "pending" not in st.session_state:
    st.session_state.pending = None


# ==========================================
# 4. 상단 로고
# ==========================================

st.markdown("""
<div style="
    display:flex;
    align-items:center;
    gap:15px;
    margin-bottom:25px;
">
    <div style="
        background:#1769AA;
        color:white;
        padding:13px 20px;
        border-radius:16px;
        font-size:30px;
        font-weight:bold;
    ">▣</div>

    <div>
        <div style="
            font-size:30px;
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


# ==========================================
# 5. 공통 기능
# ==========================================

def go_home():
    st.session_state.page = "홈"
    st.session_state.pending = None
    st.rerun()


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


def confirm_action(kind):
    item = st.session_state.pending

    if item is None or item["kind"] != kind:
        return

    if kind == "결제":
        st.warning(
            f"{item['name']}에서 "
            f"{item['amount']:,}원을 결제할까요?"
        )
    else:
        st.warning(
            f"{item['name']}님에게 "
            f"{item['amount']:,}원을 송금할까요?"
        )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("최종 확인", key="confirm_" + kind):
            if item["amount"] > st.session_state.balance:
                st.error("잔액이 부족합니다.")
                st.session_state.pending = None
                st.rerun()
            else:
                add_transaction(
                    kind,
                    item["name"],
                    -item["amount"]
                )
                st.session_state.pending = None
                st.success(f"{kind} 완료!")
                st.rerun()

    with col2:
        if st.button("취소", key="cancel_" + kind):
            st.session_state.pending = None
            st.rerun()


# ==========================================
# 6. 홈 화면
# ==========================================

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

    st.subheader("무엇을 도와드릴까요?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▧  결제하기", key="pay"):
            st.session_state.page = "결제"
            st.rerun()

    with col2:
        if st.button("➤  송금하기", key="send"):
            st.session_state.page = "송금"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        if st.button("▤  사용 내역", key="history"):
            st.session_state.page = "내역"
            st.rerun()

    with col4:
        if st.button("☎  도움받기", key="help"):
            st.session_state.page = "도움"
            st.rerun()

    st.divider()

    st.subheader("최근 사용 내역")

    for item in st.session_state.transactions[:3]:
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])

            with c1:
                st.write(f"**{item['name']}**")
                st.caption(item["time"])

            with c2:
                st.write(f"**{item['amount']:+,}원**")

    st.caption(
        "시연용 앱 · 실제 금융기관이나 계좌와 연결되어 있지 않습니다."
    )


# ==========================================
# 7. 결제 화면
# ==========================================

def payment():

    st.title("💳 결제하기")
    st.write("결제할 곳과 금액을 입력해 주세요.")

    st.write(
        f"현재 잔액: **{st.session_state.balance:,}원**"
    )

    with st.form("payment_form"):

        shop = st.text_input(
            "가게 이름",
            placeholder="예: 동네 마트"
        )

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
                st.rerun()

    confirm_action("결제")
    back_button()


# ==========================================
# 8. 송금 화면
# ==========================================

def transfer():

    st.title("➤ 송금하기")
    st.write("받는 분과 금액을 입력해 주세요.")

    st.write(
        f"현재 잔액: **{st.session_state.balance:,}원**"
    )

    with st.form("transfer_form"):

        recipient = st.text_input(
            "받는 분 이름",
            placeholder="예: 홍길동"
        )

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
                st.rerun()

    confirm_action("송금")
    back_button()


# ==========================================
# 9. 사용 내역 화면
# ==========================================

def history():

    st.title("📋 사용 내역")
    st.write("최근 결제 및 송금 기록입니다.")

    if not st.session_state.transactions:
        st.info("아직 사용 내역이 없습니다.")

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


# ==========================================
# 10. 도움받기 화면
# ==========================================

def help_page():

    st.title("☎ 도움받기")
    st.write("편한결제 사용 방법을 안내해 드립니다.")

    tips = [
        (
            "1. 결제하기",
            "가게 이름과 금액을 입력하고 결제 확인을 누르세요."
        ),
        (
            "2. 송금하기",
            "받는 분 이름과 금액을 입력한 뒤 내용을 확인하세요."
        ),
        (
            "3. 사용 내역",
            "결제와 송금 기록을 확인할 수 있습니다."
        ),
        (
            "4. 안전하게 사용하기",
            "최종 확인 화면에서 이름과 금액을 꼭 확인하세요."
        )
    ]

    for title, description in tips:
        with st.container(border=True):
            st.subheader(title)
            st.write(description)

    back_button()


# ==========================================
# 11. 앱 실행
# ==========================================

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
