import streamlit as st
import random

# Cấu hình giao diện
st.set_page_config(page_title="Chiến Binh Thủ Thành", page_icon="⚔️")

# CSS tạo màu sắc
st.markdown("""
    <style>
    .stApp { background-color: #0f2027; color: white; }
    .monster { font-size: 30px; }
    </style>
""", unsafe_allow_html=True)

# Khởi tạo game
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'monster_pos' not in st.session_state: st.session_state.monster_pos = 5
if 'score' not in st.session_state: st.session_state.score = 0

st.title("🛡️ Chiến Binh Thủ Thành")
st.write(f"### Máu của thành: {st.session_state.hp} | Điểm: {st.session_state.score}")

# Hiển thị "bản đồ" đơn giản
map_display = ["."] * 6
map_display[st.session_state.monster_pos] = "👾" # Quái vật
map_display[0] = "🏰" # Thành
st.subheader(" ".join(map_display))

# Điều khiển
col1, col2 = st.columns(2)

if col1.button("⚔️ Tấn công"):
    if st.session_state.monster_pos > 0:
        st.session_state.monster_pos -= 1
        st.session_state.score += 10
        st.success("Bạn đánh trúng quái vật!")
    if st.session_state.monster_pos == 0:
        st.session_state.monster_pos = 5 # Quái hồi sinh
        st.session_state.score += 50
    st.rerun()

if col2.button("🛡️ Hồi máu"):
    st.session_state.hp += 5
    st.warning("Bạn đã hồi phục 5 HP!")
    st.rerun()

# Logic quái tiến gần
if st.session_state.monster_pos > 0:
    st.session_state.monster_pos -= 1
    if st.session_state.monster_pos == 0:
        st.session_state.hp -= 20
        st.session_state.monster_pos = 5
        st.error("Quái vật đã chạm vào thành! Mất 20 HP!")

if st.session_state.hp <= 0:
    st.error("GAME OVER! Thành đã bị phá hủy.")
    if st.button("Chơi lại"):
        st.session_state.hp = 100
        st.session_state.monster_pos = 5
        st.session_state.score = 0
        st.rerun()
        
