import streamlit as st

def init():
    # 初始化所有会话状态
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "role" not in st.session_state:
        st.session_state.role = "学员"
    if "level" not in st.session_state:
        st.session_state.level = "初级"
    if "student_verified" not in st.session_state:
        st.session_state.student_verified = False