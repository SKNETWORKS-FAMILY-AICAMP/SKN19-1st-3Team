중고차 시장 분석 및 차량 정보 조회 플랫폼
본 프로젝트는 국내 자동차 시장 데이터를 기반으로 시장 동향을 분석하고, 사용자가 원하는 차량 정보를 손쉽게 조회할 수 있는 Streamlit 기반의 웹 애플리케이션입니다.

팀 프로필
<table>
<tr>
<td align="center" width="200">
<img src="https://via.placeholder.com/150" width="150" height="150" style="border-radius: 50%;" alt="박준영"/>
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
<img src="https://via.placeholder.com/150" width="150" height="150" style="border-radius: 50%;" alt="정종현"/>
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
<img src="https://via.placeholder.com/150" width="150" height="150" style="border-radius: 50%;" alt="김진"/>
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
<img src="https://i.ibb.co/M5m6M0Y/streamlit.png" width="150" height="150" style="border-radius: 50%;" alt="김지훈"/>
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

목차
주요 기능

기술 스택

프로젝트 실행 방법

<br>

주요 기능
프로젝트는 총 3개의 주요 페이지로 구성되어 있으며, 각 페이지는 다음과 같은 기능을 제공합니다.

1. 시장 분석 대시보드
데이터 시각화를 통해 국내 자동차 시장의 트렌드를 다각적으로 분석하고 인사이트를 제공합니다.

브랜드 별 분석: 주요 자동차 브랜드의 시장 점유율, 신차와 중고차의 평균 가격 비교 분석을 제공합니다.

연식 별 분석: 차량의 연식에 따른 감가상각 및 중고차 시장 가격 변화 추이를 분석합니다.

차량 종류 별 분석: 세단, SUV, 트럭 등 차종 별 판매 대수, 평균 중고차 가격, 평균 주행 거리 데이터를 시각화하여 제공합니다.

2. 차량 정보 조회 시스템
데이터베이스에 저장된 차량의 상세 정보를 사용자가 직접 검색하고 확인할 수 있는 시스템입니다.

계층적 검색: 사용자는 '브랜드'를 먼저 선택한 후, 해당 브랜드에 속한 '모델'을 선택하는 방식으로 손쉽게 원하는 차종을 찾을 수 있습니다.

상세 정보 제공: 검색된 차량의 모델명, 풀네임, 연비, 가격, 연도 등 5가지 핵심 정보와 함께 차량 이미지를 시각적으로 보기 쉬운 UI로 제공합니다.

3. 제조사별 FAQ
사용자들이 차량 구매 및 유지보수 시 자주 묻는 질문들을 모아 제공하는 정보 페이지입니다.

신뢰성 있는 정보: 현대자동차와 기아의 공식 웹사이트에서 자주 묻는 질문(FAQ) 데이터를 크롤링하여 정확하고 신뢰도 높은 정보를 제공합니다.

통합된 정보 제공: 여러 곳에 흩어져 있는 정보를 한곳에 모아 Streamlit 페이지를 통해 사용자가 편리하게 조회할 수 있도록 구성합니다.

<br>

기술 스택
언어: Python

프레임워크: Streamlit

데이터 처리: Pandas

데이터베이스: SQLite

<br>

프로젝트 실행 방법
저장소 복제

git clone [저장소 URL]
cd [프로젝트 폴더]

필요한 라이브러리 설치

pip install -r requirements.txt

(만약 requirements.txt 파일이 없다면 아래 명령어를 사용하세요)

pip install streamlit pandas

Streamlit 애플리케이션 실행

streamlit run app.py
