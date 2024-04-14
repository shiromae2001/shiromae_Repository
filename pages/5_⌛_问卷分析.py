import streamlit as st

st.set_page_config(page_title="⌛ 问卷分析",layout="wide")
st.title("⌛ 问卷分析")



if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
    st.write("请至问卷填写问卷并提交")

if "USER_CLASS" not in st.session_state:
    st.session_state["USER_CLASS"] = ""

if "USER_NAME" not in st.session_state:
    st.session_state["USER_NAME"] = ""

if "USER_SNO" not in st.session_state:
    st.session_state["USER_SNO"] = ""


# 总分
if "SCORE" not in st.session_state:
    st.session_state["SCORE"] = 0

# 阳性
if "POSITIVE" not in st.session_state:
    st.session_state["POSITIVE"] = []

# 因子分
if "FACTOR_SCORE" not in st.session_state:
    st.session_state["FACTOR_SCORE"] = {}

# 躯体化list
check_list1 = {"1", "4", "12", "27", "40", "42", "48", "49", "52", "53", "56", "58"}
# 强迫症状list
check_list2 = {"3", "9", "10", "28", "38", "45", "46", "51", "55", "65"}
# 人际关系敏感list
check_list3 = {"6", "21", "34", "36", "37", "41", "61", "69", "73"}
# 抑郁
check_list4 = {"5", "14", "15", "20", "22", "26", "29", "30", "31", "32", "54", "71", "79"}
# 焦虑
check_list5 = {"2", "17", "23", "33", "39", "57", "72", "78", "80", "86"}
# 敌对
check_list6 = {"11", "24", "63", "67", "74", "81"}
# 恐怖
check_list7 = {"13", "25", "47", "50", "70", "75", "82"}
# 偏执
check_list8 = {"8", "18", "43", "68", "76", "83"}
# 精神病性
check_list9 = {"7", "16", "35", "62", "77", "84", "85", "87", "88", "90"}
# 睡眠及饮食
check_list10 = {"19", "44", "59", "60", "64", "66", "89"}


if st.session_state["USER_CLASS"] != "" and st.session_state["USER_NAME"] != "" and st.session_state["USER_SNO"] != "":
    # 求分数总和
    st.session_state["SCORE"]=sum(st.session_state.user_answers.values())
    # 求阳性题目列表
    st.session_state["POSITIVE"]=[key for key,value in st.session_state.user_answers.items() if value != 0]


    st.write(f"#### 欢迎来到问卷分析")
    st.write("下面是你的问卷结果的各项评分数值")
    st.markdown(f"""
    | 指标 | 分数 |
    | ---- | ---- |
    | 总分 | {st.session_state["SCORE"]} |
    | 总症状指数 | {st.session_state["SCORE"]/90:.2f} |
    | 阳性项目数 | {len(st.session_state["POSITIVE"])} |
    | 阳性症状均分 | {st.session_state["SCORE"]/(90-len(st.session_state["POSITIVE"])):.2f} |
    """)
    st.write("")
    st.write("")
    st.write(f"""根据你的总症状指数，你的自我症状属于：""")
    if 0 <= st.session_state["SCORE"] / 90 < 0.5:
        st.write(f"""自我感觉没有量表中所列的症状""")
    elif 0.5 <= st.session_state["SCORE"] / 90 < 1.5:
        st.write(f"""感觉有点症状,但发生得并不频繁""")
    elif 1.5 <= st.session_state["SCORE"] / 90 < 2.5:
        st.write(f"""感觉有症状,其严重程度为轻到中度""")
    elif 2.5 <= st.session_state["SCORE"] / 90 < 3.5:
        st.write(f"""感觉有症状,其程度为中到严重""")
    elif 3.5 <= st.session_state["SCORE"] / 90 <= 4:
        st.write(f"""感觉有症状,且症状的频度和强度都十分严重""")


    st.write(f"""--------------""")
    # 因子分

    st.write(f"""接下来是你的问卷结果的因子分析，你的因子分析结果包含以下几个方面""")
    if set(st.session_state["POSITIVE"]).intersection(check_list1):
        st.write(f"""**躯体化**：主要反映身体不适感，包括心血管、胃肠道、呼吸和其他系统的主诉不适，和头痛、背
痛、肌肉酸痛，以及焦虑的其他躯体表现。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list2):
        st.write(f"""**强迫症状**：主要指那些
明知没有必要，但又无法摆脱的无意义的思想、冲动和行为，还有一些比较一般的认知障
碍的行为征象也在这一因子中反映。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list3):
        st.write(f"""**人际关系敏感**：主要指某些个
人不自在与自卑感，特别是与其他人相比较时更加突出。在人际交往中的自卑感，心神不
安，明显不自在，以及人际交流中的自我意识，消极的期待亦是这方面症状的典型原因。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list4):
        st.write(f"""**抑郁**：苦
闷的情感与心境为代表性症状，还以生活兴趣的减退，动力缺乏，活力丧失等为特征。还
反映失望，悲观以及与抑郁相联系的认知和躯体方面的感受，另外，还包括有关死亡的思
想和自杀观念。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list5):
        st.write(f"""**焦虑**：一般指那些烦
躁，坐立不安，神经过敏，紧张以及由此产生的躯体征象，如震颤等。测定游离不定的焦
虑及惊恐发作是本因子的主要内容，还包括一项解体感受的项目。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list6):
        st.write(f"""**敌对**：主要从三方面来反映敌对的表现：
思想、感情及行为。其项目包括厌烦的感觉，摔物，争论直到不可控制的脾气暴发等各方
面。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list7):
        st.write(f"""**恐怖**：恐惧的对象包括出门旅行，空
旷场地，人群或公共场所和交通工具。此外，还有反映社交恐怖的一些项目。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list8):
        st.write(f"""**偏执**：本因子是围练偏执性思维的基本特征而制订：主要指投射性思维，敌对，猜疑，关系观念，妄想，被动体验和夸大等。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list9):
        st.write(f"""**精神病性**：反映各式各
样的急性症状和行为，限定不严的精神病性过程的指征。此外，也可以反映精神病性行为
的继发征兆和分裂性生活方式的指征。""")
    if set(st.session_state["POSITIVE"]).intersection(check_list10):
        st.write(f"""**睡眠及饮食**：此因子反应了睡眠和饮食的情况，这个现象涉及到日常生活的不规律，可能进而引发更大的精神问题""")

    st.write("在因子分的评定中，粗略简单的判断方法是看因子分是否超过**3**分，即表明该因子的症状已达到中等以上严重程度。")
    st.write("")
    st.write("")
    st.write("")
    # 这里用到了unsafe_allow_html，是的streamlit接受不安全的HTML渲染
    st.write("""
        <div style='text-align: center; font-size: 24px; font-weight: bold;'>
            SCL—90 测验结果处理
        </div>
    """, unsafe_allow_html=True)

    # 因子分计算
    for i in range(1,11):
        check_list=eval(F"check_list{i}")
        factor_score = sum([st.session_state.user_answers[q] for q in check_list if q in st.session_state.user_answers])
        st.session_state["FACTOR_SCORE"][f"F{i}"]= factor_score


    st.write(f"""
    |      因子      |      因子含义      |                             项目                             |    T分=项目总分/项目数    |    T分    |    症状程度    |
|----------------|--------------------|------------------------------------------------------------|--------------------------|-----------|---------------|
| F1             | 躯体化             | 1、4、12、27、40、42、48、49、52、53、56、58               | {st.session_state["FACTOR_SCORE"]['F1']}/12                      | {st.session_state["FACTOR_SCORE"]['F1']/12:.2f}         | {'躯体症状表现不明显' if st.session_state["FACTOR_SCORE"]['F1']<12 else '躯体症状一般' if 12<st.session_state["FACTOR_SCORE"]['F1']<24 else '躯体化严重'}             |
| F2             | 强迫               | 3、9、10、28、38、45、46、51、55、65                       | {st.session_state["FACTOR_SCORE"]['F2']}/10                      | {st.session_state["FACTOR_SCORE"]['F2']/10:.2f}         | {'强迫症状不明显' if st.session_state["FACTOR_SCORE"]['F2']<12 else '强迫症状一般' if 12<st.session_state["FACTOR_SCORE"]['F2']<24 else '强迫症状较明显'}             |
| F3             | 人际关系           | 6、21、34、36、37、41、61、69、73                          | {st.session_state["FACTOR_SCORE"]['F3']}/9                       | {st.session_state["FACTOR_SCORE"]['F3']/9:.2f}         | {'人际关系上较为正常' if st.session_state["FACTOR_SCORE"]['F3']<12 else '人际关系一般' if 12<st.session_state["FACTOR_SCORE"]['F3']<24 else '人际关系较为敏感'}             |
| F4             | 抑郁               | 5、14、15、20、22、26、29、30、31、32、54、71、79          | {st.session_state["FACTOR_SCORE"]['F4']}/13                      | {st.session_state["FACTOR_SCORE"]['F4']/13:.2f}         | {'抑郁程度较弱' if st.session_state["FACTOR_SCORE"]['F4']<12 else '有抑郁倾向' if 12<st.session_state["FACTOR_SCORE"]['F4']<24 else '抑郁程度较强'}             |
| F5             | 焦虑               | 2、17、23、33、39、57、72、78、80、86                      | {st.session_state["FACTOR_SCORE"]['F5']}/10                      | {st.session_state["FACTOR_SCORE"]['F5']/10:.2f}         | {'不易焦虑' if st.session_state["FACTOR_SCORE"]['F5']<12 else '有焦虑倾向' if 12<st.session_state["FACTOR_SCORE"]['F5']<24 else '较易焦虑'}             |
| F6             | 敌对性             | 11、24、63、67、74、81                                     | {st.session_state["FACTOR_SCORE"]['F6']}/6                       | {st.session_state["FACTOR_SCORE"]['F6']/6:.2f}        | {'呈现友好的思想、情感和行为' if st.session_state["FACTOR_SCORE"]['F6']<12 else '有敌对的思想的倾向' if 12<st.session_state["FACTOR_SCORE"]['F6']<24 else '易表现出敌对的思想'}             |
| F7             | 恐怖               | 13、25、47、50、70、75、82                                 | {st.session_state["FACTOR_SCORE"]['F7']}/7                       | {st.session_state["FACTOR_SCORE"]['F7']/7:.2f}         | {'恐怖症状不明显' if st.session_state["FACTOR_SCORE"]['F7']<12 else '恐怖症状一般' if 12<st.session_state["FACTOR_SCORE"]['F7']<24 else '恐怖症状较为明显'}             |
| F8             | 偏执               | 8、18、43、68、76、83                                      | {st.session_state["FACTOR_SCORE"]['F8']}/6                       | {st.session_state["FACTOR_SCORE"]['F8']/6:.2f}         | {'偏执症状不明显' if st.session_state["FACTOR_SCORE"]['F8']<12 else '偏执症状一般' if 12<st.session_state["FACTOR_SCORE"]['F8']<24 else '偏执症状明显'}             |
| F9             | 精神病性           | 7、16、35、62、77、84、85、87、88、90                      | {st.session_state["FACTOR_SCORE"]['F9']}/10                      | {st.session_state["FACTOR_SCORE"]['F9']/10:.2f}         | {'精神病性症状不明显' if st.session_state["FACTOR_SCORE"]['F9']<12 else '精神病性症状一般' if 12<st.session_state["FACTOR_SCORE"]['F9']<24 else '精神病性症状较为明显'}             |
| F10            | 睡眠及饮食         | 13、25、47、50、70、75、82                                 | {st.session_state["FACTOR_SCORE"]['F10']}/7                       | {st.session_state["FACTOR_SCORE"]['F10']/7:.2f}         | \             |
""")

    st.write("在完成聊天分析后，可前往**综合评价**页面查看聊天和问卷的综合评价")
else:
    st.write("请至主页输入完整个人信息")