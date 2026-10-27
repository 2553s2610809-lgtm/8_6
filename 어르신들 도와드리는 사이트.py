import streamlit as st

# ====================================
# 1. 기본 설정
# =====================================
st.set_page_config(
    page_title="천천히 키오스크",
    page_icon="☕",
    layout="wide"
)

# =====================================
# 2. 화면 상태 설정
# =====================================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "font_level" not in st.session_state:
    st.session_state.font_level = 2

if "cart" not in st.session_state:
    st.session_state.cart = []

if "selected_drink" not in st.session_state:
    st.session_state.selected_drink = None

if "selected_temp" not in st.session_state:
    st.session_state.selected_temp = "아이스"

if "selected_size" not in st.session_state:
    st.session_state.selected_size = "보통"

if "selected_count" not in st.session_state:
    st.session_state.selected_count = 1


# =====================================
# 3. 글씨 크기 설정
# =====================================
FONT_SIZES = {
    0: {
        "name": "작은 글씨",
        "normal": 20,
        "title": 32,
        "button": 20
    },
    1: {
        "name": "보통 글씨",
        "normal": 24,
        "title": 38,
        "button": 24
    },
    2: {
        "name": "큰 글씨",
        "normal": 28,
        "title": 44,
        "button": 28
    },
    3: {
        "name": "아주 큰 글씨",
        "normal": 32,
        "title": 50,
        "button": 32
    }
}

font_setting = FONT_SIZES[st.session_state.font_level]
font_name = font_setting["name"]
font_size = font_setting["normal"]
title_size = font_setting["title"]
button_size = font_setting["button"]


# =====================================
# 4. 화면 디자인
# =====================================
st.markdown(
    f"""
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap'
    );

    html, body, [class*="css"] {{
        font-family: 'Noto Sans KR', sans-serif;
    }}

    .stApp {{
        background: linear-gradient(
            135deg,
            #fff8e9 0%,
            #edf7e9 55%,
            #dcefe3 100%
        );
    }}

    .block-container {{
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    h1 {{
        font-size: {title_size}px !important;
        color: #24543c !important;
        font-weight: 800 !important;
    }}

    h2 {{
        font-size: {int(title_size * 0.75)}px !important;
        color: #24543c !important;
        font-weight: 800 !important;
    }}

    h3 {{
        font-size: {int(title_size * 0.60)}px !important;
        color: #315d45 !important;
    }}

    p, li, .stMarkdown {{
        font-size: {font_size}px;
        line-height: 1.7;
    }}

    div.stButton > button {{
        min-height: 76px;
        border-radius: 18px;
        font-size: {button_size}px !important;
        font-weight: 700;
        border: 2px solid #b7d4bf;
        background-color: #ffffff;
        color: #24543c;
        padding: 12px 14px;
        white-space: pre-wrap;
    }}

    div.stButton > button:hover {{
        border-color: #397c54;
        background-color: #e9f5e9;
        color: #17452d;
    }}

    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stRadio"] label {{
        font-size: {font_size}px !important;
        font-weight: 700;
    }}

    div[data-testid="stSelectbox"] div,
    div[data-testid="stNumberInput"] input {{
        font-size: {font_size}px !important;
    }}

    .welcome-box {{
        background: rgba(255, 255, 255, 0.92);
        border: 3px solid #c5dfc8;
        border-radius: 24px;
        padding: 28px;
        text-align: center;
        margin-bottom: 24px;
    }}

    .welcome-text {{
        color: #315d45;
        font-size: {font_size}px;
        line-height: 1.8;
    }}

    .drink-box {{
        background: rgba(255, 255, 255, 0.94);
        border: 2px solid #d2e5d3;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 12px;
        text-align: center;
    }}

    .drink-emoji {{
        font-size: 56px;
    }}

    .drink-name {{
        font-size: {font_size}px;
        color: #24543c;
        font-weight: 800;
    }}

    .drink-price {{
        font-size: {int(font_size * 0.85)}px;
        color: #52665a;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# =====================================
# 5. 음료 목록
# =====================================
DRINKS = {
    "아메리카노": {"emoji": "☕", "price": 2500},
    "카페라떼": {"emoji": "🥛", "price": 3500},
    "바닐라라떼": {"emoji": "🧋", "price": 4000},
    "카라멜마끼아또": {"emoji": "☕", "price": 4200},
    "카푸치노": {"emoji": "☕", "price": 3500},
    "카페모카": {"emoji": "🍫", "price": 4000},
    "초코라떼": {"emoji": "🍫", "price": 3800},
    "녹차라떼": {"emoji": "🍵", "price": 3800},
    "딸기라떼": {"emoji": "🍓", "price": 4200},
    "고구마라떼": {"emoji": "🍠", "price": 4000},
    "밀크티": {"emoji": "🧋", "price": 3800},
    "망고주스": {"emoji": "🥭", "price": 4000},
    "딸기주스": {"emoji": "🍓", "price": 4000},
    "오렌지주스": {"emoji": "🍊", "price": 3500},
    "레몬에이드": {"emoji": "🍋", "price": 3800},
    "자몽에이드": {"emoji": "🍊", "price": 4000},
    "청포도에이드": {"emoji": "🍇", "price": 4000},
    "복숭아아이스티": {"emoji": "🍑", "price": 3000},
    "유자차": {"emoji": "🍯", "price": 3500},
    "레몬차": {"emoji": "🍋", "price": 3500},
    "캐모마일": {"emoji": "🌼", "price": 3500},
    "페퍼민트": {"emoji": "🌿", "price": 3500},
    "플레인요거트": {"emoji": "🥣", "price": 4200},
    "딸기요거트": {"emoji": "🍓", "price": 4500}
}


# =====================================
# 6. 공통 기능
# =====================================
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()


def font_button():
    st.markdown(f"### 현재 글씨 크기: {font_name}")

    if st.button(
        "🔎 글씨 크기 바꾸기",
        use_container_width=True,
        key="change_font"
    ):
        st.session_state.font_level = (
            st.session_state.font_level + 1
        ) % len(FONT_SIZES)

        st.rerun()


# =====================================
# 7. 큰 글씨 메뉴
# =====================================
def top_navigation():
    st.markdown("## 📌 메뉴 선택")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button(
            "🏠\n처음 화면",
            use_container_width=True,
            key="nav_home"
        ):
            go_to("home")

    with col2:
        if st.button(
            "☕\n음료 주문",
            use_container_width=True,
            key="nav_order"
        ):
            go_to("order")

    with col3:
        if st.button(
            "📖\n사용 방법",
            use_container_width=True,
            key="nav_guide"
        ):
            go_to("guide")

    with col4:
        if st.button(
            "🙋\n도움말",
            use_container_width=True,
            key="nav_faq"
        ):
            go_to("faq")


def show_drink_card(drink_name, drink_info):
    st.markdown(
        f"""
        <div class="drink-box">
            <div class="drink-emoji">{drink_info["emoji"]}</div>
            <div class="drink-name">{drink_name}</div>
            <div class="drink-price">{drink_info["price"]:,}원</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================
# 8. 사이트 제목과 메뉴
# =====================================
st.markdown(
    "<h1 style='text-align:center;'>🌿 천천히 키오스크 ☕</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="text-align:center; color:#52665a;">
        누구나 편안하게 이용할 수 있는 키오스크 연습 사이트입니다.
    </p>
    """,
    unsafe_allow_html=True
)

top_navigation()
st.divider()


# =====================================
# 9. 처음 화면
# =====================================
if st.session_state.page == "home":

    st.markdown(
        """
        <div class="welcome-box">
            <div style="font-size:70px;">☕ 🌿 ☕</div>
            <h1>어서 오세요!</h1>
            <div class="welcome-text">
                키오스크 사용이 어려우셨나요?<br>
                걱정하지 마세요.<br>
                이곳에서 천천히 연습할 수 있어요!
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "☕ 음료 주문 연습하기",
            use_container_width=True,
            key="home_order"
        ):
            go_to("order")

    with col2:
        if st.button(
            "📖 사용 방법 알아보기",
            use_container_width=True,
            key="home_guide"
        ):
            go_to("guide")

    st.divider()
    st.subheader("🌼 편리한 기능")

    feature1, feature2, feature3 = st.columns(3)

    with feature1:
        st.markdown("### 🔠 큰 글씨")
        st.write("글씨 크기를 바꾸어 편하게 읽을 수 있어요.")

    with feature2:
        st.markdown("### ☕ 주문 연습")
        st.write("다양한 음료를 선택하며 주문 방법을 배워요.")

    with feature3:
        st.markdown("### 🐢 천천히")
        st.write("서두르지 않고 단계별로 이용할 수 있어요.")

    st.divider()
    st.subheader("🔎 글씨 크기 설정")
    font_button()


# =====================================
# 10. 음료 주문 화면
# =====================================
elif st.session_state.page == "order":

    st.header("☕ 음료 주문 연습")
    st.info("1. 원하는 음료를 선택하세요.")

    drink_names = list(DRINKS.keys())
    cols = st.columns(3)

    for index, drink_name in enumerate(drink_names):
        drink_info = DRINKS[drink_name]

        with cols[index % 3]:
            show_drink_card(drink_name, drink_info)

            if st.button(
                f"{drink_info['emoji']} {drink_name} 선택",
                use_container_width=True,
                key=f"drink_{drink_name}"
            ):
                st.session_state.selected_drink = drink_name

    st.divider()

    if st.session_state.selected_drink:
        selected = st.session_state.selected_drink
        drink_info = DRINKS[selected]

        st.success(f"선택한 음료: {selected}")

        st.subheader("2. 음료 종류를 선택하세요.")

        st.radio(
            "따뜻하게 또는 차갑게",
            ["아이스", "따뜻하게"],
            horizontal=True,
            key="selected_temp"
        )

        st.subheader("3. 음료 크기를 선택하세요.")

        st.radio(
            "음료 크기",
            ["작게", "보통", "크게"],
            horizontal=True,
            key="selected_size"
        )

        st.subheader("4. 수량을 선택하세요.")

        st.number_input(
            "몇 잔 주문하시겠어요?",
            min_value=1,
            max_value=10,
            step=1,
            key="selected_count"
        )

        count = st.session_state.selected_count
        price = drink_info["price"] * count

        st.markdown(
            f"""
            <div class="welcome-box">
                <h2>🧾 주문 확인</h2>
                <div class="welcome-text">
                    음료: {selected}<br>
                    종류: {st.session_state.selected_temp}<br>
                    크기: {st.session_state.selected_size}<br>
                    수량: {count}잔<br>
                    <h2>총 금액: {price:,}원</h2>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "🛒 주문 담기",
                use_container_width=True,
                key="add_cart"
            ):
                st.session_state.cart.append({
                    "name": selected,
                    "temp": st.session_state.selected_temp,
                    "size": st.session_state.selected_size,
                    "count": count,
                    "price": price
                })

                st.success("장바구니에 담았어요!")

        with col2:
            if st.button(
                "✅ 주문 완료 연습",
                use_container_width=True,
                key="finish_order"
            ):
                go_to("complete")

    st.divider()
    st.subheader("🛒 장바구니")

    if st.session_state.cart:
        total = 0

        for item in st.session_state.cart:
            st.write(
                f"☕ {item['name']} / "
                f"{item['temp']} / "
                f"{item['size']} / "
                f"{item['count']}잔 / "
                f"{item['price']:,}원"
            )
            total += item["price"]

        st.subheader(f"총 금액: {total:,}원")

        if st.button(
            "🗑️ 장바구니 비우기",
            use_container_width=True
        ):
            st.session_state.cart = []
            st.rerun()

    else:
        st.write("아직 담긴 음료가 없어요.")

    if st.button(
        "🏠 처음 화면으로 돌아가기",
        use_container_width=True
    ):
        go_to("home")


# =====================================
# 11. 사용 방법 화면
# =====================================
elif st.session_state.page == "guide":

    st.header("📖 키오스크 사용 방법")

    st.markdown(
        """
        <div class="welcome-box">
            <h2>1단계. 음료 선택하기</h2>
            <div class="welcome-text">
                마시고 싶은 음료를 찾아 선택하세요.
            </div>
        </div>

        <div class="welcome-box">
            <h2>2단계. 옵션 선택하기</h2>
            <div class="welcome-text">
                아이스 또는 따뜻한 음료를 고르고<br>
                원하는 크기와 수량을 선택하세요.
            </div>
        </div>

        <div class="welcome-box">
            <h2>3단계. 가격 확인하기</h2>
            <div class="welcome-text">
                선택한 음료와 총금액이 맞는지 확인하세요.
            </div>
        </div>

        <div class="welcome-box">
            <h2>4단계. 주문 완료하기</h2>
            <div class="welcome-text">
                주문 완료 버튼을 눌러 연습을 마무리하세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "💡 이 사이트는 키오스크 사용을 연습하는 사이트이며, "
        "실제 결제는 이루어지지 않습니다."
    )

    if st.button(
        "☕ 주문 연습 시작하기",
        use_container_width=True
    ):
        go_to("order")

    st.divider()
    st.subheader("🔎 글씨 크기 설정")
    font_button()


# =====================================
# 12. 도움말 화면
# =====================================
elif st.session_state.page == "faq":

    st.header("🙋 도움말")

    with st.expander("글씨가 작아서 잘 안 보여요."):
        st.write(
            "처음 화면의 '글씨 크기 바꾸기' 버튼을 눌러 "
            "더 큰 글씨로 바꿀 수 있어요."
        )

    with st.expander("음료를 잘못 선택했어요."):
        st.write(
            "다른 음료를 다시 선택하면 됩니다. "
            "주문하기 전에 선택한 음료와 가격을 확인하세요."
        )

    with st.expander("주문하면 실제로 결제가 되나요?"):
        st.write(
            "아니요. 이 사이트는 연습용이므로 "
            "실제 결제는 이루어지지 않습니다."
        )

    with st.expander("천천히 연습해도 되나요?"):
        st.write(
            "물론입니다. 서두르지 말고 원하는 만큼 "
            "반복해서 연습할 수 있습니다."
        )

    with st.expander("주문 금액은 어떻게 확인하나요?"):
        st.write(
            "음료를 선택하면 화면에 음료 가격과 "
            "총금액이 표시됩니다."
        )

    st.divider()
    st.subheader("🔎 글씨 크기 설정")
    font_button()


# =====================================
# 13. 주문 완료 화면
# =====================================
elif st.session_state.page == "complete":

    st.markdown(
        """
        <div class="welcome-box">
            <div style="font-size:80px;">🎉 ☕ 🎉</div>
            <h1>주문 연습 완료!</h1>
            <div class="welcome-text">
                키오스크 주문 연습을 잘 마쳤어요.<br>
                천천히 따라오느라 수고하셨어요!
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "이 화면은 연습용입니다. 실제 주문이나 결제는 이루어지지 않아요."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "☕ 다시 주문 연습하기",
            use_container_width=True
        ):
            st.session_state.selected_drink = None
            go_to("order")

    with col2:
        if st.button(
            "🏠 처음 화면으로",
            use_container_width=True
        ):
            go_to("home")


# =====================================
# 14. 화면 아래 안내
# =====================================
st.divider()

st.markdown(
    """
    <p style="text-align:center; color:#52665a;">
        🌿 천천히 키오스크 | 누구나 편안하게 이용할 수 있도록
    </p>
    """,
    unsafe_allow_html=True
)
