import os
import streamlit as st
import pandas as pd

def main():
    st.title("问卷测评")

    # 读取文件夹内的文件名
    folder_path = "test"  # 替换为你的文件夹路径
    files = os.listdir(folder_path)
    xlsx_files = [file for file in files if file.endswith(".xlsx")]

    # 下拉框选择文件
    selected_file = st.selectbox("选择问卷", xlsx_files)

    if st.button("开始测评"):
        if selected_file:
            file_path = os.path.join(folder_path, selected_file)
            questionnaire_page(file_path)
        else:
            st.warning("请先选择一个问卷文件")

def questionnaire_page(file_path):
    # 读取问卷数据
    df = pd.read_excel(file_path)

    # 初始化答案字典
    if "ANSWER" not in st.session_state:
        st.session_state["ANSWER"] = {}

    # 获取题目总数
    total_questions = len(df)

    # 获取当前题目序号
    if "current_question" not in st.session_state:
        st.session_state["current_question"] = 1

    current_question = st.session_state["current_question"]

    # 显示题目序号
    st.write(f"当前题目：{current_question}/{total_questions}")

    # 显示题目和选项
    question = df.loc[current_question - 1, "问题"]
    options = [df.loc[current_question - 1, f"选项{i+1}"] for i in range(5)]

    st.write(question)
    selected_option = st.radio("选择答案", options, key=f"question_{current_question}")

    # 保存答案
    st.session_state["ANSWER"][current_question] = selected_option

    # 上一题和下一题按钮
    col1, col2 = st.columns(2)
    if col1.button("上一题") and current_question > 1:
        st.session_state["current_question"] -= 1
        st.experimental_rerun()
    if col2.button("下一题") and current_question < total_questions:
        st.session_state["current_question"] += 1
        st.experimental_rerun()

    # 题号按钮
    question_numbers = [str(i) for i in range(1, total_questions + 1)]
    selected_question = st.selectbox("跳转题目", question_numbers, index=current_question - 1)
    if st.button("跳转"):
        st.session_state["current_question"] = int(selected_question)
        st.experimental_rerun()

    # 提交和退出按钮
    col1, col2 = st.columns(2)
    if col1.button("提交"):
        # 在这里可以添加提交答案的逻辑
        st.success("答案已提交")
        st.session_state["ANSWER"] = {}  # 清空答案字典
        st.session_state["current_question"] = 1  # 重置当前题目序号
        st.experimental_rerun()

    if col2.button("退出答题"):
        st.session_state["ANSWER"] = {}  # 清空答案字典
        st.session_state["current_question"] = 1  # 重置当前题目序号
        st.experimental_rerun()

if __name__ == "__main__":
    main()