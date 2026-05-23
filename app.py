import streamlit as st

# 设置网页的标题和图标
st.set_page_config(page_title="JARVIS 维修管家", page_icon="🤖")

st.title("🤖 JARVIS 商业维修智能管家")
st.write("老板，请在下方选择设备症状，系统将自动生成排查方案和报价。")

device = st.selectbox("第一步：请选择故障设备", ["请选择", "炸炉", "冰柜"])

if device == "炸炉":
symptom = st.radio("第二步：请选择具体症状", ["不热", "跳闸"])

if st.button("开始诊断"):
    if symptom == "不热":
        st.success("诊断完成！")
        st.write("🔌 **故障原因：** 90% 是发热管烧断，10% 是温控器失灵。")
        st.write("💵 **建议收费：** RM 150 - 250")
        st.write("💡 **预计利润：** 约 RM 100 - 190")
    elif symptom == "跳闸":
        st.warning("安全警告！")
        st.write("🔌 **故障原因：** 发热管破损漏电，或内部电线短路。")
        st.write("⚠️ **行动建议：** 请务必先拔掉电源！带万用表去测电阻。")

elif device == "冰柜":
if st.button("开始诊断"):
    st.success("诊断完成！")
    st.write("❄️ **故障原因：** 压缩机有声音但不冷，通常是漏雪种或散热网太脏。")
    st.write("🛠️ **行动建议：** 先帮清洗底部的散热风扇，这招能解决一半问题，直接收 RM 80 清洁费！")
