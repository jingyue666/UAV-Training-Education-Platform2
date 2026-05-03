import streamlit as st
import pandas as pd
import plotly.express as px

# 模拟数据函数占位
def get_courses_by_level(level):
    return [
        {"id":1,"name":f"{level}无人机基础飞行","progress":35},
        {"id":2,"name":f"{level}航拍构图实操","progress":60}
    ]

def get_learning_progress():
    return pd.DataFrame({
        "课程":["基础飞行","航拍实操","应急避障"],"进度":[35,60,20],"状态":["进行中","进行中","未开始"]
    })

def student_learning_center():
    """学员学习中心"""
    st.title("📚 学习中心")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("初级课程", use_container_width=True):
            show_courses("初级")
    with col2:
        if st.button("中级课程", use_container_width=True):
            show_courses("中级")
    with col3:
        if st.button("高级课程", use_container_width=True):
            show_courses("高级")
    
    st.subheader("专项课程")
    specialties = ["农业植保", "城市治理", "应急救援", "电力巡检"]
    for spec in specialties:
        with st.expander(f"🎯 {spec}"):
            show_specialty_courses(spec)
    
    st.subheader("学习进度")
    progress_data = get_learning_progress()
    fig = px.bar(progress_data, x="课程", y="进度", color="状态")
    st.plotly_chart(fig)

def show_courses(level):
    courses = get_courses_by_level(level)
    for course in courses:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {course['name']}")
                st.progress(course['progress']/100)
                st.caption(f"进度: {course['progress']}%")
            with col2:
                if st.button("进入学习", key=course['id']):
                    st.info("课程播放器已打开")

def show_specialty_courses(spec):
    st.write(f"{spec} 专项课程正在加载...")
    st.button("报名学习")

def open_course_player(course_id):
    st.info(f"正在播放课程 ID:{course_id}")

def flight_simulator():
    """飞行模拟器"""
    st.title("🕹️ 无人机飞行模拟器")
    
    sim_type = st.selectbox(
        "选择模拟场景",
        ["重庆山地飞行", "城市楼宇巡检", "农田植保作业", "电力线路巡视"]
    )
    
    st.info(f"当前场景：{sim_type} 模拟器加载中...")
    st.components.v1.html("""
    <div style="height:600px;background:#222;color:#fff;text-align:center;padding-top:280px;font-size:20px;">
    无人机模拟器嵌入窗口
    </div>
    """, height=600)
    
    with st.expander("操作指南"):
        st.write("1. 使用键盘WASD控制方向")
        st.write("2. 鼠标控制视角")
        st.write("3. 空格键起飞/降落")

def online_exam():
    st.title("📝 在线考核")
    exam_type = st.selectbox("选择考试类型",["理论考试","模拟飞行考核","实操视频考核"])
    if exam_type == "理论考试":
        st.info("理论题库加载中...")