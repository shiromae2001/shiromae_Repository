import streamlit as st
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

if "USER_CLASS" not in st.session_state:
    st.session_state["USER_CLASS"] = ""

if "USER_NAME" not in st.session_state:
    st.session_state["USER_NAME"] = ""

if "USER_SNO" not in st.session_state:
    st.session_state["USER_SNO"] = ""


if "USER_TEXT" not in st.session_state:
    st.session_state["USER_TEXT"] = ""

st.set_page_config(page_title="File Submit", layout="wide")

st.title("💬 聊天测评")

# 如果消息不存在，则初始化成一个空的数组
if "MESSAGES" not in st.session_state:
    st.session_state["MESSAGES"] = []

questions = ["最近你的睡眠质量如何？", "最近生活很疲惫还是很轻松？", "你最近一次看的电影是什么？心情觉得怎么样？","最近有什么喜欢做的事情吗？"]
if "COUNT" not in st.session_state:
    st.session_state["COUNT"] = 0

if "STATU" not in st.session_state:
    st.session_state["STATU"] = 0

if st.session_state["USER_CLASS"] != "" and st.session_state["USER_NAME"] != "" and st.session_state["USER_SNO"] != "":
    # 如果 STATU 为 0,初始化一个对话
    if st.session_state["STATU"] == 0:
        system_message = "你好，我是聊天对话机器人，很高兴见到你"
        st.session_state["MESSAGES"].append(SystemMessage(content=system_message))
        system_message = """接下来，我将对你进行一些提问，来对你进行心理健康分析"""
        st.session_state["MESSAGES"].append(SystemMessage(content=system_message))
        system_message = """你今天心情怎么样？"""
        st.session_state["MESSAGES"].append(SystemMessage(content=system_message))
        st.session_state["STATU"] = st.session_state["STATU"] +1


    # 这个for循环会反复重绘对话框
    # 如果需要在对话开始前就让assistant说话就放入一个system_message
    for message in st.session_state["MESSAGES"]:
        if isinstance(message,HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)

        elif isinstance(message,SystemMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)

    user_text = st.chat_input("Say something")
    if user_text:
        st.session_state["MESSAGES"].append(HumanMessage(content=user_text))
        with st.chat_message("user"):
            st.markdown(user_text)

        if st.session_state["COUNT"] < len(questions):
            system_message = questions[st.session_state["COUNT"]]
            st.session_state["MESSAGES"].append(SystemMessage(content=system_message))
            st.session_state["COUNT"] = st.session_state["COUNT"] + 1
            with st.chat_message("assistant"):
                st.markdown(system_message)
        else:
            with st.chat_message("assistant"):
                system_message = "所有问题回答完毕，很高兴和你聊天"
                st.session_state["MESSAGES"].append(SystemMessage(content=system_message))
                st.rerun()




else:
    st.write("请至主页输入完整个人信息")
