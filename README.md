# 중고 자동차 정보 조회 시스템

국내 차량의 종합적인 정보를 제공하는 Streamlit 기반 시스템

## 팀 프로필
<table>
<tr>
<td align="center" width="200">
<img src="images/yeon.jpg" width="150" height="150" style="border-radius: 50%;" alt="박준영"/>
<br />
<h3>박준영</h3>
<p>역할: </p>
<a href="https://github.com/deneb784">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<a href="mailto:deneb784@gmail.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</td>
<td align="center" width="200">
<img src="images/jong.png" width="150" height="150" style="border-radius: 50%;" alt="정종현"/>
<br />
<h3>정종현</h3>
<p>역할: </p>
<a href="https://github.com/myem21">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<a href="mailto:myem21@gmail.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</td>
<td align="center" width="200">
<img src="images/jin.png" width="150" height="150" style="border-radius: 50%;" alt="김진"/>
<br />
<h3>김진</h3>
<p>역할: </p>
<a href="https://github.com/KIMjjjjjjjj">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<a href="mailto:jin432101@gmail.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</td>
<td align="center" width="200">
<img src="images/hun.jpg" width="150" height="150" style="border-radius: 50%;" alt="김지훈"/>
<br />
<h3>김지훈</h3>
<p>역할: </p>
<a href="https://github.com/ddeeqq">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
</a>
<a href="mailto:jihanki3@naver.com">
<img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=Gmail&logoColor=white"/>
</a>
</td>
</tr>
</table>

<br>

## 프로젝트 개요

중고 자동차 구매를 고려하는 사용자들에게 브랜드별, 연식별, 차종별 분석 데이터와 실시간 차량 정보 조회 기능을 제공합니다. 또한 현대와 기아 공식 웹사이트에서 수집한 FAQ 정보도 함께 제공하여 종합적인 자동차 정보 플랫폼을 구성합니다.

## 주요 기능

### 1페이지: 메인 페이지 및 가성비 차량 소개
- 자동차 등록 현황 대비 중고차 거래량 전년 대비 증감률 및 비율
  - 신차 등록율은 감소하고, 중고차 거래율은 증가하고 있음을 표시
  - 중고차 시장의 중요성이 더 높아지고 있음을 보임
  - 중고차 구매 고려 인원에게 좋은 정보를 제공하고 있음을 설명

- 가성비 top10 자동차 출력
  - 신차 가격 대비 중고차 가격, 연식, 주행 거리, 동일 모델 등록 대수(인기도)를 기반으로 가성비 지수를 계산
  - 가성비 지수 (100점 만점) 기준으로, 가성비 지수가 가장 높은 차종 10개를 출력

### 2페이지: 차량 정보 조회
- 데이터베이스 연동을 통한 실시간 차량 정보 검색
- 브랜드 및 모델별 필터링 기능
- 페이지네이션을 통한 효율적인 결과 표시
- 차량별 상세 정보 (가격, 연비, 연도, 이미지)

### 3페이지: FAQ
- 현대자동차 공식 웹사이트 크롤링 데이터
- 기아자동차 공식 웹사이트 크롤링 데이터
- 카테고리별 FAQ 분류 및 검색 기능

## 기술 스택

- **Frontend**: Streamlit
- **Backend**: Python
- **Data Processing**: Pandas
- **Database**: PostgreSQL/MySQL (구성 예정)
- **Web Scraping**: BeautifulSoup/Selenium
- **Data Visualization**: Plotly/Matplotlib

## 프로젝트 구조

```
car-info-system/
├── app.py                  # 메인 애플리케이션 파일
├── pages/
│   ├── analysis.py        # 데이터 분석 대시보드
│   ├── search.py          # 차량 검색 페이지
│   └── faq.py            # FAQ 페이지
├── data/
│   ├── scraped_faq.py    # FAQ 크롤링 모듈
│   └── database.py       # DB 연결 설정
├── utils/
│   └── helpers.py        # 유틸리티 함수들
├── requirements.txt       # 의존성 패키지
└── README.md
```

## 설치 및 실행

### 사전 요구사항
- Python 3.8 이상
- pip 패키지 매니저

### 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/your-username/car-info-system.git
cd car-info-system
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 실행 방법

```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 접속하여 애플리케이션을 사용할 수 있습니다.

## 개발 현황

### 완료된 기능
- 차량 검색 페이지 기본 구조
- 샘플 데이터를 활용한 검색 및 필터링
- 페이지네이션 구현
- 반응형 UI 레이아웃

### 개발 예정
- **1페이지**: 데이터 분석 대시보드
  - 브랜드별/연식별/차종별 통계 분석
  - 인터랙티브 차트 및 그래프
  - 신차-중고차 가격 비교 시각화
- **3페이지**: FAQ 시스템
  - 현대/기아 웹사이트 크롤링 구현
  - FAQ 데이터 구조화 및 검색 기능
- **데이터베이스 연동**
  - 실제 DB 스키마 설계
  - API 연동 및 데이터 파이프라인 구축

### 수정 포인트

코드 내 다음 섹션들을 통해 쉬운 커스터마이징이 가능합니다:

- **수정 포인트 1**: 실제 데이터베이스 연결 설정
- **수정 포인트 2**: DB 조회 쿼리 작성
- **수정 포인트 3**: UI 커스터마이징 (페이지당 아이템 수 등)
- **수정 포인트 4**: 결과 카드 레이아웃 변경

## 데이터 구조

### 차량 정보 테이블
```sql
CREATE TABLE car_info (
    id INT PRIMARY KEY,
    브랜드 VARCHAR(50),
    모델명 VARCHAR(100),
    풀네임 VARCHAR(200),
    연비 DECIMAL(5,2),
    가격 INT,
    연도 INT,
    이미지_URL VARCHAR(500)
);
```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
