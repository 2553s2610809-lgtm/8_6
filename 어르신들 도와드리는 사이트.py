 ```python
import streamlit as st

# ==========================================
# 1. 기본 설정
# ==========================================
st.set_page_config(
    page_title="천천히 키오스크",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. 세션 상태 초기화
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "font_level" not in st.session_state:
    st.session_state.font_level = 2

if "selected_drink" not in st.session_state:
    st.session_state.selected_drink = "아메리카노"

if "quantity" not in st.session_state:
    st.session_state.quantity = 1

# ==========================================
# 3. 글자 크기 설정
# ==========================================
FONT_SIZES = {
    0: ("작은 글씨", 20, 30, 19),
    1: ("보통 글씨", 24, 36, 22),
    2: ("큰 글씨", 28, 42, 26),
    3: ("아주 큰 글씨", 32, 46, 30),
}

font_name, body_size, title_size, button_size = FONT_SIZES[
    st.session_state.font_level
]

# ==========================================
# 4. 음료 메뉴
# ==========================================
DRINKS = {
    "아메리카노": {"price": 2500, "emoji": "☕"},
    "카페라테": {"price": 3500, "emoji": "🥛"},
    "바닐라라테": {"price": 4000, "emoji": "☕"},
    "카라멜마키아토": {"price": 4500, "emoji": "🍮"},
    "카푸치노": {"price": 3800, "emoji": "☕"},
    "카페모카": {"price": 4300, "emoji": "🍫"},
    "화이트초콜릿모카": {"price": 4500, "emoji": "🍫"},
    "초코라테": {"price": 4000, "emoji": "🍫"},
    "녹차라테": {"price": 4000, "emoji": "🍵"},
    "고구마라테": {"price": 4200, "emoji": "🍠"},
    "딸기라테": {"price": 4500, "emoji": "🍓"},
    "말차라테": {"price": 4300, "emoji": "🍵"},
    "레몬에이드": {"price": 4000, "emoji": "🍋"},
    "자몽에이드": {"price": 4200, "emoji": "🍊"},
    "청포도에이드": {"price": 4200, "emoji": "🍇"},
    "딸기스무디": {"price": 4500, "emoji": "🍓"},
    "망고스무디": {"price": 4500, "emoji": "🥭"},
    "플레인요거트스무디": {"price": 4500, "emoji": "🥣"},
    "복숭아아이스티": {"price": 3000, "emoji": "🍑"},
    "캐모마일차": {"price": 3000, "emoji": "🌼"},
    "녹차": {"price": 2500, "emoji": "🍵"},
    "레몬차": {"price": 3000, "emoji": "🍋"},
    "유자차": {"price": 3000, "emoji": "🍯"},
    "초코우유": {"price": 3000, "emoji": "🥛"},
}

# ==========================================
# 5. 예쁜 배경과 전체 글자 디자인
# ==========================================
st.markdown(
    f"""
    <style>
    /* 전체 배경 */
    .stApp {{
        background: linear-gradient(
            150deg,
            #FFF8E9 0%,
            #F0F7E9 48%,
            #E5F0E4 100%
        );
    }}

    /* 기본 글자 */
    html, body, [class*="css"] {{
        font-size: {body_size}px;
    }}

    /* 본문 글씨 */
    .stMarkdown p,
    .stMarkdown li,
    .stMarkdown ol,
    .stMarkdown ul,
    .stText,
    [data-testid="stWidgetLabel"] p,
    [data-testid="stCaptionContainer"] p,
    [data-testid="stAlert"] p,
    [data-testid="stExpander"] p {{
        font-size: {body_size}px !important;
        line-height: 1.7 !important;
        color: #344536;
    }}

    /* 제목 */
    h1 {{
        font-size: {title_size}px !important;
        color: #31543B !important;
        font-weight: 900 !important;
        line-height: 1.35 !important;
    }}

    h2 {{
        font-size: {body_size + 8}px !important;
        color: #31543B !important;
        line-height: 1.5 !important;
    }}

    h3 {{
        font-size: {body_size + 4}px !important;
        color: #42664A !important;
        line-height: 1.5 !important;
    }}

    /* 버튼 */
    div.stButton > button {{
        width: 100%;
        min-height: 68px;
        height: auto;
        padding: 12px;
        border-radius: 16px;
        border: 2px solid #B7CDAE;
        background-color: #FFFFFF;
        color: #31543B;
        font-size: {button_size}px !important;
        font-weight: 800 !important;
        white-space: normal;
        line-height: 1.5;
        transition: 0.2s;
    }}

    div.stButton > button:hover {{
        background-color: #E1EEDB;
        border-color: #668C69;
        color: #24452C;
    }}

    /* 입력 상자와 선택 메뉴 */
    div[data-baseweb="select"] > div {{
        min-height: 58px;
        border-radius: 12px;
        border-color: #B7CDAE;
    }}

    div[data-baseweb="select"] * {{
        font-size: {body_size}px !important;
    }}

    /* 안내 상자 */
    div[data-testid="stAlert"] {{
        border-radius: 16px;
    }}

    /* 구분선 */
    hr {{
        border-color: #C9DAC2;
    }}

    /* 메뉴 카드 */
    .drink-card {{
        background: rgba(255, 255, 255, 0.92);
        border: 2px solid #D5E3CD;
        border-radius: 20px;
        padding: 18px;
        text-align: center;
        margin: 8px 0;
        box-shadow: 0 4px 12px rgba(65, 92, 65, 0.08);
    }}

    .drink-emoji {{
        font-size: 42px;
        margin-bottom: 8px;
    }}

    .drink-name {{
        font-size: {body_size}px;
        font-weight: 800;
        color: #31543B;
        line-height: 1.5;
    }}

    .drink-price {{
        font-size: {body_size}px;
        color: #6A785E;
        margin-top: 8px;
    }}

    /* 환영 상자 */
    .welcome-card {{
        background: rgba(255, 255, 255, 0.8);
        border: 2px solid #D5E3CD;
        border-radius: 22px;
        padding: 24px;
        text-align: center;
        margin-bottom: 20px;
    }}

    .welcome-card p {{
        font-size: {body_size}px !important;
        line-height: 1.8 !important;
    }}

    /* 작은 안내 글씨도 읽기 쉽게 */
    [data-testid="stCaptionContainer"] {{
        font-size: {max(body_size - 4, 18)}px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 6. 공통 기능
# ==========================================
def go_to(page):
    st.session_state.page = page
    st.rerun()


def back_home():
    st.session_state.page = "home"
    st.rerun()


def font_button():
    st.markdown(
        f"**현재 글씨 크기: {font_name}**"
    )

    if st.button(
        "🔎 글씨 크기 바꾸기",
        use_container_width=True,
        key="change_font"
    ):
        st.session_state.font_level = (
            st.session_state.font_level + 1
        ) % len(FONT_SIZES)

        st.rerun()


def home_button():
    st.divider()

    if st.button(
        "🏠 메인 화면으로 돌아가기",
        use_container_width=True,
        key=f"home_{st.session_state.page}"
    ):
        back_home()


# ==========================================
# 7. 공통 상단 제목
# ==========================================
st.title("☘️ 천천히 키오스크")

st.markdown(
    "<p style='text-align:center;'>"
    "어르신을 위한 쉽고 편안한 키오스크 연습"
    "</p>",
    unsafe_allow_html=True
)

# ==========================================
# 8. 메인 화면
# ==========================================
if st.session_state.page == "home":

    st.markdown(
        """
        <div class="welcome-card">
            <div style="font-size:55px;">🌷</div>
            <h2>안녕하세요!</h2>
            <p>
                키오스크 사용이 어려우신가요?<br>
                걱정하지 마세요.<br>
                <strong>천천히 하나씩 함께 배워봐요!</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    font_button()

    st.divider()

    st.header("무엇을 도와드릴까요?")

    st.write("원하는 메뉴를 눌러 주세요.")

    if st.button(
        "☕ 키오스크 주문 연습하기",
        use_container_width=True
    ):
        go_to("order")

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

    st.success(
        "🌼 실수해도 괜찮습니다!\n\n"
        "화면을 천천히 읽고 따라 해 보세요."
    )

    st.markdown(
        """
        <div class="welcome-card">
            <p><strong  
