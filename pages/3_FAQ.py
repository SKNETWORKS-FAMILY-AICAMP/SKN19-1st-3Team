import streamlit as st
import pandas as pd
import Data_input as Dinput
import re

# DB에서 DataFrame 형태로 로드
df = Dinput.load_data_to_db("SELECT * FROM car_faq")

st.title("Car FAQ")
st.markdown("---")

# 카테고리 선택
categories = df['category'].unique()
selected_category = st.selectbox("카테고리를 선택하세요:", categories)

# 검색어 입력
search_query = st.text_input("검색어를 입력하세요:")

# 선택한 카테고리로 필터링
filtered_df = df[df['category'] == selected_category]

# 검색어가 입력되면 question 또는 answer에 포함된 항목만 필터링
if search_query:
    filtered_df = filtered_df[
        filtered_df['question'].str.contains(search_query, case=False, na=False) |
        filtered_df['answer'].str.contains(search_query, case=False, na=False)
    ]

def highlight_keyword(text, keyword):
    if not keyword:
        return text
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return pattern.sub(f'<span style="color:red;font-weight:bold;">\\g<0></span>', text)

# FAQ 출력
for idx, row in filtered_df.iterrows():
    st.markdown("---")
    q_text = row['question'].strip()
    question_html = highlight_keyword(q_text, search_query)
    answer_html = highlight_keyword(row['answer'], search_query)
    st.markdown(f"**Q:** {question_html}", unsafe_allow_html=True)
    st.markdown(f"**A:** {answer_html}", unsafe_allow_html=True)
    if pd.notna(row.get('site')):
        st.markdown(f"🔗 출처: {row['site']}")
