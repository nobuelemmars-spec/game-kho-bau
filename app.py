import streamlit as st
import random
if 'score' not in st.session_state: st.session_state.score = 0
if 'treasure' not in st.session_state: st.session_state.treasure = random.randint(1, 3)
st.title("Game Tìm Kho Báu")
st.write(f"Điểm: {st.session_state.score}")
cols = st.columns(3)
for i, col in enumerate(cols, 1):
    if col.button(f"Cửa {i}"):
        if i == st.session_state.treasure:
            st.success("Thắng!")
            st.session_state.score += 1
        else:
            st.error(f"Thua! Kho báu ở cửa {st.session_state.treasure}")
        st.session_state.treasure = random.randint(1, 3)
        st.rerun()
