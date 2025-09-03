import csv
import pandas as pd
import mysql.connector

CSV_FILE = "merged_clean.csv"  # 차종, 차량명, 연식, 주행거리, 가격
CSV_FILE2 = "car_name.csv"  # 브랜드, 차종, 차량종류, 신차가격
CSV_FILE3 = "usedcar_data.csv" # 연도, 총거래량

"""
MySQL 연결 설정
db_config = {
    'user    ': 'your_username',    # MySQL 사용자 이름
    'password': 'your_password',    # MySQL 비밀번호
    'host    ': 'localhost',        # MySQL 호스트 (로컬호스트
    'database': 'used_car_db'      # 사용할 데이터베이스 이름
}
"""

### 실행 안되면 encoding 방식 'cp949'로 바꿔보기 ###
def insert_data_to_db():
    # MySQL 데이터베이스 연결
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # car_name.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE2, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO CarName (car_brand, car_name, car_type, newcar_price) VALUES (%s, %s, %s, %s)",
                (row['브랜드'], row['차종'], row['차량종류'], row['신차가격'])
            )

    # kcar_cars.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO CarInfo (car_name, full_name, model_year, mileage, price) VALUES (%s, %s, %s, %s, %s)",
                (row['차종'], row['차량명'], row['연식'], row['주행거리'], row['가격'])
            )

    # usedcar_data.csv 파일 읽기 및 데이터 삽입
    with open(CSV_FILE3, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO UsedCarData (yearNum, total_transactions) VALUES (%s, %s)",
                (row['연도'], row['총거래량'])
            )

    conn.commit()
    cursor.close()
    conn.close()


def load_data_to_db(query):
    # MySQL 데이터베이스 연결
    conn = mysql.connector.connect(**db_config)

    df = pd.read_sql(query, conn)

    conn.close()
    return df