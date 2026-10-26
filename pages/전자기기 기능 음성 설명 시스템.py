
import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(
    page_title="쉬운 전자생활",
    page_icon="🔊",
    layout="centered",
)

# 화면 디자인
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F8FC;
    }
    h1, h2, h3, p, label {
        color: #17324D;
    }
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: 800;
        color: #174A7E;
        padding: 12px 0;
    }
    .intro {
        text-align: center;
        font-size: 20px;
        line-height: 1.8;
        color: #334155;
    }
    div.stButton > button {
        width: 100%;
        min-height: 58px;
        font-size: 21px;
        font-weight: bold;
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 초보자도 이해할 수 있는 단계별 안내
GUIDES = {
    "스마트폰": {
        "전화 걸기": (
            "전화 걸기",
            [
                "스마트폰 화면에서 초록색 전화기 모양을 찾아 누르세요.",
                "숫자 버튼을 눌러 전화할 번호를 입력하세요.",
                "초록색 통화 버튼을 누르면 전화가 연결됩니다.",
                "통화를 마칠 때는 빨간색 종료 버튼을 누르세요.",
            ],
        ),
        "글자 크게 보기": (
            "글자 크게 보기",
            [
                "스마트폰에서 설정 앱을 찾아 누르세요.",
                "화면 또는 디스플레이 메뉴를 찾아 누르세요.",
                "글자 크기 또는 글꼴 크기 메뉴를 선택하세요.",
                "조절 막대를 움직여 글자를 크게 만드세요.",
                "기종에 따라 메뉴 이름과 위치가 다를 수 있습니다.",
            ],
        ),
        "사진 찍기": (
            "사진 찍기",
            [
                "카메라 모양의 앱을 찾아 누르세요.",
                "찍고 싶은 대상을 화면 가운데에 맞추세요.",
                "화면에 있는 동그란 촬영 버튼을 누르세요.",
                "사진 앱이나 갤러리에서 찍은 사진을 확인하세요.",
            ],
        ),
        "와이파이 연결": (
            "와이파이 연결",
            [
                "설정 앱을 여세요.",
                "와이파이 또는 Wi-Fi 메뉴를 누르세요.",
                "주변에 표시되는 와이파이 이름을 선택하세요.",
                "비밀번호를 물어보면 안내받은 비밀번호를 입력하세요.",
                "연결됨이라고 표시되면 사용할 수 있습니다.",
            ],
        ),
    },
    "카카오톡": {
        "메시지 보내기": (
            "카카오톡 메시지 보내기",
            [
                "카카오톡 앱을 여세요.",
                "대화 목록에서 메시지를 보낼 사람을 선택하세요.",
                "화면 아래쪽의 입력 칸을 누르세요.",
                "전하고 싶은 말을 입력하세요.",
                "전송 버튼을 누르면 메시지가 전달됩니다.",
            ],
        ),
        "사진 보내기": (
            "카카오톡 사진 보내기",
            [
                "카카오톡에서 사진을 보낼 사람과의 대화를 여세요.",
                "입력 칸 옆의 더하기 버튼을 누르세요.",
                "앨범 또는 사진 메뉴를 선택하세요.",
                "보낼 사진을 선택하세요.",
                "전송 버튼을 누르면 사진이 전달됩니다.",
            ],
        ),
        "영상 통화": (
            "카카오톡 영상 통화",
            [
                "카카오톡에서 통화할 사람의 대화를 여세요.",
                "화면 위쪽의 전화기 모양 또는 통화 메뉴를 누르세요.",
                "영상 통화 메뉴를 선택하세요.",
                "상대방이 받으면 화면을 보며 이야기할 수 있습니다.",
                "통화가 끝나면 종료 버튼을 누르세요.",
            ],
        ),
    },
    "인터넷": {
        "인터넷 검색하기": (
            "인터넷 검색하기",
            [
                "인터넷이나 크롬 앱을 여세요.",
                "검색창을 누르세요.",
                "찾고 싶은 내용을 입력하세요. 예를 들어 날씨라고 입력할 수 있습니다.",
                "검색 또는 돋보기 버튼을 누르세요.",
                "화면에 나온 결과 중 원하는 내용을 선택하세요.",
            ],
        ),
        "유튜브 동영상 보기": (
            "유튜브 동영상 보기",
            [
                "유튜브 앱을 여세요.",
                "화면 위쪽의 돋보기 모양을 누르세요.",
                "보고 싶은 영상의 제목을 입력하세요.",
                "검색 결과에서 원하는 영상을 누르세요.",
                "영상이 재생되면 소리와 화면을 즐기시면 됩니다.",
            ],
        ),
    },
    "생활 속 전자기기": {
        "TV 리모컨 사용하기": (
            "TV 리모컨 사용하기",
            [
                "리모컨을 TV 쪽으로 향하게 하세요.",
                "전원 버튼을 눌러 TV를 켜세요.",
                "채널 위아래 버튼으로 원하는 방송을 찾으세요.",
                "음량 위아래 버튼으로 소리를 조절하세요.",
                "버튼 이름과 위치는 리모컨 종류에 따라 다를 수 있습니다.",
            ],
        ),
        "무선 이어폰 연결하기": (
            "무선 이어폰 연결하기",
            [
                "무선 이어폰을 충전 케이스에서 꺼내세요.",
                "스마트폰에서 설정 앱을 여세요.",
                "블루투스 메뉴를 찾아 켜세요.",
                "목록에서 이어폰 이름을 선택하세요.",
                "연결되었다는 표시가 나오면 사용할 수 있습니다.",
            ],
        ),
        "휴대전화 충전하기": (
            "휴대전화 충전하기",
            [
                "휴대전화에 맞는 충전기를 준비하세요.",
                "충전 케이블을 휴대전화 충전 단자에 연결하세요.",
                "충전기의 플러그를 안전한 콘센트에 연결하세요.",
                "화면에 충전 표시가 나타나는지 확인하세요.",
                "충전 중 기기나 충전기가 비정상적으로 뜨거우면 사용을 중단하세요.",
            ],
        ),
    },
}


def make_explanation(title, steps):
    """음성으로 읽기 편한 설명문을 만듭니다."""
    intro = f"안녕하세요. 쉬운 전자생활입니다. 오늘은 {title} 방법을 알려드리겠습니다."
    body = " ".join(
        f"{index}단계. {step}"
        for index, step in enumerate(steps, start=1)
    )
    ending = "천천히 한 단계씩 따라 해 보세요. 잘되지 않아도 괜찮습니다."
    return f"{intro} {body} {ending}"


def make_audio(text, slow=False):
    """한국어 음성을 생성합니다."""
    audio_buffer = BytesIO()
    tts = gTTS(text=text, lang="ko", slow=slow)
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer.getvalue()


# 제목
st.markdown(
    '<div class="main-title">🔊 쉬운 전자생활</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="intro">'
    '어려운 전자기기 사용법을<br>'
    '<b>쉽고 친절한 목소리</b>로 알려드려요.<br>'
    '원하는 기능을 선택해 보세요!'
    '</div>',
    unsafe_allow_html=True,
)

st.divider()

# 기능 선택
st.subheader("1. 어떤 기능을 배우고 싶으세요?")

category = st.selectbox(
    "전자기기 종류를 선택하세요",
    list(GUIDES.keys()),
)

function_name = st.selectbox(
    "배우고 싶은 기능을 선택하세요",
    list(GUIDES[category].keys()),
)

title, steps = GUIDES[category][function_name]
explanation = make_explanation(title, steps)

slow_mode = st.checkbox("🐢 천천히 말하기", value=False)

st.divider()

# 설명 시작 버튼
st.subheader("2. 설명을 들어 보세요")

if st.button("🔊 설명 듣기", type="primary", use_container_width=True):
    with st.spinner("음성을 준비하고 있어요. 잠시만 기다려 주세요."):
        try:
            audio = make_audio(explanation, slow=slow_mode)
            st.session_state["audio"] = audio
            st.session_state["audio_title"] = title
            st.session_state["audio_error"] = None
        except Exception:
            st.session_state["audio"] = None
            st.session_state["audio_error"] = (
                "음성을 만들지 못했어요. 인터넷 연결을 확인한 뒤 "
                "다시 눌러 주세요. 아래 글 설명은 그대로 이용할 수 있어요."
            )

if st.session_state.get("audio_title") == title:
    if st.session_state.get("audio"):
        st.success("음성이 준비되었습니다. 아래 재생 버튼을 누르세요.")
        st.audio(st.session_state["audio"], format="audio/mp3")

if st.session_state.get("audio_error"):
    st.warning(st.session_state["audio_error"])

st.divider()

# 글로 보는 설명
st.subheader(f"📖 {title}")
st.write("아래 순서대로 천천히 따라 해 보세요.")

for index, step in enumerate(steps, start=1):
    st.markdown(
        f"""
        <div style="
            background-color: white;
            border: 2px solid #D6E5F5;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 10px;
            font-size: 20px;
            color: #17324D;
            line-height: 1.7;
        ">
        <b>{index}단계</b><br>{step}
        </div>
        """,
        unsafe_allow_html=True,
    )

st.info(
    "전자기기마다 화면과 버튼 위치가 다를 수 있어요. "
    "화면이 다르면 가족이나 주변 사람에게 도움을 요청해도 괜찮습니다."
)

st.caption("쉬운 전자생활 | 누구나 쉽게 배우는 디지털 안내")

