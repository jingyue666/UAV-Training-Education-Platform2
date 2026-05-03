import streamlit as st
import sqlite3
import os
from datetime import datetime

# 适配云端数据库路径
DB_PATH = os.path.join("/tmp", "drone_platform.db")

# 临时禁用人脸识别，避免部署报错
# import face_recognition_api

def show_login():
    """登录/注册界面"""
    tab1, tab2 = st.tabs(["登录", "注册"])
    
    with tab1:
        username = st.text_input("用户名/手机号")
        password = st.text_input("密码", type="password")
        if st.button("登录"):
            authenticate(username, password)
    
    with tab2:
        reg_type = st.radio("注册类型", ["个人学员", "接单员", "企业用户"])
        if reg_type == "接单员":
            show_pilot_registration()

def show_pilot_registration():
    st.text_input("真实姓名")
    st.text_input("手机号")
    st.text_input("设置用户名")
    st.text_input("设置密码", type="password")
    st.selectbox("技能等级", ["初级","中级","高级"])
    if st.button("立即注册"):
        st.success("注册提交成功，等待管理员审核")

def authenticate(username, password):
    """验证用户凭证"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, username, role, level FROM users 
        WHERE username=? AND password=?
    ''', (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        st.session_state.authenticated = True
        st.session_state.user_id = user[0]
        st.session_state.username = user[1]
        st.session_state.role = user[2]
        st.session_state.level = user[3]
        st.success("登录成功！")
        st.rerun()
    else:
        st.error("用户名或密码错误")

def logout():
    st.session_state.authenticated = False
    st.session_state.user_id = None
    st.session_state.username = ""
    st.session_state.role = "学员"
    st.rerun()