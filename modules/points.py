import streamlit as st
import pandas as pd

def get_points_history():
    return [
        {"时间":"2026-05-01","类型":"完成订单","积分":+80},
        {"时间":"2026-05-02","类型":"客户好评","积分":+50},
        {"时间":"2026-05-03","类型":"签到奖励","积分":+20}
    ]

def get_available_rewards():
    return [
        {"id":1,"name":"无人机配件优惠券","description":"满200减50","points":500},
        {"id":2,"name":"高级课程免费名额","description":"兑换一门高级课","points":1500}
    ]

def contribution_system():
    """贡献值系统"""
    st.title("🏆 贡献值与激励体系")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("总贡献值", "1,250", "+120")
    with col2:
        st.metric("当前等级", "中级接单员", "↑")
    with col3:
        st.metric("排名", "第15名", "↑3")
    with col4:
        st.metric("可兑换", "2,500元", "查看")
    
    st.subheader("贡献值记录")
    points_data = get_points_history()
    df = pd.DataFrame(points_data)
    st.dataframe(df, use_container_width=True)
    
    with st.expander("贡献值计算规则"):
        st.write("""
        - 完成订单：基础金额×难度系数
        - 客户好评：+50贡献值/次
        - 推荐新用户：+100贡献值/人
        - 参与公益活动：+200贡献值/次
        - 成为讲师：+500贡献值
        """)
    
    st.subheader("🎁 兑换商城")
    rewards = get_available_rewards()
    current_points = 1250
    for reward in rewards:
        col1, col2 = st.columns([3,1])
        with col1:
            st.write(f"**{reward['name']}**")
            st.write(reward['description'])
        with col2:
            if st.button(f"兑换 {reward['points']}积分",disabled=reward['points'] > current_points):
                st.success("兑换申请提交成功")