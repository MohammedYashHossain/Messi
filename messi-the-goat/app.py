import streamlit as st

from src.data_loader import load_all_messi_data, load_messi_data
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


def render_birthday_banner() -> None:
    """Render the Argentina x Bangladesh banner and live birthday countdown."""
    st.markdown(
        """
        <style>
            .birthday-band {
                border: 1px solid #d7e3f4;
                border-radius: 12px;
                padding: 20px 22px;
                margin: 8px 0 18px;
                background: #f7fbff;
            }
            .flag-line {
                font-size: 44px;
                line-height: 1.1;
                margin-bottom: 8px;
            }
            .birthday-band h1 {
                margin: 0;
                font-size: 34px;
                line-height: 1.2;
            }
            .birthday-band p {
                margin: 8px 0 0;
                color: #334155;
                font-size: 17px;
            }
            @media (max-width: 700px) {
                .flag-line {
                    font-size: 34px;
                }
                .birthday-band h1 {
                    font-size: 26px;
                }
            }
        </style>
        <div class="birthday-band">
            <div class="flag-line">🇦🇷 x 🇧🇩</div>
            <h1>Messi the Goat</h1>
            <p>Argentina x Bangladesh, plus a countdown to June 24 because me and Messi share the same birthday.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.iframe(
        """
        <div class="countdown-wrap">
            <div class="countdown-label">Countdown to June 24</div>
            <div id="birthday-countdown" class="countdown-time">Loading...</div>
        </div>
        <style>
            .countdown-wrap {
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                border: 1px solid #e2e8f0;
                border-radius: 10px;
                padding: 14px 16px;
                background: #ffffff;
            }
            .countdown-label {
                color: #475569;
                font-size: 14px;
                margin-bottom: 6px;
            }
            .countdown-time {
                color: #0f172a;
                font-size: 26px;
                font-weight: 700;
                letter-spacing: 0;
            }
            @media (max-width: 700px) {
                .countdown-time {
                    font-size: 21px;
                }
            }
        </style>
        <script>
            function nextBirthdayTarget() {
                const now = new Date();
                let target = new Date(now.getFullYear(), 5, 24, 0, 0, 0);
                if (now > target) {
                    target = new Date(now.getFullYear() + 1, 5, 24, 0, 0, 0);
                }
                return target;
            }

            function updateCountdown() {
                const target = nextBirthdayTarget();
                const now = new Date();
                const diff = Math.max(0, target - now);
                const days = Math.floor(diff / (1000 * 60 * 60 * 24));
                const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
                const minutes = Math.floor((diff / (1000 * 60)) % 60);
                const seconds = Math.floor((diff / 1000) % 60);
                document.getElementById("birthday-countdown").textContent =
                    `${days}d ${hours}h ${minutes}m ${seconds}s`;
            }

            updateCountdown();
            setInterval(updateCountdown, 1000);
        </script>
        """,
        height=105,
    )


@st.cache_data
def get_dashboard_data():
    """Load and enrich the dashboard dataset."""
    overall_df = load_messi_data()
    detail_df = load_all_messi_data()
    valued_df = estimate_intrinsic_value(overall_df)
    forecast_df = forecast_goat_index(valued_df, years_ahead=3)
    return valued_df, detail_df, forecast_df


df, detail, forecast = get_dashboard_data()

render_birthday_banner()
st.write(
    "A simple Messi dashboard using club and Argentina records. It combines "
    "both into one overall score, compares that score to a rough value estimate, "
    "and makes a small forecast."
)

peak_row = df.loc[df["goat_index"].idxmax()]
value_row = df.loc[df["intrinsic_value_m"].idxmax()]

metric_cols = st.columns(4)
metric_cols[0].metric("Best Season", peak_row["season"], f"{peak_row['goat_index']:.2f}")
metric_cols[1].metric(
    "Top Model Value",
    value_row["season"],
    f"${value_row['intrinsic_value_m']:.1f}M",
)
metric_cols[2].metric(
    "Total Model Value",
    f"${df['intrinsic_value_m'].sum():.1f}M",
)
metric_cols[3].metric(
    "Avg Value Ratio",
    f"{df['value_efficiency'].mean():.2f}x",
)

st.subheader("Overall Data")
st.dataframe(df, width="stretch")

st.subheader("Club And Argentina Data")
st.dataframe(detail, width="stretch")

left_col, right_col = st.columns(2)
with left_col:
    st.plotly_chart(plot_goat_index(df), width="stretch")
with right_col:
    st.plotly_chart(plot_value_comparison(df), width="stretch")

surplus_col, forecast_col = st.columns(2)
with surplus_col:
    st.plotly_chart(plot_surplus_value(df), width="stretch")
with forecast_col:
    st.plotly_chart(plot_forecast(forecast), width="stretch")

st.subheader("Simple Forecast")
st.dataframe(forecast, width="stretch")
