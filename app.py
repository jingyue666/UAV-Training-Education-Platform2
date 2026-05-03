import streamlit as st
from modules import auth, training, marketplace, admin, special_groups, points
import session_state

def main():
    st.set_page_config(
        page_title="无人机教培接单平台",
        page_icon="🚁",
        layout="wide"
    )

    # 初始化会话
    session_state.init()

    # 侧边栏
    with st.sidebar:
        # 有 logo 就放，没有注释也行
        # st.image("logo.png", width=150)
        st.title("导航菜单")

        if not st.session_state.authenticated:
            auth.show_login()
        else:
            user_role = st.session_state.role

            menu_options = {
                "学员": ["学习中心", "模拟训练", "接单大厅", "个人中心", "高校学生通道"],
                "接单员": ["任务大厅", "我的订单", "技能提升", "收益中心", "贡献值系统"],
                "企业用户": ["发布需求", "人才库", "项目管理", "企业中心"],
                "管理员": ["用户管理", "订单监控", "内容管理", "数据分析"]
            }

            opt_list = menu_options.get(user_role, [])
            selected = st.selectbox("选择功能模块", opt_list)

            if st.button("退出登录", use_container_width=True):
                auth.logout()

    # 主页面路由
    if not st.session_state.authenticated:
        st.title("🚁 无人机教培与接单平台")
        st.info("请在左侧登录/注册进入系统")
    else:
        route_content(selected, user_role)

def route_content(selected, role):
    if role == "学员":
        if selected == "学习中心":
            training.student_learning_center()
        elif selected == "模拟训练":
            training.flight_simulator()
        elif selected == "接单大厅":
            marketplace.order_center()
        elif selected == "高校学生通道":
            special_groups.student_channel()
    elif role == "接单员":
        if selected == "任务大厅":
            marketplace.order_center()
        elif selected == "我的订单":
            marketplace.order_management()
        elif selected == "贡献值系统":
            points.contribution_system()
    elif role == "管理员":
        if selected == "用户管理":
            admin.user_management()
        elif selected == "数据分析":
            admin.data_analytics()

if __name__ == "__main__":
    main()