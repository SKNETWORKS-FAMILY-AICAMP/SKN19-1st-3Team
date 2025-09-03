import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import Data_input as Dinput

plt.rc("font", family="AppleGothic")

# 페이지 제목
st.title("중고차 구매 고객을 위한 정보 제공 서비스")
st.markdown("---")

query_1 = """
SELECT 
    u.yearNum,
    u.total_transactions AS used_transactions,
    a.total_transactions AS all_transactions,
    ROUND(u.total_transactions / a.total_transactions * 100, 2) AS used_ratio_percent
FROM UsedCarData u
JOIN AllCarData a 
    ON u.yearNum = a.yearNum
ORDER BY u.yearNum;
"""
df_1 = Dinput.load_data_to_db(query_1)

df_1["all_transactions_yoy"] = df_1["all_transactions"].pct_change() * 100
df_1["all_transactions_yoy"] = df_1["all_transactions_yoy"].round(2)

# 4️⃣ Streamlit 제목
st.header("📊 자동차 등록 현황 대비 중고차 거래량 전년 대비 증감률 및 비율")

# 5️⃣ Matplotlib 그래프 그리기
fig, ax1 = plt.subplots(figsize=(10, 6))

# 선 그래프 (중고차 거래량)
ax1.plot(df_1["yearNum"], df_1["used_transactions"], marker="o", label="중고차 거래 비율", color="blue")
ax1.set_xlabel("Year")
ax1.set_ylabel("중고차 거래 비율 (%)", color="blue")
ax1.legend(loc="upper left")

# 막대 그래프 (all_transactions 전년 대비 증감률)
ax2 = ax1.twinx()
ax2.bar(df_1["yearNum"], df_1["all_transactions_yoy"], alpha=0.3, color="orange", label="신차 등록 증감율(%)")
ax2.set_ylabel("신차 등록 증감율(%)", color="orange")

# 범례 합치기
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="upper right")

plt.title("신차 등록 증감률 및 중고차 거래 비율 (2015-2023)")
plt.grid(True)

# 6️⃣ Streamlit에 표시
st.pyplot(fig)

st.markdown("신차 등록률이 감소하고 중고차 거래율이 증가하는 현상은, 소비자들이 새 차보다 중고차를 선호하게 되면서 중고차 시장이 점점 더 중요한 자동차 유통 채널로 자리 잡고 있음을 보여줍니다.")

st.markdown("---")

query_2 = """
    SELECT
    c.car_name AS car_name, 
    c.car_brand, 
    c.car_type, 
    c.newcar_price, 
    i.full_name, 
    i.mileage, 
    i.model_year, 
    i.price
FROM CarName c
JOIN CarInfo i ON c.car_name = i.car_name;"""

df_2 = Dinput.load_data_to_db(query_2)
df_2 = Dinput.calculate_value_score(df_2)

df_unique = df_2.sort_values('value_score', ascending=False).drop_duplicates(subset='car_name', keep='first')
top10 = df_unique.head(10)
st.title("가성비 상위 10개 차량")
st.markdown("가성비 점수는 신차 가격 대비 중고차 가격, 연식, 주행 거리, 동일 모델 등록 대수(인기도)를 종합적으로 고려하여 계산되었습니다.")
st.dataframe(top10[['full_name', 'price', 'value_score']].rename(columns={
    'full_name': '차량명',
    'price': '중고차 가격(만원)',
    'value_score': '가성비 점수'
}).style.hide(axis=0))
