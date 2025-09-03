import csv
import pandas as pd
import mysql.connector

CSV_FILE = "merged_clean.csv"  # 차종, 차량명, 연식, 주행거리, 가격
CSV_FILE2 = "car_name.csv"  # 브랜드, 차종, 차량종류, 신차가격
CSV_FILE3 = "usedcar_data.csv" # 연도, 총거래대수
CSV_FILE4 = "AllCarData.csv" # 연도, 총거래량
CSV_FILE5 = "kia_faq.csv"  # category, question, answer, site(선택)
CSV_FILE6 = "hyundai_faq.csv"  # category, question, answer, site(선택)

# MySQL 연결 설정
db_config = {
    'user': 'Park',    # MySQL 사용자 이름
    'password': 'Park',    # MySQL 비밀번호
    'host': 'localhost',        # MySQL 호스트 (로컬호스트
    'database': 'used_car_db',      # 사용할 데이터베이스 이름
    'auth_plugin': 'mysql_native_password'  # 인증 플러그인 설정
}


### 실행 안되면 encoding 방식 'cp949'로 바꿔보기 ###
def insert_data_to_db():
    # MySQL 데이터베이스 연결
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # car_name.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE2, mode='r', encoding='cp949') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT IGNORE INTO CarName (car_brand, car_name, car_type, newcar_price) VALUES (%s, %s, %s, %s)",
                (row['브랜드'], row['차종'], row['차량종류'], int(row['신차가격']))
            )
    print("car_name.csv data inserted successfully.")



    # kcar_cars.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT IGNORE INTO CarInfo (car_name, full_name, model_year, mileage, price) VALUES (%s, %s, %s, %s, %s)",
                (row['차종'], row['차량명'], row['연식'], row['주행거리'], row['가격'])
            )
    print("kcar_cars.csv data inserted successfully.")

    # usedcar_data.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE3, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT IGNORE INTO UsedCarData (yearNum, total_transactions) VALUES (%s, %s)",
                (row['연도'], row['총거래대수'])
            )
    print("usedcar_data.csv data inserted successfully.")

    # AllCarData.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE4, mode='r', encoding='cp949') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT IGNORE INTO AllCarData (yearNum, total_transactions) VALUES (%s, %s)",
                (row['연도'], row['총거래대수'])
            )
    print("AllCarData.csv data inserted successfully.")

    conn.commit()
    cursor.close()
    conn.close()


def load_data_to_db(query):
    # MySQL 데이터베이스 연결
    conn = mysql.connector.connect(**db_config)

    df = pd.read_sql(query, conn)

    conn.close()
    return df

def insert_faq_data_to_db():
    # MySQL 데이터베이스 연결
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    with open(CSV_FILE5, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT IGNORE INTO car_faq (category, question, answer, site) VALUES (%s, %s, %s, %s)",
                (row['category'], row['question'], row['answer'], row.get('site'))  # site 컬럼은 없을 수 있으니 get 사용
            )
    with open(CSV_FILE6, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT IGNORE INTO car_faq (category, question, answer, site) VALUES (%s, %s, %s, %s)",
                (row['category'], row['question'], row['answer'], row.get('site'))  # site 컬럼은 없을 수 있으니 get 사용
            )
    print("FAQ data inserted successfully.")
    
    conn.commit()
    cursor.close()
    conn.close()

def calculate_value_score(df):
    """차량의 가성비 점수를 계산하는 함수"""
    df_copy = df.copy()
    
    # 필요한 컬럼이 있는지 확인
    required_columns = ['신차가격', '가격', '연식', '주행거리', '차종']
    if not all(col in df_copy.columns for col in required_columns):
        return df_copy
    
    # 현재 연도 (2024년 기준)
    current_year = 2024
    
    # 1. 신차 대비 중고차 가격 비율 (낮을수록 좋음, 0-1)
    df_copy['price_ratio'] = df_copy['가격'] / df_copy['신차가격']
    
    # 2. 차량 연령 점수 (최근 연식일수록 좋음, 0-1)
    max_age = current_year - df_copy['연식'].min()
    df_copy['age_score'] = 1 - ((current_year - df_copy['연식']) / max_age)
    
    # 3. 주행거리 점수 (적을수록 좋음, 0-1)
    max_mileage = df_copy['주행거리'].max()
    df_copy['mileage_score'] = 1 - (df_copy['주행거리'] / max_mileage)
    
    # 4. 차종별 인기도 점수 (같은 차종 등록 대수가 많을수록 좋음, 0-1)
    car_popularity = df_copy['차종'].value_counts()
    max_popularity = car_popularity.max()
    df_copy['popularity_score'] = df_copy['차종'].map(car_popularity) / max_popularity
    
    # 전체 가성비 점수 계산 (가중평균)
    df_copy['value_score'] = (
        (1 - df_copy['price_ratio']) * 0.35 +  # 가격 비율 (35%)
        df_copy['age_score'] * 0.25 +          # 연식 점수 (25%)
        df_copy['mileage_score'] * 0.25 +      # 주행거리 점수 (25%)
        df_copy['popularity_score'] * 0.15     # 인기도 점수 (15%)
    ) * 100  # 100점 만점으로 변환
    
    return df_copy
    
if __name__ == "__main__":
    insert_data_to_db()
    insert_faq_data_to_db()