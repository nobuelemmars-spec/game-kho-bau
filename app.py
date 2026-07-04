import streamlit as st
import random
import time
st.title("Game Tìm Kho Báu")
if 'score' not in st.session_state: st.session_state.score = 0
if 'treasure' not in st.session_state: st.session_state.treasure = random.randint(1, 3)
if 'message' not in st.session_state: st.session_state.message = ""
st.write(f"### Điểm của bạn: {st.session_state.score}")
if st.session_state.message:
    st.info(st.session_state.message)
    if st.button("Chơi tiếp ván mới"):
        st.session_state.message = ""
        st.session_state.treasure = random.randint(1, 3)
        st.rerun()
cols = st.columns(3)
for i, col in enumerate(cols, 1):
    if col.button(f"Cửa {i}"):
        with st.spinner('Đang mở cửa...'):
            time.sleep(0.5) # Tạo độ trễ hồi hộp
            if i == st.session_state.treasure:
                st.session_state.score += 1
                st.session_state.message = f"Chúc mừng! Bạn đã tìm thấy kho báu ở cửa {i}!"
            else:
                st.session_state.score = max(0, st.session_state.score - 1)
                st.session_state.message = f"Thua rồi! Kho báu thực sự ở cửa {st.session_state.treasure}."
            st.rerun()
