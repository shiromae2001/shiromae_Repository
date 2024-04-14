import streamlit as st
import pandas as pd

st.title("心理健康问卷")

if 'start' not in st.session_state:
    st.session_state.start = False

if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = None

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

file_path = "C:\\Users\\shiromae\\PycharmProjects\\pythonProject1\\pages\\问卷.xlsx"
quiz_data = pd.read_excel(file_path)

# 选项对应的分值
option_mapping = {
    "无": 0,
    "轻度": 1,
    "中度": 2,
    "偏重": 3,
    "严重": 4
}

if not st.session_state.start:
    st.write("欢迎参加心理健康问卷调查!")
    if st.button("开始答题"):
        st.session_state.start = True
        st.session_state.current_quiz = quiz_data.to_dict('records')
else:
    if st.session_state.current_quiz:
        for i, question in enumerate(st.session_state.current_quiz):
            st.write(f"**{question['问题']}**")
            options = [question['选项1'], question['选项2'], question['选项3'], question['选项4'],
                       question['选项5']]
            user_answer = st.radio("", options, key=f"Q{i + 1}", index=0)
            st.session_state.user_answers[f"{i + 1}"] = user_answer

        if st.button("提交"):
            # 把对应的答案替换成分数
            for key, value in st.session_state.user_answers.items():
                st.session_state.user_answers[key] = option_mapping[value]

            st.write("用户答案:")
            st.write(st.session_state.user_answers)
            # 在这里可以对用户的答案进行处理和分析
            st.write("问卷已提交,感谢您的参与!")
            st.session_state.start = False
            st.session_state.current_quiz = None

    else:
        st.write("问卷已完成,感谢您的参与!")
        st.session_state.start = False
