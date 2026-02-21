import streamlit as st
import pandas as pd
import plotly.express as px

# Саҳифа созламалари
st.set_page_config(page_title="AI Inventory Management", layout="wide")

st.title("📦 AI-асосидаги Заҳираларни Бошқариш Тизими")
st.sidebar.header("Фильтрлар")

# 1. Маълумотларни юклаш
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/forecast_results.csv', index_col=0)
    df.index = pd.to_datetime(df.index)
    return df

try:
    data = load_data()

    # 2. Sidebar фильтрлари
    selected_store = st.sidebar.selectbox("Дўконни танланг:", sorted(data['store_id'].unique()))
    selected_item = st.sidebar.selectbox("Маҳсулотни танланг:", sorted(data['item_id'].unique()))

    # Фильтрланган маълумот
    filtered_df = data[(data['store_id'] == selected_store) & (data['item_id'] == selected_item)].tail(30)

    # 3. Асосий кўрсаткичлар (Metrics)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Умумий аниқлик (Accuracy)", "88.52%")
    with col2:
        st.metric("Ўртача хатолик (MAE)", "2.73")
    with col3:
        st.metric("Stockout Risk", "3.20%")

    # 4. График: Сотув ва Башорат солиштирмаси
    st.subheader(f"{selected_store} - {selected_item} учун сотувлар динамикаси")
    fig = px.line(filtered_df, x=filtered_df.index, y=['sales', 'forecast'],
                  labels={'value': 'Дона', 'index': 'Сана'},
                  title="Ҳақиқий сотув ва Модель башорати")
    st.plotly_chart(fig, use_container_width=True)

    # 5. Буюртма Тавсияси Жадвали
    st.subheader("📅 Келаси давр учун харид режаси")
    order_table = filtered_df[['forecast', 'safety_stock', 'order_recommendation']].tail(7)
    st.table(order_table)

    # 6. Бюджет ҳисоби (Сиз айтган 53.99 ўртача нарх билан)
    total_order = order_table['order_recommendation'].sum()
    st.info(f"💡 Ушбу маҳсулот бўйича келаси 7 кунлик жами буюртма: **{total_order} дона**")

except FileNotFoundError:
    st.error("Башорат файли топилмади. Аввал 'scripts/model_inference.py' ни юргизинг.")