import streamlit as st

st.set_page_config(page_title="📈 综合评价", layout="wide")
st.title("📈 综合评价")


# 对聊天分数转换
def convert_chat_score(score):
    return round((score + 5) * 10, 2)


# 对问卷分数转换
def convert_scl90_score(score):
    return round(100 - (score / 360) * 200, 2)


if "USER_CLASS" not in st.session_state:
    st.session_state["USER_CLASS"] = ""

if "USER_NAME" not in st.session_state:
    st.session_state["USER_NAME"] = ""

if "USER_SNO" not in st.session_state:
    st.session_state["USER_SNO"] = ""

if "FINAL_CHAT_SCORE" not in st.session_state:
    st.session_state["FINAL_CHAT_SCORE"] = 0

if "FINAL_SCL90_SCORE" not in st.session_state:
    st.session_state["FINAL_SCL90_SCORE"] = 0

if "CHAT_WEIGHT" not in st.session_state:
    st.session_state["CHAT_WEIGHT"] = 0

if "SCL90_WEIGHT" not in st.session_state:
    st.session_state["SCL90_WEIGHT"] = 0

if "CHAT_WEIGHT_SCORE" not in st.session_state:
    st.session_state["CHAT_WEIGHT_SCORE"] = 0

if "SCL90_WEIGHT_SCORE" not in st.session_state:
    st.session_state["SCL90_WEIGHT_SCORE"] = 0

if "TOTAL_SCORE" not in st.session_state:
    st.session_state["TOTAL_SCORE"] = 0


if st.session_state["USER_CLASS"] != "" and st.session_state["USER_NAME"] != "" and st.session_state[
    "USER_SNO"] != "" and st.session_state["CHAT_SCORE"] != None and st.session_state["SCORE"] != None:

    st.session_state["FINAL_CHAT_SCORE"] = convert_chat_score(st.session_state["CHAT_SCORE"])
    st.session_state["FINAL_SCL90_SCORE"] = convert_scl90_score(st.session_state["SCORE"])

    st.session_state["CHAT_WEIGHT"]= st.slider("聊天分析占比", 0.0, 1.0, 0.5, 0.01)
    st.session_state["SCL90_WEIGHT"]= 1 -st.session_state["CHAT_WEIGHT"]

    analysis= st.button("开始分析")

    if analysis :
        st.session_state["CHAT_WEIGHT_SCORE"]=st.session_state["FINAL_CHAT_SCORE"]*st.session_state["CHAT_WEIGHT"]
        st.session_state["SCL90_WEIGHT_SCORE"]=st.session_state["FINAL_SCL90_SCORE"]*st.session_state["SCL90_WEIGHT"]
        st.session_state["TOTAL_SCORE"] = st.session_state["CHAT_WEIGHT_SCORE"]+st.session_state["SCL90_WEIGHT_SCORE"]

        table = f"""
                | 分析项目 | 分数 |
                | --- | --- |
                | 聊天分析转换后的分数 | {st.session_state['FINAL_CHAT_SCORE']:.2f} |
                | SCL-90转换后的分数 | {st.session_state['FINAL_SCL90_SCORE']:.2f} |
                | 聊天分析加权分数 | {st.session_state['CHAT_WEIGHT_SCORE']:.2f} |
                | SCL-90加权分数 | {st.session_state['SCL90_WEIGHT_SCORE']:.2f} |
                | 总分 | {st.session_state['TOTAL_SCORE']:.2f} |
                """

        st.markdown(table)


    pass
else:
    st.write("请至主页输入完整个人信息，并在聊天分析和问卷分析后重新访问此页面")
