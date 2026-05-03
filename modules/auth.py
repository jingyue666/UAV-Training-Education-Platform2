import streamlit as st
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("/tmp", "drone_platform.db")

def show_login():
    tab1, tab2 = st.tabs(["登录", "注册"])
    
    with tab1:
        username = st.text_input("用户名/手机号")
        password = st.text_input("密码", type="password")
        if st.button("登录"):
            authenticate(username, password)
    
    with tab2:
        reg_type = st.radio("注册类型", ["个人学员", "接单员", "企业用户"])
        username = st.text_input("用户名", key="reg_user")
        password = st.text_input("密码", type="password", key="reg_pwd")
        real_name = st.text_input("真实姓名")
        phone = st.text_input("手机号")

        if st.button("完成注册"):
            register_user(username, password, real_name, phone, reg_type)
            st.success("注册成功！请返回登录")

def register_user(username, password, real_name, phone, role):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, password, real_name, phone, role, level, points, balance)
            VALUES (?, ?, ?, ?, ?, ?, 0, 0)
        ''', (username, password, real_name, phone, role, "初级"))
        conn.commit()
    except Exception as e:
        st.error("用户名已存在")
    conn.close()

def authenticate(username, password):
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
        
        # 自动匹配菜单角色（解决菜单不显示问题）
        db_role = user[2]
        if db_role == "个人学员":
            st.session_state.role = "学员"
        else:
            st.session_state.role = db_role

        st.session_state.level = user[3]
        st.rerun()
    else:
        st.error("用户名或密码错误")

def logout():
    st.session_state.authenticated = False
    st.session_state.user_id = None
    st.session_state.username = ""
    st.session_state.role = "学员"
    st.rerun()
