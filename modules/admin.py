import streamlit as st
import pandas as pd
import plotly.express as px

def get_users(search, role_filter, status_filter):
    return [
        {"id":1,"username":"user01","role":"学员","status":"正常"},
        {"id":2,"username":"pilot01","role":"接单员","status":"正常"},
        {"id":3,"username":"ent01","role":"企业","status":"待审核"}
    ]

def get_user_growth_data():
    return pd.DataFrame({
        "date":["1月","2月","3月","4月","5月"],
        "count":[120,280,560,1300,2450]
    })

def get_order_distribution():
    return pd.DataFrame({
        "type":["航拍","植保","巡检","赛事"],
        "count":[120,95,80,45]
    })

def get_revenue_data():
    return pd.DataFrame({
        "source":["课程售卖","平台抽成","企业订单","增值服务"],
        "amount":[58000,32000,45000,21800]
    })

def user_management():
    """用户管理后台"""
    st.title("👥 用户管理")
    col1, col2, col3 = st.columns(3)
    with col1:
        search = st.text_input("搜索用户")
    with col2:
        role_filter = st.multiselect("角色", ["学员", "接单员", "企业", "讲师"])
    with col3:
        status_filter = st.multiselect("状态", ["正常", "禁用", "待审核"])
    
    users = get_users(search, role_filter, status_filter)
    df = pd.DataFrame(users)
    
    edited_df = st.data_editor(
        df,
        column_config={
            "id": st.column_config.NumberColumn("ID", disabled=True),
            "username": "用户名",
            "role": st.column_config.SelectboxColumn(
                "角色", options=["学员", "接单员", "企业", "讲师", "管理员"]
            ),
            "status": st.column_config.SelectboxColumn(
                "状态", options=["正常", "禁用", "待审核"]
            )
        },
        use_container_width=True
    )
    
    if st.button("保存更改"):
        st.success("用户信息已更新")

def data_analytics():
    """数据分析仪表板"""
    st.title("📊 数据统计与分析")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("总用户数", "2,458", "+12%")
    with col2:
        st.metric("月订单量", "324", "+8%")
    with col3:
        st.metric("完成率", "92%", "+2%")
    with col4:
        st.metric("总收入", "¥156,800", "+15%")
    
    tab1, tab2, tab3 = st.tabs(["用户增长", "订单分析", "收入分布"])
    
    with tab1:
        user_growth = get_user_growth_data()
        fig = px.line(user_growth, x="date", y="count", title="用户增长趋势")
        st.plotly_chart(fig)
    
    with tab2:
        order_data = get_order_distribution()
        fig = px.pie(order_data, values="count", names="type", title="订单类型分布")
        st.plotly_chart(fig)
    
    with tab3:
        revenue_data = get_revenue_data()
        fig = px.bar(revenue_data, x="source", y="amount", title="收入来源分布")
        st.plotly_chart(fig)