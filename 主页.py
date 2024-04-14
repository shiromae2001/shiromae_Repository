import streamlit as st

st.set_page_config(page_title="大学生心里健康分析系统",layout="wide")
# 班级、姓名、学号置空
# 在st界面中。'''会被当成st.write直接输出

# 使用方法 streamlit run 主页.py --theme.primaryColor=white


if "USER_CLASS" not in st.session_state:
    st.session_state["USER_CLASS"] = ""

if "USER_NAME" not in st.session_state:
    st.session_state["USER_NAME"] = ""

if "USER_SNO" not in st.session_state:
    st.session_state["USER_SNO"] = ""

if "USER_TEXT" not in st.session_state:
    st.session_state["USER_TEXT"] = ""

if "MESSAGES" not in st.session_state:
    st.session_state["MESSAGES"] = []

questions = ["你今天心情怎么样", "2", "3"]
if "COUNT" not in st.session_state:
    st.session_state["COUNT"] = 0

if "STATU" not in st.session_state:
    st.session_state["STATU"] = 0



st.title("大学生心里健康分析系统")


if st.session_state["USER_CLASS"] != "" and st.session_state["USER_NAME"] != "" and st.session_state["USER_SNO"] != "":
    with st.container():
        st.write(f"""
            欢迎您，{st.session_state["USER_CLASS"]}班的{st.session_state["USER_NAME"]}同学
            """)


else:
    with st.container():
        # 设置三个并排的输入框
        col1, col2, col3 = st.columns(3)

        with col1:
            user_class = st.text_input("班级", value=st.session_state['USER_CLASS'], max_chars=None, key=1,
                                       type='default')

        with col2:
            user_name = st.text_input("姓名", value=st.session_state['USER_NAME'], max_chars=None, key=2,
                                      type='default')

        with col3:
            user_sno = st.text_input("学号", value=st.session_state['USER_SNO'], max_chars=None, key=3, type='default')

        saved = st.button("保存")

        if saved and user_class != "" and user_name != "" and user_sno != "":
            st.session_state["USER_CLASS"] = user_class
            st.session_state["USER_NAME"] = user_name
            st.session_state["USER_SNO"] = user_sno
            st.rerun()
        elif user_class == "" or user_name == "" or user_sno == "":
            st.write("请输入完整的信息")

