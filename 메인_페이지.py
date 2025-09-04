import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import Data_input as Dinput
import platform



# 메인 페이지
# - 신차 등록 현황 대비 중고차 거래량 전년 대비 증감률 및 비율 그래프
# - 가성비 상위 10개 차량 순위표


# OS별 폰트 설정
if platform.system() == "Windows":
    plt.rc("font", family="Malgun Gothic")  # Windows
elif platform.system() == "Darwin":
    plt.rc("font", family="AppleGothic")   # macOS

# 메인 페이지 제목
st.title("중고차 구매 고객을 위한 정보 제공 서비스")
st.markdown("---")

# 등록 현황 데이터 로드
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

### 그래프 출력----------------------------

st.header("📊 자동차 등록 현황 대비 중고차 거래량 전년 대비 증감률 및 비율")
st.text('')

fig, ax1 = plt.subplots(figsize=(10, 6))

# 선 그래프 (중고차 거래량)
ax1.plot(df_1["yearNum"], df_1["used_transactions"], marker="o", label="중고차 거래 비율", color="blue")
ax1.set_xlabel("Year")
ax1.set_ylabel("중고차 거래 비율 (%)", color="blue")
ax1.legend(loc="upper left")

# 막대 그래프 (전체 차 전년 대비 증감률)
ax2 = ax1.twinx()
ax2.bar(df_1["yearNum"], df_1["all_transactions_yoy"], alpha=0.3, color="orange", label="신차 등록 증감율(%)")
ax2.set_ylabel("신차 등록 증감율(%)", color="orange")

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="upper right")

plt.title("신차 등록 증감률 및 중고차 거래 비율 (2015-2023)")
plt.grid(True)
st.pyplot(fig)

### --------------------------------------

# 설명 박스
st.markdown("""
<div style="
    padding:20px; 
    border-radius:12px; 
    background-color:#f0f8ff; 
    border-left:6px solid #1f77b4;
    font-size:18px; 
    line-height:1.5;
    color:black;
">
    최근 <strong style="color:#ff5733;">중고차 시장의 활성화</strong>와 더불어 
    많은 소비자들이 중고차를 찾고 있습니다.<br>
    해당 페이지를 통해 6000개가 넘는 매물 중 <strong style="color:#1f77b4;">원하는 매물</strong>을 
    쉽게 찾아보세요.
</div>
""", unsafe_allow_html=True)


st.markdown("---")

# 가성비 순위 데이터 로드
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
top10 = top10[['full_name', 'price', 'value_score']].rename(columns={
    'full_name': '차량명',
    'price': '중고차 가격',
    'value_score': '가성비 점수'
})

# 순위표 출력 -----------------------------
count = 1   # 순위
for _, car in top10.iterrows():

    if car['가성비 점수'] >= 70:
        score_color = 'green'
    elif car['가성비 점수'] >= 50:
        score_color = 'orange'
    else:
        score_color = 'red'
    
    bg_color = "#ffffff"
    icon = ""
    icon_size = "0px"

    if count == 1:
        icon = "🥇"
        bg_color = "#ffea8c"
        icon_size = "64px"
    elif count == 2:
        icon = "🥈"
        bg_color = "#cdcdcd"
        icon_size = "64px"
    elif count == 3:
        icon = "🥉"
        bg_color = "#ffe0ae"
        icon_size = "64px"

    st.markdown(f"""
    <div style="
        display: flex; 
        align-items: center; 
        padding:15px; 
        margin:10px 0; 
        border-radius:12px; 
        background-color:{bg_color}; 
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    ">
        <div style="font-size:{icon_size}; margin-right:15px;">{icon}</div>
        <div>
            <h3 style="color:#1f77b4; margin-bottom:5px;">{str(count) + ". " + car['차량명']}</h3>
            <p style="font-size:24px; color:#1f77b4; margin:0;">
                <strong>{car['중고차 가격']:,} 만원</strong>
            </p>
            <p style="font-size:32px; margin:0; color:{score_color};">
                가성비 점수: <strong>{car['가성비 점수']:.2f}</strong>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    count += 1


### -------------------------------------