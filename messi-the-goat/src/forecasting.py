import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from src.metrics import calculate_goat_index


FORECAST_FEATURES = [
    "age",
    "appearances",
    "goals",
    "assists",
    "trophies",
    "estimated_market_value_m",
]


def forecast_goat_index(df: pd.DataFrame, years_ahead: int = 3) -> pd.DataFrame:
    """Forecast future GOAT Index values from age and recent production features."""
    if years_ahead < 1:
        raise ValueError("years_ahead must be at least 1")

    model_df = df.copy()
    if "goat_index" not in model_df.columns:
        model_df = calculate_goat_index(model_df)

    x = model_df[FORECAST_FEATURES]
    y = model_df["goat_index"]

    if len(model_df) >= 10:
        model = RandomForestRegressor(n_estimators=300, random_state=42, min_samples_leaf=2)
    else:
        model = LinearRegression()
    model.fit(x, y)

    latest = model_df.sort_values("age").iloc[-1]
    recent = model_df.tail(min(4, len(model_df)))
    future_rows = []

    for step in range(1, years_ahead + 1):
        aging_factor = 0.92**step
        future_features = {
            "age": int(latest["age"] + step),
            "appearances": max(12, recent["appearances"].mean() * aging_factor),
            "goals": max(4, recent["goals"].mean() * aging_factor),
            "assists": max(3, recent["assists"].mean() * aging_factor),
            "trophies": max(0, recent["trophies"].mean() * aging_factor),
            "estimated_market_value_m": max(
                5,
                recent["estimated_market_value_m"].mean() * aging_factor,
            ),
        }
        prediction = float(model.predict(pd.DataFrame([future_features]))[0])
        future_rows.append(
            {
                "forecast_year": step,
                "age": future_features["age"],
                "predicted_goat_index": round(max(0, min(100, prediction)), 2),
            }
        )

    return pd.DataFrame(future_rows)
