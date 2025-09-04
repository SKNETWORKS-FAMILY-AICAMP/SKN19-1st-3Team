import streamlit as st
import pandas as pd
import Data_input as Dinput  # load_data_to_db, calculate_value_score 사용

# --------------------------------------------------------------------------
# --- 데이터 필터링 함수 ---
# --------------------------------------------------------------------------
def filter_car_data(data, brand=None, car_type=None, min_year=None, max_year=None,
                   min_price=None, max_price=None, min_mileage=None, max_mileage=None):
    """조건에 따라 차량 데이터를 필터링하는 함수"""
    filtered_data = data.copy()

    if brand and brand != "전체":
        filtered_data = filtered_data[filtered_data['car_brand'] == brand]

    if car_type and car_type != "전체":
        filtered_data = filtered_data[filtered_data['car_type'] == car_type]

    if min_year:
        filtered_data = filtered_data[filtered_data['model_year'] >= min_year]

    if max_year:
        filtered_data = filtered_data[filtered_data['model_year'] <= max_year]

    if min_price:
        filtered_data = filtered_data[filtered_data['price'] >= min_price]

    if max_price:
        filtered_data = filtered_data[filtered_data['price'] <= max_price]

    if min_mileage:
        filtered_data = filtered_data[filtered_data['mileage'] >= min_mileage]

    if max_mileage:
        filtered_data = filtered_data[filtered_data['mileage'] <= max_mileage]

    return filtered_data


def get_analysis_data(data, analysis_type, group_by):
    """분석 데이터를 생성하는 함수"""
    if analysis_type == "평균 가격":
        return data.groupby(group_by)['price'].mean().reset_index()
    elif analysis_type == "판매 대수":
        return data.groupby(group_by).size().reset_index(name='판매대수')
    elif analysis_type == "평균 주행거리":
        return data.groupby(group_by)['mileage'].mean().reset_index()
    elif analysis_type == "신차-중고차 가격차이":
        result = data.groupby(group_by).agg({
            'newcar_price': 'mean',
            'price': 'mean'
        }).reset_index()
        result['가격차이'] = result['newcar_price'] - result['price']
        return result


# --------------------------------------------------------------------------
# --- 메인 페이지 (차량 검색) ---
# --------------------------------------------------------------------------
def main():
    st.set_page_config(
        page_title="차량 검색",
        page_icon="🔍",
        layout="wide"
    )

    st.title("🔍 차량 검색 및 분석")
    st.markdown("---")

    # DB에서 데이터 로드
    query = """
        SELECT 
            c.car_brand,
            i.car_name,
            c.car_type,
            i.full_name,
            i.model_year,
            i.mileage,
            i.price,
            c.newcar_price
        FROM carname c
        JOIN carinfo i ON c.car_name = i.car_name
        WHERE i.price IS NOT NULL 
        AND i.mileage IS NOT NULL;
    """
    car_data = Dinput.load_data_to_db(query)

    if car_data.empty:
        st.error("데이터를 로드할 수 없습니다.")
        return

    # 세션 상태 초기화
    if 'filtered_results' not in st.session_state:
        st.session_state.filtered_results = pd.DataFrame()
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = pd.DataFrame()
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 0

    # 사이드바 필터
    st.sidebar.header("검색 및 분석 옵션")

    # 브랜드 선택
    brands = ["전체"] + sorted(car_data['car_brand'].unique().tolist())
    selected_brand = st.sidebar.selectbox("브랜드", brands)

    # 차량종류 선택
    if selected_brand != "전체":
        available_types = car_data[car_data['car_brand'] == selected_brand]['car_type'].unique()
    else:
        available_types = car_data['car_type'].unique()

    car_types = ["전체"] + sorted(available_types.tolist())
    selected_type = st.sidebar.selectbox("차량종류", car_types)

    # 연식 범위
    min_year = int(car_data['model_year'].min())
    max_year = int(car_data['model_year'].max())
    year_range = st.sidebar.slider("연식 범위", min_year, max_year, (min_year, max_year))

    # 가격 범위
    min_price = int(car_data['price'].min())
    max_price = int(car_data['price'].max())
    price_range = st.sidebar.slider("가격 범위 (만원)", min_price, max_price, (min_price, max_price))

    # 주행거리 범위
    min_mileage = int(car_data['mileage'].min())
    max_mileage = int(car_data['mileage'].max())
    mileage_range = st.sidebar.slider("주행거리 범위 (km)", min_mileage, max_mileage, (min_mileage, max_mileage))

    st.sidebar.markdown("---")
    st.sidebar.header("분석 옵션")

    # 분석 유형 선택
    analysis_type = st.sidebar.selectbox("분석 유형",
                                       ['브랜드별 분석', '연식별 분석', '차량종류별 분석'])

    # 분석 지표 선택
    if analysis_type == '브랜드별 분석':
        group_by = 'car_brand'
        metric_options = ['평균 가격', '판매 대수', '평균 주행거리', '신차-중고차 가격차이']
    elif analysis_type == '연식별 분석':
        group_by = 'model_year'
        metric_options = ['평균 가격', '판매 대수', '평균 주행거리']
    else:  # 차량종류별 분석
        group_by = 'car_type'
        metric_options = ['평균 가격', '판매 대수', '평균 주행거리', '신차-중고차 가격차이']

    selected_metric = st.sidebar.selectbox('분석 지표', metric_options)

    # 검색 및 분석 실행 버튼
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("검색 실행", type="primary", use_container_width=True):
            filtered_data = filter_car_data(
                car_data,
                brand=selected_brand,
                car_type=selected_type,
                min_year=year_range[0],
                max_year=year_range[1],
                min_price=price_range[0],
                max_price=price_range[1],
                min_mileage=mileage_range[0],
                max_mileage=mileage_range[1]
            )
            if not filtered_data.empty:
                st.session_state.filtered_results = Dinput.calculate_value_score(filtered_data)
            else:
                st.session_state.filtered_results = pd.DataFrame()
            st.session_state.page_number = 0

    with col2:
        if st.button("분석 실행", type="secondary", use_container_width=True):
            filtered_data = filter_car_data(
                car_data,
                brand=selected_brand,
                car_type=selected_type,
                min_year=year_range[0],
                max_year=year_range[1],
                min_price=price_range[0],
                max_price=price_range[1],
                min_mileage=mileage_range[0],
                max_mileage=mileage_range[1]
            )
            if not filtered_data.empty:
                st.session_state.analysis_results = get_analysis_data(filtered_data, selected_metric, group_by)
            else:
                st.session_state.analysis_results = pd.DataFrame()

    # 탭으로 결과 구분
    tab1, tab2 = st.tabs(["🔍 검색 결과", "📊 분석 결과"])

    with tab1:
        st.header("검색 결과")

        if st.session_state.filtered_results.empty:
            st.warning("필터 조건을 설정하고 '검색 실행' 버튼을 눌러주세요.")
        else:
            results = st.session_state.filtered_results

            # 가성비 상위 추천 차량
            if 'value_score' in results.columns:
                st.subheader("🏆 가성비 상위 추천 차량")
                top_recommendations = results.head(5)

                for _, row in top_recommendations.iterrows():
                    with st.container():
                        col1, col2, col3, col4 = st.columns([3, 2, 2.5, 1.5])
                        with col1:
                            st.write(f"**{row['full_name']}**")
                            st.write(f"{row['car_brand']} | {row['car_type']}")
                        with col2:
                            st.metric("가격", f"{row['price']:,}만원")
                        with col3:
                            st.metric("연식", f"{row['model_year']}년")
                            st.metric("주행거리", f"{row['mileage']:,.0f}km")
                        with col4:
                            st.metric("가성비 점수", f"{row['value_score']:.1f}")
                        st.markdown("---")

            st.subheader("전체 검색 결과")

            # 페이지네이션
            items_per_page = 10
            start_idx = st.session_state.page_number * items_per_page
            end_idx = start_idx + items_per_page

            paginated_results = results.iloc[start_idx:end_idx]

            st.info(f"총 {len(results)}대의 차량이 검색되었습니다.")

            if not paginated_results.empty:
                display_columns = ['full_name', 'car_brand', 'car_type', 'model_year', 'mileage', 'price', 'newcar_price']
                if 'value_score' in paginated_results.columns:
                    display_columns.append('value_score')

                formatted_results = paginated_results[display_columns].copy()
                if 'mileage' in formatted_results.columns:
                    formatted_results['mileage'] = formatted_results['mileage'].apply(lambda x: f"{x:,.0f}km")

                st.dataframe(formatted_results, use_container_width=True, hide_index=True)

            total_items = len(results)
            total_pages = (total_items - 1) // items_per_page + 1 if total_items > 0 else 1

            st.markdown(f"페이지: **{st.session_state.page_number + 1} / {total_pages}**")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("이전 페이지", disabled=(st.session_state.page_number <= 0)):
                    st.session_state.page_number -= 1
                    st.rerun()
            with col2:
                if st.button("다음 페이지", disabled=(st.session_state.page_number >= total_pages - 1)):
                    st.session_state.page_number += 1
                    st.rerun()

    with tab2:
        st.header(f"{analysis_type} - {selected_metric}")

        if st.session_state.analysis_results.empty:
            st.warning("분석 조건을 설정하고 '분석 실행' 버튼을 눌러주세요.")
        else:
            analysis_result = st.session_state.analysis_results

            if selected_metric == "평균 가격":
                st.bar_chart(analysis_result.set_index(group_by)['price'])
                st.dataframe(analysis_result, use_container_width=True, hide_index=True)

            elif selected_metric == "판매 대수":
                st.bar_chart(analysis_result.set_index(group_by)['판매대수'])
                st.dataframe(analysis_result, use_container_width=True, hide_index=True)

            elif selected_metric == "평균 주행거리":
                st.bar_chart(analysis_result.set_index(group_by)['mileage'])
                st.dataframe(analysis_result, use_container_width=True, hide_index=True)

            elif selected_metric == "신차-중고차 가격차이":
                st.bar_chart(analysis_result.set_index(group_by)['가격차이'])
                st.dataframe(analysis_result, use_container_width=True, hide_index=True)



main()
