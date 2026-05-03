import streamlit as st

def get_intern_orders():
    return [
        {"id":1,"title":"航拍实习助理","location":"重庆江北","reward":"150/天"},
        {"id":2,"title":"电力巡检实习生","location":"重庆南岸","reward":"180/天"}
    ]

def student_channel():
    """高校学生专用通道"""
    st.title("🎓 高校学生专用通道")
    
    if not st.session_state.get("student_verified"):
        st.info("请先进行学生认证")
        col1, col2 = st.columns(2)
        with col1:
            student_id = st.text_input("学号")
            university = st.text_input("学校")
        with col2:
            st.file_uploader("上传学生证", type=['jpg', 'png'])
        
        if st.button("提交认证"):
            st.session_state.student_verified = True
            st.success("✅ 学生认证通过，刷新中...")
            st.rerun()
    else:
        st.success("✅ 学生认证已通过")
        tabs = st.tabs(["实习订单", "课程折扣", "比赛活动", "就业推荐"])
        with tabs[0]:
            intern_orders = get_intern_orders()
            for order in intern_orders:
                with st.container():
                    st.write(f"**{order['title']}**")
                    st.write(f"📍 {order['location']} | 🎓 实习证明 | 💰 {order['reward']}")
                    if st.button("申请实习", key=order['id']):
                        st.success("实习申请已提交")

def veteran_channel():
    """退役军人/失业人员通道"""
    st.title("🪖 退役军人/失业人员支持通道")
    identity = st.radio("您的身份", ["退役军人", "失业人员"])
    st.subheader("支持政策")
    if identity == "退役军人":
        st.write("""
        - 学费减免50%
        - 优先安排实习岗位
        - 就业推荐优先
        """)
        if st.button("申请退役军人福利"):
            st.success("福利申请已提交")
    else:
        st.write("""
        - 政府补贴培训
        - 免费基础课程
        - 就业指导服务
        """)