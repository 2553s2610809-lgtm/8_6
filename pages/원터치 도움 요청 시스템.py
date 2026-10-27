
import re
from urllib.parse import quote

import streamlit as st


st.set_page_config(
    page_title="도와줘요 | 원터치 도움 요청",
    page_icon="🆘",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- 디자인 ----------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F4F8FC;
    }
    .block-container {
        max-width: 720px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, p, label {
        color: #18324A;
    }
    .hero {
        background: #FFFFFF;
        border: 2px solid #D9E7F5;
        border-radius: 24px;
        padding: 24px 18px;
        text-align: center;
        margin-bottom: 18px;
    }
    .hero-icon {
        font-size: 64px;
        line-height: 1.3;
    }
    .hero-title {
        font-size: 30px;
        font-weight: 800;
        color: #18324A;
        margin: 8px 0;
    }
    .hero-description {
        font-size: 19px;
        line-height: 1.7;
        color: #34495E;
    }
    .help-button button {
        width: 100%;
        min-height: 100px;
        font-size: 30px !important;
        font-weight: 800 !important;
        border-radius: 20px !important;
        background: #C62828 !important;
        color: white !important;
        border: 3px solid #A61F1F !important;
    }
    .stButton button {
        min-height: 52px;
        font-size: 18px;
        font-weight: 700;
        border-radius: 12px;
    }
    .contact-link {
        display: block;
        text-align: center;
        text-decoration: none !important;
        font-size: 23px;
        font-weight: 800;
        padding: 18px 12px;
        margin: 12px 0;
        border-radius: 15px;
        color: white !important;
    }
    .call-link {
        background: #167347;
    }
    .sms-link {
        background: #175DA8;
    }
    .info-card {
        background: #FFFFFF;
        border: 1px solid #D9E7F5;
        border-radius: 16px;
        padding: 16px;
        margin: 12px 0;
        font-size: 18px;
        line-height: 1.7;
    }
    div[data-testid="stWidgetLabel"] p {
        font-size: 18px;
        font-weight: 700;
    }
    @media (max-width: 480px) {
        .hero-title { font-size: 26px; }
        .hero-description { font-size: 17px; }
        .help-button button { font-size: 25px !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- 기본 설정 ----------
if "guardian_name" not in st.session_state:
    st.session_state.guardian_name = ""

if "guardian_phone" not in st.session_state:
    st.session_state.guardian_phone = ""

if "help_requested" not in st.session_state:
    st.session_state.help_requested = False

if "help_message" not in st.session_state:
    st.session_state.help_message = ""

if "large_text" not in st.session_state:
    st.session_state.large_text = True


# ---------- 제목 ----------
st.markdown(
    """
    <div class="hero">
        <div class="hero-icon">🤝</div>
        <div class="hero-title">도와줘요</div>
        <div class="hero-description">
            기기 사용이 어려우신가요?<br>
            괜찮아요. 버튼을 눌러 도움을 요청하세요.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- 글씨 크기 ----------
st.session_state.large_text = st.toggle(
    "큰 글씨로 보기",
    value=st.session_state.large_text,
)

if st.session_state.large_text:
    st.markdown(
        """
        <style>
        p, li, label, .stMarkdown {
            line-height: 1.7;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---------- 상황 선택 ----------
st.subheader("어떤 점이 어려우신가요?")

situation = st.selectbox(
    "어려운 상황을 선택하세요",
    [
        "상황을 선택하지 않았어요",
        "키오스크 사용이 어려워요",
        "스마트폰 사용이 어려워요",
        "무인민원발급기 사용이 어려워요",
        "결제나 주문 방법을 모르겠어요",
        "기타 도움이 필요해요",
    ],
    label_visibility="collapsed",
)

message_map = {
    "상황을 선택하지 않았어요":
        "기기 사용에 어려움이 있어요. 도와주세요.",
    "키오스크 사용이 어려워요":
        "키오스크 사용 방법을 모르겠어요. 도와주세요.",
    "스마트폰 사용이 어려워요":
        "스마트폰 사용 중 어려움이 생겼어요. 도와주세요.",
    "무인민원발급기 사용이 어려워요":
        "무인민원발급기 사용 방법을 모르겠어요. 도와주세요.",
    "결제나 주문 방법을 모르겠어요":
        "결제 또는 주문하는 방법을 모르겠어요. 도와주세요.",
    "기타 도움이 필요해요":
        "기기 사용 중 문제가 생겼어요. 도와주세요.",
}

st.markdown(
    f"""
    <div class="info-card">
        <strong>도움 요청 내용</strong><br>
        {message_map[situation]}
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- 원터치 도움 요청 ----------
st.markdown('<div class="help-button">', unsafe_allow_html=True)

if st.button(
    "🆘  도와주세요!",
    use_container_width=True,
    help="누르면 보호자에게 연락할 수 있는 버튼이 나타납니다.",
):
    st.session_state.help_requested = True
    st.session_state.help_message = message_map[situation]

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.help_requested:
    st.success("도움 요청 준비가 되었어요. 아래 버튼으로 연락하세요.")

    st.info(
        "전화 또는 문자 버튼을 누르면 기기의 연락 기능이 열립니다. "
        "연락을 완료하려면 열린 화면에서 직접 진행해 주세요."
    )

# ---------- 보호자 연락처 설정 ----------
st.divider()
st.subheader("📞 가족 또는 도움 줄 사람 등록")
st.caption("보호자 정보를 입력한 뒤 저장 버튼을 눌러주세요.")

with st.form("guardian_form"):
    guardian_name = st.text_input(
        "보호자 이름",
        value=st.session_state.guardian_name,
        placeholder="예: 딸, 아들, 보호자",
        max_chars=30,
    )

    guardian_phone = st.text_input(
        "보호자 전화번호",
        value=st.session_state.guardian_phone,
        placeholder="예: 010-1234-5678",
        max_chars=20,
    )

    saved = st.form_submit_button(
        "연락처 저장",
        use_container_width=True,
    )

    if saved:
        clean_phone = re.sub(r"[\s\-()]", "", guardian_phone.strip())

        if not guardian_name.strip():
            st.error("보호자 이름을 입력해 주세요.")
        elif not re.fullmatch(r"\+?[0-9]{8,15}", clean_phone):
            st.error("전화번호를 확인해 주세요. 숫자와 국가번호를 확인해 주세요.")
        else:
            st.session_state.guardian_name = guardian_name.strip()
            st.session_state.guardian_phone = clean_phone
            st.success("연락처가 저장되었어요.")

# ---------- 전화 및 문자 ----------
if st.session_state.guardian_phone:
    st.subheader("연락하기")

    st.markdown(
        f"**등록된 도움 제공자:** {st.session_state.guardian_name}"
    )

    phone = st.session_state.guardian_phone
    sms_message = st.session_state.get(
        "help_message",
        message_map[situation],
    )

    call_url = f"tel:{phone}"
    sms_url = f"sms:{phone}?body={quote(sms_message)}"

    st.markdown(
        f"""
        <a class="contact-link call-link" href="{call_url}">
            📞 전화로 도움 요청하기
        </a>
        <a class="contact-link sms-link" href="{sms_url}">
            💬 문자로 도움 요청하기
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "기기와 브라우저에 따라 전화·문자 앱이 열리지 않을 수 있어요. "
        "이 경우 아래 번호를 확인해 직접 연락해 주세요."
    )
    st.code(phone, language=None)

    if st.button("도움 요청 화면 닫기", use_container_width=True):
        st.session_state.help_requested = False
        st.session_state.help_message = ""
        st.rerun()
else:
    st.info("먼저 보호자 연락처를 등록하면 전화와 문자 버튼을 사용할 수 있어요.")

# ---------- 이용 안내 ----------
st.divider()
st.subheader("📘 사용 방법")

st.markdown(
    """
    <div class="info-card">
        <strong>1.</strong> 가족이나 도움을 줄 사람의 연락처를 등록하세요.<br>
        <strong>2.</strong> 어려운 상황을 선택하세요.<br>
        <strong>3.</strong> 빨간색 '도와주세요!' 버튼을 누르세요.<br>
        <strong>4.</strong> 전화 또는 문자 버튼을 눌러 연락하세요.
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "안내: 이 앱은 연락을 연결하기 위한 도구입니다. "
    "버튼을 누르는 것만으로 보호자에게 자동 연락되지는 않습니다. "
    "긴급한 상황에서는 112 또는 119에 직접 연락하세요."
)

        
