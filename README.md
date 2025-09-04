#  중고 자동차 정보 조회 시스템

 **데이터 기반 중고차 구매 의사결정 지원 플랫폼**  
 Streamlit 기반 웹 애플리케이션으로 중고차 시장 분석과 실시간 정보 조회 서비스

<br>

##  팀 프로필
<table>
<tr>
<td align="center" width="200" style="vertical-align: top; height: 300px;">
<img src="images/yeon.jpg" width="150" height="150" style="border-radius: 50%; object-fit: cover;" alt="박준영"/>
<br />
<h3 style="margin: 10px 0 5px 0;">박준영</h3>
<p style="margin: 5px 0;">?</p>
<div style="margin-top: 10px;">
<a href="https://github.com/deneb784">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<br />
<a href="mailto:deneb784@gmail.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</div>
</td>
<td align="center" width="200" style="vertical-align: top; height: 300px;">
<img src="images/jong.png" width="150" height="150" style="border-radius: 50%; object-fit: cover;" alt="정종현"/>
<br />
<h3 style="margin: 10px 0 5px 0;">정종현</h3>
<p style="margin: 5px 0;">?</p>
<div style="margin-top: 10px;">
<a href="https://github.com/myem21">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<br />
<a href="mailto:myem21@gmail.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</div>
</td>
<td align="center" width="200" style="vertical-align: top; height: 300px;">
<img src="images/jin.png" width="150" height="150" style="border-radius: 50%; object-fit: cover;" alt="김진"/>
<br />
<h3 style="margin: 10px 0 5px 0;">김진</h3>
<p style="margin: 5px 0;">?</p>
<div style="margin-top: 10px;">
<a href="https://github.com/KIMjjjjjjjj">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<br />
<a href="mailto:jin432101@gmail.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</div>
</td>
<td align="center" width="200" style="vertical-align: top; height: 300px;">
<img src="images/hun.jpg" width="150" height="150" style="border-radius: 50%; object-fit: cover;" alt="김지훈"/>
<br />
<h3 style="margin: 10px 0 5px 0;">김지훈</h3>
<p style="margin: 5px 0;">?</p>
<div style="margin-top: 10px;">
<a href="https://github.com/ddeeqq">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<br />
<a href="mailto:jihanki3@naver.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</div>
</td>
</tr>
</table>

<br>

---

##  프로젝트 개요

중고 자동차 구매를 고려하는 사용자들에게 **데이터 기반의 인사이트**와 **실시간 차량 정보**를 제공하는 종합 플랫폼입니다.

###  핵심 가치
- **데이터 기반 분석**: 브랜드별, 연식별, 차종별 심층 분석
- **실시간 정보**: 최신 중고차 시장 데이터 제공  
- **가성비 분석**: 독자적 알고리즘을 통한 가성비 지수 계산
- **사용자 친화적**: 직관적 UI/UX를 통한 쉬운 정보 접근

<br>

---

##  시스템 아키텍처

### ERD (Entity Relationship Diagram)
<!-- ERD 이미지 자리 -->

<br>

---

##  주요 기능

###  1페이지: 메인 대시보드 & 가성비 분석
- **시장 트렌드 분석**
  - 자동차 등록 현황 vs 중고차 거래량 비교 시각화
  - 전년 대비 증감률 및 시장 동향 분석
  - 중고차 시장 성장세와 중요성 데이터 제시

- **가성비 TOP 10 차량 추천**
  - 독자적 가성비 지수 (100점 만점) 계산 알고리즘
  - 신차 가격 대비 중고차 가격, 연식, 주행거리, 인기도 종합 분석
  - 실시간 업데이트되는 추천 리스트

###  2페이지: 차량 조회 & 분석
- **고급 검색 필터링**
  - 브랜드, 차종, 연식, 가격, 주행거리별 다중 필터링
  - 실시간 검색 결과 및 페이지네이션 지원

- **데이터 분석 대시보드**
  - 브랜드별/연식별/차량종류별 통계 분석
  - 평균 가격, 판매 대수, 주행거리 비교
  - 신차-중고차 가격차이 분석
  - 인터랙티브 차트를 통한 시각화

###  3페이지: 통합 FAQ 시스템
- **멀티 브랜드 FAQ 지원**
  - 현대자동차, 기아자동차 공식 FAQ 통합
  - 카테고리별 분류 및 실시간 검색 기능
  - 키워드 하이라이팅으로 향상된 가독성

<br>

---

##  기술 스택

### Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Backend & Database
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### Data Processing & Analysis
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)

### Web Scraping
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

<br>

---

## 📁 프로젝트 구조

```
SKN19-1st-3Team/
├── 📄 메인_페이지.py              # 메인 대시보드 (가성비 분석)
├── 📄 2_조회_및_분석.py           # 차량 검색 및 데이터 분석
├── 📄 3_FAQ.py                   # 통합 FAQ 시스템
├── 📊 Data_input.py              # 데이터베이스 연동 모듈
├── 🔧 Data_Preprocessing.py      # 데이터 전처리 모듈
├── 🕷️ Crawling_data_KCar.py     # K-Car 중고차 데이터 크롤링
├── 🕷️ Crawling_data_Hyundai_FAQ.py  # 현대차 FAQ 크롤링
├── 🕷️ Crawling_data_Kia_FAQ.py      # 기아차 FAQ 크롤링
├── 🗄️ DB making.sql             # 데이터베이스 스키마
├── 🖼️ images/                   # 팀원 프로필 이미지
│   ├── yeon.jpg
│   ├── jong.png
│   ├── jin.png
│   └── hun.jpg
├── 📊 data/                      # 데이터 파일들
│   ├── merged_clean.csv          # 정제된 중고차 데이터
│   ├── car_name.csv             # 차량 기본 정보
│   ├── usedcar_data.csv         # 중고차 거래량 데이터
│   ├── AllCarData.csv           # 전체 차량 등록 데이터
│   ├── hyundai_faq.csv          # 현대차 FAQ
│   └── kia_faq.csv              # 기아차 FAQ
├── ⚙️ .env                       # 환경변수 설정
├── 🚫 .gitignore                # Git 제외 파일
└── 📖 README.md
```

<br>

---

##  데이터베이스 설계

### 주요 테이블 구조

#### CarName 테이블
```sql
CREATE TABLE CarName (
    car_name VARCHAR(50) PRIMARY KEY,
    car_brand VARCHAR(50) NOT NULL,
    car_type ENUM('경차', '승용차', 'SUV', '승합차', '트럭'),
    newcar_price INT NOT NULL
);
```

#### CarInfo 테이블  
```sql
CREATE TABLE CarInfo (
    car_ID INT AUTO_INCREMENT PRIMARY KEY,
    car_name VARCHAR(50),
    full_name VARCHAR(100) NOT NULL,
    mileage INT,
    model_year INT,
    price INT NOT NULL,
    FOREIGN KEY (car_name) REFERENCES CarName(car_name)
);
```

#### car_faq 테이블
```sql
CREATE TABLE car_faq (
    faq_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    site VARCHAR(100)
);
```

<br>

---


### 가성비 점수 산출 공식

```python
def calculate_value_score(df, w_price=0.4, w_year=0.2, w_mileage=0.3, w_count=0.1):
    # 정규화 점수 계산
    df['price_saving'] = (df['newcar_price'] - df['price']) / df['newcar_price']
    df['year_score'] = (df['model_year'] - df['model_year'].min()) / (df['model_year'].max() - df['model_year'].min())
    df['mileage_score'] = 1 - (df['mileage'] - df['mileage'].min()) / (df['mileage'].max() - df['mileage'].min())
    df['count_score'] = (df['model_count'] - df['model_count'].min()) / (df['model_count'].max() - df['model_count'].min())
    
    # 종합 가성비 점수 (100점 만점)
    df['value_score'] = (w_price * df['price_saving'] + w_year * df['year_score'] + 
                        w_mileage * df['mileage_score'] + w_count * df['count_score']) * 100
```

### 평가 지표
- **가격 절약률 (40%)**: 신차 대비 중고차 가격 할인율
- **연식 점수 (20%)**: 차량의 상대적 신식도
- **주행거리 점수 (30%)**: 주행거리 대비 차량 상태
- **인기도 점수 (10%)**: 동일 모델 등록 대수

<br>

---

##  주요 분석 기능

### 시장 트렌드 분석
- 신차 등록량 vs 중고차 거래량 추세 비교
- 전년 대비 증감률 시각화
- 중고차 시장 점유율 변화

### 브랜드별 분석
- 브랜드별 평균 중고차 가격
- 신차-중고차 가격차이 분석
- 브랜드별 중고차 등록 대수

### 차량 종류별 분석  
- 경차, 승용차, SUV, 승합차, 트럭별 통계
- 차종별 가격 분포 및 선호도
- 연식별 가치 하락률 분석

<br>
