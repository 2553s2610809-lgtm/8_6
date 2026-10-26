import streamlit as st
from pathlib import Path
from urllib.parse import urlparse

# --------------------------------------------------
# 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="어르신 키오스크 결제 도우미",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }

    .stApp {
        background: #F5F8FC;
        color: #14263D;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    .hero {
        background: #103A66;
        color: white;
        padding: 28px 30px;
        border-radius: 22px;
        margin-bottom: 20px;
    }

    .hero h1 {
        color: white;
        font-size: clamp(30px, 4vw, 48px);
        font-weight: 900;
        margin: 0 0 12px 0;
    }

    .hero p {
        color: #F1F6FF;
        font-size: clamp(18px, 2vw, 25px);
        margin: 0;
        line-height: 1.6;
    }

    .section-title {
        font-size: clamp(25px, 3vw, 34px);
        font-weight: 900;
        margin: 12px 0 16px 0;
        color: #103A66;
    }

    .step-card {
        background: white;
        border: 2px solid #D9E5F2;
        border-radius: 18px;
        padding: 22px 20px;
        min-height: 165px;
        margin-bottom: 12px;
    }

    .step-number {
        color: #1767B2;
        font-size: 18px;
        font-weight: 900;
    }

    .step-heading {
        font-size: clamp(23px, 2.5vw, 30px);
        font-weight: 900;
        margin: 8px 0;
        color: #14263D;
    }

    .step-description {
        font-size: clamp(17px, 1.8vw, 21px);
        line-height: 1.65;
        color: #34465D;
    }

    .notice {
        background: #FFF3D6;
        border-left: 8px solid #E6A000;
        border-radius: 12px;
        padding: 18px 20px;
        font-size: clamp(18px, 2vw, 23px);
        line-height: 1.65;
        margin: 16px 0;
        color: #513B00;
    }

    .success-panel {
        background: #E5F7ED;
        border: 2px solid #9DD9B5;
        border-radius: 16px;
        padding: 20px;
        font-size: clamp(20px, 2.3vw, 27px);
        font-weight: 800;
        color: #155B35;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        color: #42546A;
        font-size: 17px;
        padding: 20px 8px 5px 8px;
    }

    div.stButton > button {
        min-height: 60px;
        width: 100%;
        font-size: 21px;
        font-weight: 800;
        border-radius: 14px;
        border: 2px solid #1767B2;
    }

    div[data-testid="stRadio"] label {
        font-size: 20px;
        font-weight: 700;
    }

    [data-testid="stVideo"] {
        border-radius: 16px;
        overflow: hidden;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 0.8rem;
        }

        .hero {
            padding: 22px 18px;
        }

        .step-card {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# 결제 안내 자료
# --------------------------------------------------
PAYMENT_GUIDES = {
    "💳 카드 결제": [
        (
            "1단계",
            "결제 방법 선택",
            "화면에서 '카드 결제' 또는 '신용카드'를 찾아 눌러 주세요.",
        ),
        (
            "2단계",
            "카드 넣기 또는 대기",
            "카드 투입구가 있으면 안내 방향에 맞춰 넣어 주세요. "
            "카드를 대는 방식이라면 표시된 곳에 카드를 대 주세요.",
        ),
        (
            "3단계",
            "결제 완료 확인",
            "승인 안내가 나올 때까지 잠시 기다려 주세요. "
            "완료 화면이나 영수증을 확인하세요.",
        ),
    ],
    "📱 간편결제": [
        (
            "1단계",
            "간편결제 선택",
            "화면에서 사용할 수 있는 간편결제 방법을 선택해 주세요.",
        ),
        (
            "2단계",
            "화면 안내 따라 하기",
            "휴대전화나 인증 화면이 나타나면 안내에 따라 진행해 주세요.",
        ),
        (
            "3단계",
            "결제 완료 확인",
            "완료 안내가 나타날 때까지 기다려 주세요. "
            "화면이 다르거나 어렵다면 직원에게 도움을 요청하세요.",
        ),
    ],
    "❓ 결제가 안 될 때": [
        (
            "1단계",
            "잠시 기다리기",
            "화면에 처리 중이라는 안내가 있다면 잠시 기다려 주세요.",
        ),
        (
            "2단계",
            "카드와 화면 확인",
            "카드를 너무 일찍 빼지 말고, 화면에 나온 안내를 확인하세요.",
        ),
        (
            "3단계",
            "직원에게 도움 요청",
            "결제가 되었는지 확실하지 않다면 다시 결제하지 말고 "
            "직원에게 먼저 확인해 주세요.",
        ),
    ],
}


def valid_video_url(value: str) -> bool:
    """HTTP 또는 HTTPS 영상 주소인지 간단히 확인합니다."""
    try:
        parsed = urlparse(value.strip())
        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
        )
    except (ValueError, AttributeError):
        return False


def show_step_card(number: str, heading: str, description: str):
    """큰 글씨의 단계별 안내 카드를 표시합니다."""
    st.markdown(
        f"""
        <div class="step-card">
            <div class="step-number">{number}</div>
            <div class="step-heading">{heading}</div>
            <div class="step-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# 관리자 설정: 영상 주소
# --------------------------------------------------
with st.sidebar:
    st.header("⚙️ 영상 설정")
    st.caption(
        "관리자가 교육 영상을 등록하는 곳입니다. "
        "설정을 변경하지 않아도 기본 안내 화면을 사용할 수 있습니다."
    )

    video_url = st.text_input(
        "결제 안내 영상 URL",
        value="",
        placeholder="https://example.com/payment-guide.mp4",
        help=(
            "직접 재생할 수 있는 MP4 주소나 지원되는 영상 URL을 입력하세요. "
            "일반 웹페이지 주소는 재생되지 않을 수 있습니다."
        ),
    ).strip()

    local_video = Path("payment_guide.mp4")
    use_local_video = local_video.is_file()

    if use_local_video:
        st.success("저장소의 payment_guide.mp4 파일을 찾았습니다.")

    st.caption(
        "권장: 매장 키오스크와 일치하는 영상을 사용하세요. "
        "영상은 반복 재생 및 음소거 자동 재생을 시도합니다."
    )

# --------------------------------------------------
# 상단 안내
# --------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>💳 키오스크 결제, 천천히 따라 해 보세요!</h1>
        <p>
            서두르지 않으셔도 괜찮습니다.<br>
            화면을 보고 한 단계씩 천천히 따라 해 주세요.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# 결제 방식 선택
# --------------------------------------------------
st.markdown(
    '<div class="section-title">어떤 도움이 필요하신가요?</div>',
    unsafe_allow_html=True,
)

selected_guide = st.radio(
    "안내 종류",
    options=list(PAYMENT_GUIDES.keys()),
    horizontal=True,
    label_visibility="collapsed",
)

# --------------------------------------------------
# 큰 화면 영상
# --------------------------------------------------
st.markdown(
    '<div class="section-title">🎬 결제 방법 안내 영상</div>',
    unsafe_allow_html=True,
)

if video_url and not valid_video_url(video_url):
    st.warning(
        "영상 주소를 확인해 주세요. http:// 또는 https://로 "
        "시작하는 올바른 주소를 입력해야 합니다."
    )

video_source = None

if video_url and valid_video_url(video_url):
    video_source = video_url
elif use_local_video:
    video_source = str(local_video)

if video_source:
    try:
        st.video(
            video_source,
            loop=True,
            autoplay=True,
            muted=True,
            width="stretch",
        )
        st.caption(
            "영상이 자동 재생되지 않으면 재생 버튼을 눌러 주세요. "
            "브라우저 설정에 따라 자동 재생이 제한될 수 있습니다."
        )
    except Exception:
        st.warning(
            "영상을 불러오지 못했습니다. 주소가 올바른지, "
            "영상이 공개되어 있는지 확인해 주세요."
        )
        st.info("아래의 큰 글씨 단계별 안내를 이용하실 수 있습니다.")
else:
    st.markdown(
        """
        <div class="success-panel">
            👋 반갑습니다!<br><br>
            ① 결제 방법을 선택하세요.<br>
            ② 화면의 안내에 따라 카드를 넣거나 대세요.<br>
            ③ 결제가 완료되었는지 확인하세요.<br><br>
            아래 안내를 보면서 천천히 따라 해 보세요.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "반복 재생할 영상을 준비했다면 왼쪽 위 메뉴의 "
        "'영상 설정'에서 주소를 입력하거나 "
        "저장소에 payment_guide.mp4 파일을 추가하세요."
    )

# --------------------------------------------------
# 단계별 학습
# --------------------------------------------------
st.markdown(
    '<div class="section-title">👣 순서대로 따라 하기</div>',
    unsafe_allow_html=True,
)

steps = PAYMENT_GUIDES[selected_guide]

for number, heading, description in steps:
    show_step_card(number, heading, description)

# --------------------------------------------------
# 도움 요청 안내
# --------------------------------------------------
st.markdown(
    """
    <div class="notice">
        <strong>😊 잘 모르셔도 괜찮습니다!</strong><br>
        화면이 다르거나 결제가 어려우면 가까운 직원에게
        "키오스크 결제를 도와주세요"라고 말씀해 주세요.<br>
        결제 여부가 확실하지 않을 때는 다시 결제하기 전에
        직원에게 먼저 확인해 주세요.
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# 안내 다시 보기 버튼
# --------------------------------------------------
if st.button("🔄 처음 안내부터 다시 보기", type="primary"):
    st.session_state["reset_notice"] = True
    st.rerun()

if st.session_state.get("reset_notice", False):
    st.success(
        "처음 안내 화면입니다. 위에서 결제 방법을 선택하고 "
        "천천히 다시 확인해 보세요."
    )
    st.session_state["reset_notice"] = False

st.markdown(
    """
    <div class="footer">
        어르신의 디지털 생활을 응원합니다 💙<br>
        이 화면은 결제 방법을 안내하는 교육용 앱이며,
        실제 결제를 처리하지 않습니다.
    </div>
    """,
    unsafe_allow_html=True,
)

    
