import streamlit as st

from src.data_loader import load_messi_data
from src.forecasting import forecast_goat_index
from src.valuation import estimate_intrinsic_value
from src.visuals import (
    plot_forecast,
    plot_goat_index,
    plot_surplus_value,
    plot_value_comparison,
)


st.set_page_config(
    page_title="Messi the Goat",
    page_icon="M",
    layout="wide",
)


@st.cache_data
def get_dashboard_data():
    """Load and enrich the dashboard dataset."""
    raw_df = load_messi_data()
    valued_df = estimate_intrinsic_value(raw_df)
    forecast_df = forecast_goat_index(valued_df, years_ahead=3)
    return valued_df, forecast_df


df, forecast = get_dashboard_data()

st.title("Messi the Goat")
st.write(
    "This app looks at Messi's seasons and gives each one a simple score. "
    "It also makes a rough value estimate and a short forecast for the next "
    "few years."
)

peak_row = df.loc[df["goat_index"].idxmax()]
value_row = df.loc[df["intrinsic_value_m"].idxmax()]

metric_cols = st.columns(4)
metric_cols[0].metric("Best Scored Season", peak_row["season"], f"{peak_row['goat_index']:.2f}")
metric_cols[1].metric(
    "Highest Model Value",
    value_row["season"],
    f"${value_row['intrinsic_value_m']:.1f}M",
)
metric_cols[2].metric(
    "Total Model Value",
    f"${df['intrinsic_value_m'].sum():.1f}M",
)
metric_cols[3].metric(
    "Average Value Ratio",
    f"{df['value_efficiency'].mean():.2f}x",
)

st.subheader("Season Data")
st.dataframe(df, use_container_width=True)

left_col, right_col = st.columns(2)
with left_col:
    st.plotly_chart(plot_goat_index(df), use_container_width=True)
with right_col:
    st.plotly_chart(plot_value_comparison(df), use_container_width=True)

surplus_col, forecast_col = st.columns(2)
with surplus_col:
    st.plotly_chart(plot_surplus_value(df), use_container_width=True)
with forecast_col:
    st.plotly_chart(plot_forecast(forecast), use_container_width=True)

st.subheader("Simple Forecast")
st.dataframe(forecast, use_container_width=True)
