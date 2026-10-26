import streamlit as st

st.set_page_config(
    page_title="천천히 키오스크",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "home"

if "large_font" not in st.session_state:
    st.session_state.large_font = True

# 글씨 크기 설정
font_size = "24px" if st.session_state.large_font else "18px"

# 화면 디자인
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #FFF8EE;
    }}

    h1 {{
        color: #654321;
        text-align: center;
        font-size: 38px !important;
    }}

    h2, h3 {{
        color: #654321;
    }}

    p, label, .stMarkdown {{
        font-size: {font_size};
        line-height: 1.7;
    }}

    div.stButton > button {{
        width: 100%;
        min-height: 65px;
        font-size: {font_size} !important;
        font-weight: bold;
        border-radius: 15px;
        border: 2px solid #C8A27A;
        background-color: #FFFFFF;
        color: #493322;
    }}

    div.stButton > button:hover {{
        background-color: #F1DFC7;
        border-color: #8B5E3C;
        color: #493322;
    }}

    .welcome {{
        background-color: #F3E3CE;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        color: #493322;
        font-size: {font_size};
        line-height: 1.8;
        margin-bottom: 20px;
    }}

    .footer {{
        text-align: center;
        color: #6D5A48;
        font-size: 16px;
        padding: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# 페이지 이동 함수
def go_to(page):
    st.session_state.page = page
    st.rerun()


# 메인 화면
if st.session_state.page == "home":

    st.title("☕ 천천히 키오스크")

    st.markdown(
        """
        <div class="welcome">
            <strong>안녕하세요!</strong><br>
            키오스크 사용이 어려우신가요?<br>
            걱정하지 마세요.<br>
            천천히 하나씩 함께 배워봐요!
        </div>
        """,
        unsafe_allow_html=True
    )

    # 글씨 크기 조절
    if st.button(
        "🔎 글씨 크기 바꾸기",
        use_container_width=True
    ):
        st.session_state.large_font = (
            not st.session_state.large_font
        )
        st.rerun()

    st.divider()

    st.subheader("무엇을 도와드릴까요?")
    st.write("원하는 메뉴를 눌러 주세요.")

    if st.button(
        "☕ 키오스크 주문 연습하기",
        use_container_width=True
    ):
        go_to("practice")

    if st.button(
        "📖 키오스크 사용 방법 배우기",
        use_container_width=True
    ):
        go_to("guide")

    if st.button(
        "💡 자주 묻는 질문",
        use_container_width=True
    ):
        go_to("faq")

    st.divider()

    st.markdown(
        """
        <div class="welcome">
            <strong>기억하세요!</strong><br>
            실수해도 괜찮습니다.<br>
            천천히 읽고 따라 하면 됩니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer">
            누구나 쉽게 사용할 수 있는 디지털 세상을 위해
        </div>
        """,
        unsafe_allow_html=True
    )


# 키오스크 주문 연습 화면
elif st.session_state.page == "practice":

    st.title("☕ 주문 연습하기")

    st.write(
        "원하는 음료를 선택하고 주문 과정을 연습해 보세요."
    )

    menu = {
        "아메리카노": 2500,
        "카페라테": 3500,
        "바닐라라테": 4000,
        "레몬에이드": 4000
    }

    drink = st.selectbox(
        "어떤 음료를 주문하시겠어요?",
        list(menu.keys())
    )

    quantity = st.selectbox(
        "몇 잔을 주문하시겠어요?",
        [1, 2, 3, 4, 5]
    )

    total = menu[drink] * quantity

    st.subheader("주문 확인")
    st.write(f"선택한 음료: {drink}")
    st.write(f"수량: {quantity}잔")
    st.write(f"총금액: {total:,}원")

    st.info(
        "이 화면은 주문 연습용입니다. "
        "실제 결제는 이루어지지 않습니다."
    )

    if st.button("🏠 메인 화면으로 돌아가기"):
        go_to("home")


# 사용 방법 안내 화면
elif st.session_state.page == "guide":

    st.title("📖 사용 방법 배우기")

    st.subheader("1. 원하는 메뉴 고르기")
    st.write(
        "화면에 있는 메뉴를 천천히 읽고 "
        "먹고 싶은 음료를 선택하세요."
    )

    st.subheader("2. 주문 수량 선택하기")
    st.write(
        "몇 잔을 주문할지 선택하고 "
        "총금액을 확인하세요."
    )

    st.subheader("3. 주문 내용 확인하기")
    st.write(
        "메뉴와 수량이 맞는지 확인한 후 "
        "다음 단계로 이동하세요."
    )

    st.subheader("4. 결제하기")
    st.write(
        "실제 매장에서는 화면의 안내에 따라 "
        "결제를 진행하세요. 어려우면 직원에게 "
        "도움을 요청해도 괜찮습니다."
    )

    if st.button("🏠 메인 화면으로 돌아가기"):
        go_to("home")


# 자주 묻는 질문 화면
elif st.session_state.page == "faq":

    st.title("💡 자주 묻는 질문")

    with st.expander("메뉴를 잘못 선택했어요."):
        st.write(
            "괜찮습니다. 이전 화면으로 돌아가 "
            "원하는 메뉴를 다시 선택하면 됩니다."
        )

    with st.expander("글씨가 너무 작아요."):
        st.write(
            "메인 화면의 '글씨 크기 바꾸기' 버튼을 "
            "눌러 글씨 크기를 조절할 수 있습니다."
        )

    with st.expander("결제 방법을 모르겠어요."):
        st.write(
            "화면의 결제 안내를 천천히 읽어 보세요. "
            "필요하면 매장 직원에게 도움을 요청하세요."
        )

    with st.expander("실수하면 어떻게 하나요?"):
        st.write(
            "주문을 확정하기 전에는 이전 화면으로 "
            "돌아가 내용을 확인할 수 있습니다."
        )

    if st.button("🏠 메인 화면으로 돌아가기"):
        go_to("home")
