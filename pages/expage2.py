import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import Data_input as Dinput

plt.rc("font", family="AppleGothic")

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