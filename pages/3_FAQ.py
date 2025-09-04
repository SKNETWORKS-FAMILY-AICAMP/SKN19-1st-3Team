import streamlit as st
import pandas as pd
import Data_input as Dinput
from PIL import Image 
import re

# DB에서 DataFrame 형태로 로드
df = Dinput.load_data_to_db("SELECT * FROM car_faq")

# st.title("Car FAQ")
my_image = Image.open('./data/image_03.jpg')
st.image(my_image)
st.markdown("---")

# 카테고리 선택
# categories = df['category'].unique()
# selected_category = st.selectbox("카테고리를 선택하세요:", categories)
with st.container():
    st.markdown('<div class="input-box"><span class="input-label">📂 카테고리를 선택하세요</span>', unsafe_allow_html=True)
    selected_category = st.selectbox("", df['category'].unique(), label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# 검색어 입력
# search_query = st.text_input("검색어를 입력하세요:")
with st.container():
    st.markdown('<div class="input-box"><span class="input-label">🔍 검색어를 입력하세요</span>', unsafe_allow_html=True)
    search_query = st.text_input("", "", placeholder="예: 견적, 기준...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# 선택한 카테고리로 필터링
filtered_df = df[df['category'] == selected_category].copy()
filtered_df['question'] = filtered_df['question'].apply(
    lambda x: x.rstrip()[:-4].rstrip() if isinstance(x, str) and x.rstrip().endswith("연장하다") else x
)

# 검색어가 입력되면 question 또는 answer에 포함된 항목만 필터링
if search_query:
    filtered_df = filtered_df[
        filtered_df['question'].str.contains(search_query, case=False, na=False) |
        filtered_df['answer'].str.contains(search_query, case=False, na=False)
    ]

# 검색된 FAQ 개수 출력
results_len = len(filtered_df)
if results_len > 0:
    st.info(f"총 {results_len}개의 FAQ가 검색되었습니다.")
else:
    st.warning(f"검색 결과가 없습니다. 다시 입력해주세요.")

# FAQ 출력
def highlight_keyword(text, keyword):
    if not keyword:
        return text
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return pattern.sub(f'<span style="color:#ff4757;font-weight:600;">\\g<0></span>', text)

# for idx, row in filtered_df.iterrows():
#     st.markdown("---")
#     q_text = row['question'].strip()
#     question_html = highlight_keyword(q_text, search_query)
#     answer_html = highlight_keyword(row['answer'], search_query)
#     st.markdown(f"**Q:** {question_html}", unsafe_allow_html=True)
#     st.markdown(f"**A:** {answer_html}", unsafe_allow_html=True)
#     if pd.notna(row.get('site')):
#         st.markdown(f"🔗 출처: {row['site']}")

faq_card_style = """
<style>
.faq-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 20px 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.faq-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
.faq-question {
    font-size: 19px;
    font-weight: 700;
    color: #2d3436;
    margin-bottom: 12px;
}
.faq-answer {
    font-size: 16px;
    color: #444;
    line-height: 1.6;
    padding-left: 5px;
    border-left: 3px solid #ff6b6b20;
}
.faq-answer-line {
    margin-bottom: 6px;
}
.faq-source {
    font-size: 14px;
    color: #636e72;
    margin-top: 12px;
}
</style>
"""
st.markdown(faq_card_style, unsafe_allow_html=True)

for idx, row in filtered_df.iterrows():
    q_text = row['question'].strip()
    question_html = highlight_keyword(q_text, search_query)

    answer_lines = row['answer'].splitlines()
    answer_html = "".join(
        [f'<div class="faq-answer-line">{highlight_keyword(line, search_query)}</div>' for line in answer_lines if line.strip()]
    )

    st.markdown(f"""
    <div class="faq-card">
        <div class="faq-question">💬 {question_html}</div>
        <div class="faq-answer">{answer_html}</div>
        {f'<div class="faq-source">🔗 출처: {row["site"]}</div>' if pd.notna(row.get("site")) else ""}
    </div>
    """, unsafe_allow_html=True)
