
import streamlit as st
import random

# --- 앱의 기본 설정 ---
# 웹 페이지의 제목(탭에 표시됨)과 아이콘을 설정합니다.
st.set_page_config(page_title="교사용 응원 카드", page_icon="💌")

# --- 교사가 직접 수정할 수 있는 부분 ---
# 응원 문구 리스트입니다. 원하는 만큼 추가하거나 수정하세요.
QUOTES = [
    "선생님의 따뜻한 말 한마디가 아이들의 세상을 바꿉니다.",
    "오늘도 아이들의 성장을 위해 애쓰시는 선생님을 응원합니다!",
    "가르침은 희망을 이야기하는 것입니다. 선생님은 희망의 전달자입니다.",
    "선생님의 열정이 아이들의 미래를 밝힙니다. 지치지 마세요!",
    "작은 씨앗을 위대한 나무로 키우는 선생님, 당신은 정원사입니다.",
    "실수는 배움의 과정일 뿐입니다. 너그럽게 지켜봐 주세요.",
    "선생님의 미소가 교실을 가장 밝은 곳으로 만듭니다. 오늘 하루도 웃으세요!",
    "아이들과 함께 웃고 성장하는 오늘 하루가 되길 바랍니다.",
    "세상을 바꾸는 가장 강력한 무기는 교육입니다. 선생님은 그 무기를 만드는 분입니다.",
    "이미 충분히 잘하고 계십니다. 스스로를 믿어주세요!"
]
# --- 코드 수정 끝 ---


# --- 앱의 핵심 로직 ---

# 앱의 제목을 화면에 표시합니다.
st.title("💌 교사용 응원 카드")
st.write("버튼을 눌러 오늘의 응원 메시지를 받아보세요!")

# 세션 상태(Session State) 초기화
# st.session_state는 사용자가 앱과 상호작용하는 동안 데이터를 기억하는 공간입니다.
# 'current_quote'가 아직 없으면 빈 문자열로 만들어줍니다.
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = ""
# 'previous_quote'가 아직 없으면 빈 문자열로 만들어줍니다.
if 'previous_quote' not in st.session_state:
    st.session_state.previous_quote = ""

# "오늘의 응원 받기" 버튼을 만듭니다.
if st.button("오늘의 응원 받기 CLICK! ✨"):
    # 이전에 표시했던 문구를 'previous_quote'에 저장합니다.
    st.session_state.previous_quote = st.session_state.current_quote
    
    # QUOTES 리스트에서 무작위로 하나를 선택합니다.
    new_quote = random.choice(QUOTES)
    
    # 선택된 새 문구를 'current_quote'에 저장합니다.
    st.session_state.current_quote = new_quote

# 현재 응원 문구가 있다면 화면에 예쁘게 표시합니다.
if st.session_state.current_quote:
    st.markdown(f"""
    <div style="padding: 20px; border-radius: 10px; background-color: #f0f2f6; text-align: center;">
        <h2 style="color: #333;">{st.session_state.current_quote}</h2>
    </div>
    """, unsafe_allow_html=True)
    st.write("") # 여백 추가

# 이전에 본 문구가 있을 경우에만 "최근 응원 문구 다시 보기" 버튼을 표시합니다.
if st.session_state.previous_quote:
    if st.button("↩️ 최근 응원 문구 다시 보기"):
        # 이전 문구를 정보 상자 형태로 표시합니다.
        st.info(f"이전 문구: {st.session_state.previous_quote}")
