import streamlit as st
from datetime import datetime
import folium
from streamlit_folium import st_folium

# 模拟数据占位
def get_available_orders(location, min_p, max_p, skill):
    return [
        {"id":1,"title":"城市航拍接单","date":"2026-05-04","location":"重庆","price":1200,"difficulty":"中级"},
        {"id":2,"title":"农田植保作业","date":"2026-05-05","location":"郊区","price":2800,"difficulty":"高级"}
    ]

def get_active_orders():
    return [{"id":1,"title":"楼盘航拍拍摄","progress":65}]

def get_active_devices():
    return [{"id":"UAV001","lat":29.56,"lng":106.55,"status":"飞行中"}]

def order_center():
    """接单大厅"""
    st.title("🎯 任务大厅")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        location = st.text_input("地点", placeholder="输入城市或区域")
    with col2:
        min_price, max_price = st.slider("预算范围", 0, 10000, (500, 5000))
    with col3:
        skill_level = st.multiselect("所需技能",["初级","中级","高级","农业植保","航拍","巡检"])
    
    orders = get_available_orders(location, min_price, max_price, skill_level)
    
    for order in orders:
        with st.container():
            st.markdown(f"### {order['title']}")
            col1, col2, col3 = st.columns([2,1,1])
            with col1:
                st.write(f"📅 {order['date']}")
                st.write(f"📍 {order['location']}")
                st.write(f"💰 ¥{order['price']}")
            with col2:
                st.metric("难度", order['difficulty'])
            with col3:
                if st.button("抢单", key=order['id']):
                    st.success("抢单成功！")

def order_management():
    """订单管理"""
    st.title("📋 我的订单")
    tabs = st.tabs(["进行中", "待验收", "已完成", "已取消"])
    
    with tabs[0]:
        active_orders = get_active_orders()
        for order in active_orders:
            with st.container():
                st.write(f"**{order['title']}**")
                st.progress(order['progress']/100)
                if st.button("上传进度", key=f"upload_{order['id']}"):
                    st.info("进度上传弹窗")

def realtime_monitoring():
    """实时监控"""
    st.title("📡 实时监控中心")
    m = folium.Map(location=[29.56, 106.55], zoom_start=12)
    devices = get_active_devices()
    for device in devices:
        folium.Marker([device['lat'], device['lng']],
            popup=f"设备{device['id']}",tooltip=device['status']).add_to(m)
    st_folium(m, width=700, height=500)
    st.subheader("实时视频")
    st.info("实时视频流加载中...")
    if st.button("🚨 紧急求助", type="primary"):
        st.warning("已发送紧急求助通知")

def grab_order(order_id):
    st.success(f"已成功接单 ID:{order_id}")

def upload_progress(order_id):
    st.info(f"上传任务进度 ID:{order_id}")