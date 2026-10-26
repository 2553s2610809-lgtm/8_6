
import streamlit as st

# 기본 설정
st.set_page_config(
    page_title="천천히 키오스크",
    page_icon="☕",
    layout="centered"
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
        min-height: 60px;
        font-size: {font_size};
        font-weight: bold;
        border-radius: 12px;
        border: 2px solid #C8A27A;
    }}

    div.stButton > button:hover {{
        background-color: #F1DFC7;
        border-color: #8B5E3C;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# 페이지 이동 함수
def move_page(page):
    st.session_state.page = page


# 공통 제목
st.title("☕ 천천히 키오스크")
st.caption("어르신을 위한 쉬운 키오스크 사용 연습")


# =================================
# 1. 메인 화면
# =================================
if st.session_state.page == "home":

    st.subheader("안녕하세요!")

    st.info(
        "키오스크 사용이 어려우신가요?\n\n"
        "걱정하지 마세요. 천천히 하나씩 배워봐요!"
    )

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
        move_page("order")
        st.rerun()

    if st.button(
        "📖 키오스크 사용 방법 배우기",
        use_container_width=True
    ):
        move_page("guide")
        st.rerun()

    if st.button(
        "💡 자주 묻는 질문",
        use_container_width=True
    ):
        move_page("faq")
        st.rerun()

    st.divider()

    st.success(
        "실수해도 괜찮습니다!\n\n"
        "천천히 읽고 따라 해 보세요."
    )


# =================================
# 2. 키오스크 주문 연습
# =================================
elif st.session_state.page == "order":

    st.header("☕ 주문 연습하기")

    st.write("원하는 음료를 선택해 주세요.")

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
    st.write(f"주문 수량: {quantity}잔")

    st.success(f"총금액: {total:,}원")

    st.warning(
        "연습용 화면입니다. 실제 결제는 이루어지지 않습니다."
    )

    if st.button(
        "🏠 메인 화면으로 돌아가기",
        use_container_width=True
    ):
        move_page("home")
        st.rerun()


# =================================
# 3. 키오스크 사용 방법
# =================================
elif st.session_state.page == "guide":

    st.header("📖 키오스크 사용 방법")

    st.subheader("1. 메뉴 선택하기")
    st.write(
        "화면에서 먹고 싶은 음식이나 음료를 선택하세요."
    )

    st.subheader("2. 수량 선택하기")
    st.write(
        "주문할 음식이나 음료가 몇 개인지 선택하세요."
    )

    st.subheader("3. 금액 확인하기")
    st.write(
        "선택한 메뉴와 수량, 총금액이 맞는지 확인하세요."
    )

    st.subheader("4. 결제하기")
    st.write(
        "실제 매장에서는 화면의 안내에 따라 결제하세요. "
        "어려우면 직원에게 도움을 요청해도 괜찮습니다."
    )

    st.info(
        "모든 키오스크의 사용 방법이 같지는 않습니다. "
        "화면에 나오는 안내를 천천히 확인하세요."
    )

    if st.button(
        "🏠 메인 화면으로 돌아가기",
        use_container_width=True
    ):
        move_page("home")
        st.rerun()


# =================================
# 4. 자주 묻는 질문
# =================================
elif st.session_state.page == "faq":

    st.header("💡 자주 묻는 질문")

    with st.expander("메뉴를 잘못 선택했어요."):

        st.write(
            "괜찮습니다. 주문을 확정하기 전이라면 "
            "이전 화면으로 돌아가 다시 선택할 수 있습니다."
        )

    with st.expander("글씨가 너무 작아요."):

        st.write(
            "메인 화면의 '글씨 크기 바꾸기' 버튼을 "
            "눌러 글씨 크기를 조절하세요."
        )

    with st.expander("결제 방법을 모르겠어요."):

        st.write(
            "화면의 안내를 천천히 읽어 보세요. "
            "어려우면 매장 직원에게 도움을 요청하세요."
        )

    with st.expander("주문하다가 실수하면 어떡하죠?"):

        st.write(
            "당황하지 마세요. 주문 내용을 다시 확인하고 "
            "필요하면 직원에게 도움을 요청하세요."
        )

    if st.button(
        "🏠 메인 화면으로 돌아가기",
        use_container_width=True
    ):
        move_page("home")
        st.rerun()


# =================================
# 하단 안내
# =================================
st.divider()

st.caption(
    "천천히 키오스크 | 누구나 쉽게 배우는 디지털 세상"
)

