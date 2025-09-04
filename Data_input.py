import csv
import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

CSV_FILE = "merged_clean.csv"  # 차종, 차량명, 연식, 주행거리, 가격
CSV_FILE2 = "car_name.csv"  # 브랜드, 차종, 차량종류, 신차가격
CSV_FILE3 = "usedcar_data.csv" # 연도, 총거래대수
CSV_FILE4 = "AllCarData.csv" # 연도, 총거래량
CSV_FILE5 = "kia_faq.csv"  # category, question, answer, site(선택)
CSV_FILE6 = "hyundai_faq.csv"  # category, question, answer, site(선택)

load_dotenv()  # .env 파일에서 환경 변수 로드
# MySQL 연결 설정
db_config = {
    'user': os.getenv("DATABASE_USER"),             # MySQL 사용자 이름
    'password': os.getenv("DATABASE_PASSWORD"),         # MySQL 비밀번호
    'host': os.getenv("HOST"),        # MySQL 호스트 (로컬호스트
    'database': 'used_car_db'   # 사용할 데이터베이스 이름
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
                "INSERT INTO CarName (car_brand, car_name, car_type, newcar_price) VALUES (%s, %s, %s, %s)",
                (row['브랜드'], row['차종'], row['차량종류'], row['신차가격'])
            )
    print("car_name.csv data inserted successfully.")



    # kcar_cars.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO CarInfo (car_name, full_name, model_year, mileage, price) VALUES (%s, %s, %s, %s, %s)",
                (row['차종'], row['차량명'], row['연식'], row['주행거리'], row['가격'])
            )
    print("kcar_cars.csv data inserted successfully.")

    # usedcar_data.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE3, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO UsedCarData (yearNum, total_transactions) VALUES (%s, %s)",
                (row['연도'], row['총거래대수'])
            )
    print("usedcar_data.csv data inserted successfully.")

    # AllCarData.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE4, mode='r', encoding='cp949') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO AllCarData (yearNum, total_transactions) VALUES (%s, %s)",
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


def calculate_value_score(df: pd.DataFrame,
    w_price=0.4, w_year=0.2, w_mileage=0.3, w_count=0.1) -> pd.DataFrame:
    """
    CarName + CarInfo JOIN 결과 DataFrame에서 가성비 점수를 계산하고 반환합니다.
    
    df 컬럼:
    - 'car_name', 'full_name', 'price', 'model_year', 'mileage', 'newcar_price'
    
    반환:
    - 기존 컬럼 + 'model_count', 'price_saving', 'year_score', 'mileage_score', 'count_score', 'value_score'
    """
    
    df = df.copy()
    
    # 동일 모델 등록 대수
    df['model_count'] = df.groupby('car_name')['car_name'].transform('count')
    
    # 정규화 점수 계산
    df['price_saving'] = (df['newcar_price'] - df['price']) / df['newcar_price']
    df['year_score'] = (df['model_year'] - df['model_year'].min()) / (df['model_year'].max() - df['model_year'].min())
    df['mileage_score'] = 1 - (df['mileage'] - df['mileage'].min()) / (df['mileage'].max() - df['mileage'].min())
    df['count_score'] = (df['model_count'] - df['model_count'].min()) / (df['model_count'].max() - df['model_count'].min())
    
    # 종합 가성비 점수
    df['value_score'] = ((
        w_price * df['price_saving'] +
        w_year * df['year_score'] +
        w_mileage * df['mileage_score'] +
        w_count * df['count_score']
    )*100)
    
    # 점수 내림차순 정렬
    df = df.sort_values(by='value_score', ascending=False).reset_index(drop=True)
    
    return df

### 실행 안되면 encoding 방식 'cp949'로 바꿔보기 ###
def insert_faq_data_to_db():
    # MySQL 데이터베이스 연결
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    with open(CSV_FILE5, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO car_faq (category, question, answer, site) VALUES (%s, %s, %s, %s)",
                (row['category'], row['question'], row['answer'], row.get('site'))  # site 컬럼은 없을 수 있으니 get 사용
            )
    with open(CSV_FILE6, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['category'].strip()
            question = row['question'].strip()

            # question이 category로 시작하면 제거
            if question.startswith(category):
                question = question[len(category):].strip()

            cursor.execute(
                "INSERT INTO car_faq (category, question, answer, site) VALUES (%s, %s, %s, %s)",
                (category, question, row['answer'], row.get('site'))  # site 컬럼은 없을 수 있으니 get 사용
            )
    print("FAQ data inserted successfully.")
    
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    insert_data_to_db()