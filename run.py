import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import Data_input as Dinput

plt.rc("font", family="AppleGothic")

# 페이지 제목
st.title("중고차 구매 고려 고객을 위한 정보 제공 서비스")
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
st.title("📊 중고차 거래량 vs 전체 거래량 전년 대비 증감률 및 비율")

# 5️⃣ Matplotlib 그래프 그리기
fig, ax1 = plt.subplots(figsize=(10, 6))

# 선 그래프 (중고차 거래량)
ax1.plot(df_1["yearNum"], df_1["used_transactions"], marker="o", label="Used Transactions", color="blue")
ax1.set_xlabel("Year")
ax1.set_ylabel("Used Transactions")
ax1.legend(loc="upper left")

# 막대 그래프 (all_transactions 전년 대비 증감률)
ax2 = ax1.twinx()
ax2.bar(df_1["yearNum"], df_1["all_transactions_yoy"], alpha=0.3, color="orange", label="All Transactions YoY (%)")
ax2.set_ylabel("All Transactions YoY (%)")

# 범례 합치기
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="upper right")

plt.title("Used Transactions, All Transactions YoY, and Used Ratio (%)")
plt.grid(True)

# 6️⃣ Streamlit에 표시
st.pyplot(fig)

st.markdown("---")

data_options = ['브랜드별 분석', '연식별 분석', '차량 종류별 분석']
selected_option1 = st.selectbox('데이터 옵션을 선택하세요', data_options, key='data_option')

df = None

if selected_option1 == '브랜드별 분석':
    x_label = 'car_brand'
    option_name = None
    option = st.selectbox('확인하고자 하는 분석 데이터를 선택하세요.',['브랜드별 판매 대수', '브랜드별 평균 중고차 가격', '브랜드별 평균 주행 거리', '브랜드별 신차가격 - 중고차가격 비교'])
    if option:
        if option == '브랜드별 판매 대수':
            option_name = option
            y_label = 'COUNT(*)'
            query = """
            SELECT c.car_brand,  COUNT(*),
                    AVG(i.price) AS avg_used_price
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_brand;
            """
        elif option == '브랜드별 평균 중고차 가격':
            option_name = option
            y_label = 'avg_used_price'
            query = """
            SELECT c.car_brand,  COUNT(*),
                    AVG(i.price) AS avg_used_price
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_brand;
            """
        elif option == '브랜드별 평균 주행 거리':
            option_name = option
            y_label = 'avg_mileage'
            query = """
            SELECT c.car_brand,  COUNT(*),
                    AVG(i.mileage) AS avg_mileage
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_brand;
            """
        elif option == '브랜드별 신차가격 - 중고차가격 비교':
            option_name = option
            y_label = 'price_difference'
            query = """
            SELECT c.car_brand,
            AVG(c.newcar_price) AS avg_newcar_price,
            AVG(i.price) AS avg_used_price,
            (AVG(c.newcar_price) - AVG(i.price)) AS price_difference
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_brand;
            """
    df = Dinput.load_data_to_db(query)
elif selected_option1 == '차량 종류별 분석':
    x_label = 'car_type'
    option_name = None
    option = st.selectbox('확인하고자 하는 분석 데이터를 선택하세요.',['차량 종류별 판매 대수', '차량 종류별 평균 중고차 가격', '차량 종류별 평균 주행 거리', '차량 종류별 신차가격 - 중고차가격 비교'])
    if option:
        if option == '차량 종류별 판매 대수':
            option_name = option
            y_label = 'COUNT(*)'
            query = """
            SELECT c.car_type,  COUNT(*),
                    AVG(i.price) AS avg_used_price
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_type;
            """
        elif option == '차량 종류별 평균 중고차 가격':
            option_name = option
            y_label = 'avg_used_price'
            query = """
            SELECT c.car_type,  COUNT(*),
                    AVG(i.price) AS avg_used_price
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_type;
            """
        elif option == '차량 종류별 평균 주행 거리':
            option_name = option
            y_label = 'avg_mileage'
            query = """
            SELECT c.car_type,  COUNT(*),
                    AVG(i.mileage) AS avg_mileage
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_type;
            """
        elif option == '차량 종류별 신차가격 - 중고차가격 비교':
            option_name = option
            y_label = 'price_difference'
            query = """
            SELECT c.car_type,
            AVG(c.newcar_price) AS avg_newcar_price,
            AVG(i.price) AS avg_used_price,
            (AVG(c.newcar_price) - AVG(i.price)) AS price_difference
            FROM CarName c
            JOIN CarInfo i ON c.car_name = i.car_name
            GROUP BY c.car_type;
            """
    df = Dinput.load_data_to_db(query)
elif selected_option1 == '연식별 분석':
    x_label = 'model_year'
    option_name = None
    option = st.selectbox('확인하고자 하는 분석 데이터를 선택하세요.',['연식별 판매 대수', '연식별 평균 중고차 가격', '연식별 평균 주행 거리'])
    if option:
        if option == '연식별 판매 대수':
            option_name = option
            y_label = 'COUNT(*)'
            query = """
            SELECT i.model_year, COUNT(*),
                   AVG(i.price) AS avg_used_price
            FROM CarInfo i
            GROUP BY i.model_year;
            """
        elif option == '연식별 평균 중고차 가격':
            option_name = option
            y_label = 'avg_used_price'
            query = """
            SELECT i.model_year, COUNT(*),
                   AVG(i.price) AS avg_used_price
            FROM CarInfo i
            GROUP BY i.model_year;
            """
        elif option == '연식별 평균 주행 거리':
            option_name = option
            y_label = 'avg_mileage'
            query = """
            SELECT i.model_year, COUNT(*),
                   AVG(i.mileage) AS avg_mileage
            FROM CarInfo i
            GROUP BY i.model_year;
            """
    df = Dinput.load_data_to_db(query)



if df is not None and not df.empty:
    st.subheader(option_name)
    st.bar_chart(data=df, x=x_label, y=y_label)

    # 2️⃣ 평균 가격 그래프 (Bar Chart)
    # st.subheader("브랜드별 평균 중고차 가격")
    # st.bar_chart(data=df, x="car_brand", y=y_label)

    # # 3️⃣ Matplotlib 활용 (두 값 비교를 한 그래프에)
    # st.subheader("판매 대수 & 평균 가격 비교 (Matplotlib)")

    # fig, ax1 = plt.subplots(figsize=(8,5))

    # # 왼쪽 y축: 판매 대수
    # ax1.bar(df["car_brand"], df["COUNT(*)"], color="skyblue", alpha=0.7, label="판매 대수")
    # ax1.set_ylabel("판매 대수", color="skyblue")
    # ax1.tick_params(axis="y", labelcolor="skyblue")

    # # 오른쪽 y축: 평균 가격
    # ax2 = ax1.twinx()
    # ax2.plot(df["car_brand"], df["avg_used_price"], color="red", marker="o", label="평균 가격")
    # ax2.set_ylabel("평균 중고차 가격", color="red")
    # ax2.tick_params(axis="y", labelcolor="red")

    # # 그래프 출력
    # st.pyplot(fig)