import streamlit as st
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import torch
from torch import nn
import jieba
import re
from gensim.models import Word2Vec

st.set_page_config(page_title="💭 聊天分析",layout="wide")
st.title("💭 聊天分析")

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

if "CHAT_SCORE" not in st.session_state:
    st.session_state["CHAT_SCORE"] = 0



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
model_path = 'model_9_1_epoch50.pth'
word2vec_model_path = 'model_9_1.model'
label={'厌恶': 0, '快乐': 1, '喜欢': 2, '愤怒': 3, '惊讶': 4, '悲伤': 5, '恐惧': 6}
# 将字典的键值对调换，使得值作为键，键作为值
reversed_label = {value: key for key, value in label.items()}
class BiLSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers, dropout):
        super(BiLSTM, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True, bidirectional=True, dropout=dropout)
        self.fc = nn.Linear(hidden_dim * 2, output_dim)

    def forward(self, x):
        batch_size = x.size(0)
        h0 = torch.zeros(self.num_layers * 2, batch_size, self.hidden_dim).to(x.device)
        c0 = torch.zeros(self.num_layers * 2, batch_size, self.hidden_dim).to(x.device)

        x = x.unsqueeze(1)  # 将输入数据转换为 3-D 张量
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

word2vec_model = Word2Vec.load(word2vec_model_path)

input_dim = 256
hidden_dim = 512
output_dim = 7
num_layers = 3
dropout = 0.2
bilstm_model = BiLSTM(input_dim=input_dim, hidden_dim=hidden_dim, output_dim=output_dim, num_layers=num_layers,dropout=dropout).to(device)
bilstm_model.load_state_dict(torch.load(model_path))
bilstm_model.eval()


def preprocess_text(text):
    # 分词
    words = jieba.lcut(text)
    # 过滤掉标点符号
    words = [re.sub("[\s+\.\!\/,$%^*(+\"\'''""《》]+|[+——！，。？、~@#￥%……&*（）：；''""]+", "", word) for word in words if
             len(word) > 0]
    return words


def get_vector(words):
    vectors = [word2vec_model.wv[word] for word in words if word in word2vec_model.wv]
    if not vectors:
        vectors = [torch.zeros(word2vec_model.vector_size)]  # 使用全零向量作为默认向量
    vector = sum(vectors) / len(vectors)
    return vector

if st.session_state["USER_CLASS"] != "" and st.session_state["USER_NAME"] != "" and st.session_state["USER_SNO"] != "" and st.session_state["MESSAGES"] != []:
    st.write("根据聊天测评的记录，你的聊天分析如下：")
    st.write("----")

    for message in st.session_state["MESSAGES"]:
        if isinstance(message, HumanMessage):
            word=preprocess_text(message.content)
            vector=get_vector(word)
            data=torch.tensor(vector, dtype=torch.float32).unsqueeze(0).to(device)
            with torch.no_grad():
                output = bilstm_model(data)
                predicted_class = torch.argmax(output).item()

            st.write(message.content)
            st.write(f"""分词结果：{word}""")

            if predicted_class in reversed_label:
                predicted_emotion = reversed_label[predicted_class]
                st.write(f'预测的类别: {predicted_emotion}')
                if predicted_class in [1, 2, 4]:
                    st.session_state["CHAT_SCORE"] += 1
                else:
                    st.session_state["CHAT_SCORE"] -= 1
            st.write("----")
    st.write("在完成问卷分析后，可前往**综合评价**页面查看聊天和问卷的综合评价")

else:
    st.write("请至主页输入完整个人信息，并在聊天室完成聊天流程后返回此页面")