
import re
import streamlit as st

ag    .
  setst_page_config(
e_title="한 번에 도움 요청",
    page_icon="🆘",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# 어르신을 위한 큰 글씨와 큰 버튼
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F4F8FC;
    }
    .block-container {
        max-width: 760px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, p, label, li {
        color: #172B4D;
    }
    h1 {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
    }
    .intro {
        background: #FFFFFF;
        padding: 22px;
        border-radius: 18px;
        border: 2px solid #D5E5F5;
        font-size: 1.2rem;
        line-height: 1.8;
        margin-bottom: 18px;
    }
    .help-card {
        background: #FFFFFF;
        padding: 18px;
        border-radius: 15px;
        border-left: 6px solid #2471A3;
        font-size: 1.12rem;
        line-height: 1.8;
        margin: 10px 0;
    }
    div.stButton > button,
    div.stLinkButton > a {
        min-height: 64px;
        width: 100%;
        font-size: 1.25rem !important;
        font-weight: 800 !important;
        border-radius: 14px !important;
    }
    div.stButton > button[kind="primary"] {
        background-color: #C62828;
        color: white;
        border: 2px solid #A71919;
    }
    input, textarea {
        font-size: 1.1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 세션 상태 초기화
# 연락처는 현재 세션에서만 유지됨
# -----------------------------
if "helper_name" not in st.session_state:
    st.session_state.helper_name = ""
if "helper_phone" not in st.session_state:
    st.session_state.helper_phone = ""
if "show_call" not in st.session_state:
    st.session_state.show_call = False

def normalize_phone(raw_phone):
    """전화번호에서 숫자와 맨 앞의 +만 허용해 정리."""
    value = raw_phone.strip()
    if not value:
        return ""

    # 국내 번호 입력과 국제번호 형식 지원
    if value.startswith("+"):
        digits = re.sub(r"\D", "", value[1:])
        return "+" + digits if digits else ""

    return re.sub(r"\D", "", value)

def is_valid_phone(phone):
    """기본적인 전화번호 형식 확인. 실제 연결 가능 여부는 확인하지 못함."""
    if phone.startswith("+"):
        digits = phone[1:]
        return digits.isdigit() and 8 <= len(digits) <= 15

    return phone.isdigit() and 9 <= len(phone) <= 11

# -----------------------------
# 첫 화면
# -----------------------------
st.title("🆘 한 번에 도움 요청")
st.markdown(
    """
    <div class="intro">
    <b>사용하기 어려우신가요?</b><br>
    괜찮습니다. 천천히 따라 해 보세요.<br>
    가족에게 전화하거나 쉬운 사용 방법을 확인할 수 있습니다.
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("📞 1. 도움을 줄 사람 등록하기")
st.write("가족이나 믿을 수 있는 사람의 이름과 전화번호를 입력하세요.")

with st.form("contact_form"):
    name_input = st.text_input(
        "도움을 줄 사람 이름",
        value=st.session_state.helper_name,
        placeholder="예: 딸, 아들, 보호자",
        max_chars=30,
    )
    phone_input = st.text_input(
        "전화번호",
        value=st.session_state.helper_phone,
        placeholder="예: 010-1234-5678",
        max_chars=20,
    )
    save_contact = st.form_submit_button(
        "연락처 저장하기",
        use_container_width=True,
    )

if save_contact:
    clean_name = name_input.strip()
    clean_phone = normalize_phone(phone_input)

    if not clean_name:
        st.error("도움을 줄 사람의 이름을 입력해 주세요.")
    elif not is_valid_phone(clean_phone):
        st.error("전화번호를 다시 확인해 주세요. 예: 010-1234-5678")
    else:
        st.session_state.helper_name = clean_name
        st.session_state.helper_phone = clean_phone
        st.session_state.show_call = False
        st.success(
            f"{clean_name}님의 연락처를 현재 화면에 저장했습니다."
        )
        st.info(
            "이 연락처는 현재 세션에만 저장됩니다. "
            "앱을 다시 열면 사라질 수 있으니 확인해 주세요."
        )

st.divider()

# -----------------------------
# 원터치 도움 요청
# -----------------------------
st.subheader("🆘 2. 도움이 필요할 때")

st.write(
    "기기를 사용하다 어려움이 생기면 아래 버튼을 누르세요."
)

if st.button(
    "도와주세요! 가족에게 연락하기",
    type="primary",
    use_container_width=True,
):
    if not st.session_state.helper_phone:
        st.session_state.show_call = False
        st.warning(
            "먼저 위에서 가족이나 도움을 줄 사람의 "
            "이름과 전화번호를 등록해 주세요."
        )
    else:
        st.session_state.show_call = True

if st.session_state.show_call and st.session_state.helper_phone:
    phone = st.session_state.helper_phone
    name = st.session_state.helper_name or "도움을 줄 사람"

    st.markdown(
        f"""
        <div class="help-card">
        <b>{name}님에게 연락할 준비가 되었습니다.</b><br>
        아래 전화 버튼을 눌러 통화를 시작하세요.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 전화 앱 실행을 요청하는 링크
    st.link_button(
        f"📞 {name}님에게 전화하기",
        f"tel:{phone}",
        use_container_width=True,
    )

    st.caption(
        "기기와 브라우저에 따라 전화 앱이 열리지 않을 수 있습니다. "
        "통화가 실제로 연결되었는지는 직접 확인해 주세요."
    )

st.divider()

# -----------------------------
# 상황별 쉬운 도움말
# -----------------------------
st.subheader("💡 3. 어떤 점이 어려우신가요?")

problem = st.selectbox(
    "어려운 상황을 선택하세요.",
    [
        "상황을 선택해 주세요",
        "키오스크에서 주문하기",
        "스마트폰 글자 입력하기",
        "화면의 작은 글씨 읽기",
        "인터넷이나 앱 열기",
        "결제 화면 사용하기",
    ],
)

tips = {
    "키오스크에서 주문하기": [
        "화면에서 먹고 싶은 메뉴를 천천히 찾으세요.",
        "메뉴를 선택한 뒤 화면의 안내를 확인하세요.",
        "결제 방법이 어렵다면 직원에게 도움을 요청하세요.",
    ],
    "스마트폰 글자 입력하기": [
        "글자를 입력할 칸을 한 번 눌러 보세요.",
        "화면 아래에 글자판이 나타나는지 확인하세요.",
        "어려우면 가족에게 화면을 보여 주고 도움을 요청하세요.",
    ],
    "화면의 작은 글씨 읽기": [
        "스마트폰 설정에서 글자 크기를 크게 바꿀 수 있습니다.",
        "화면을 확대하는 기능을 사용할 수도 있습니다.",
        "설정을 찾기 어렵다면 가족에게 도움을 요청하세요.",
    ],
    "인터넷이나 앱 열기": [
        "화면에 있는 앱 그림을 한 번 눌러 보세요.",
        "화면이 바뀔 때까지 잠시 기다리세요.",
        "모르는 안내가 나오면 서두르지 말고 가족에게 물어보세요.",
    ],
    "결제 화면 사용하기": [
        "금액과 상품이 맞는지 먼저 확인하세요.",
        "비밀번호나 인증번호를 다른 사람에게 알려 주지 마세요.",
        "결제가 어렵거나 의심스러운 화면이 나오면 진행을 멈추고 직원이나 가족에게 확인하세요.",
    ],
}

if problem == "상황을 선택해 주세요":
    st.info("위 목록에서 어려운 상황을 선택해 주세요.")
else:
    for i, tip in enumerate(tips[problem], start=1):
        st.markdown(
            f'<div class="help-card"><b>{i}.</b> {tip}</div>',
            unsafe_allow_html=True,
        )

    if st.button(
        "이 문제로 가족에게 도움 요청하기",
        use_container_width=True,
    ):
        if st.session_state.helper_phone:
            st.session_state.show_call = True
            st.success(
                "위의 빨간 도움 요청 버튼 아래에 있는 "
                "전화 연결 버튼을 확인해 주세요."
            )
        else:
            st.warning(
                "먼저 가족의 연락처를 등록해 주세요."
            )

st.divider()

st.markdown(
    """
    <div class="intro">
    <b>안전하게 사용하기</b><br>
    비밀번호, 인증번호, 은행 정보는 다른 사람에게 알려 주지 마세요.<br>
    위급한 상황에서는 웹 앱에만 의존하지 말고
    주변 사람이나 긴급 신고 서비스를 이용하세요.
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "한 번에 도움 요청 | 어르신의 쉬운 디지털 생활을 위한 앱"
)

