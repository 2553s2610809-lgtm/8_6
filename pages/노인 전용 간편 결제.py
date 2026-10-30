
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="편한결제",
    page_icon="💳",
    layout="wide"
)

# 상단 로고
st.markdown(
    """
    <div style="font-size:30px; font-weight:bold; color:#174A78;">
        편한결제
    </div>
    <div style="font-size:17px; color:#58738D;">
        누구나 쉽고 편하게
    </div>
    """,
    unsafe_allow_html=True
)
