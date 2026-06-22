import pandas as pd

from src.metrics import calculate_goat_index


def estimate_intrinsic_value(
    df: pd.DataFrame,
    discount_rate: float = 0.10,
    dollars_per_goat_point_m: float = 1.5,
) -> pd.DataFrame:
    """Estimate finance-style intrinsic value from seasonal GOAT Index output."""
    if discount_rate <= -1:
        raise ValueError("discount_rate must be greater than -1")

    valued = df.copy()
    if "goat_index" not in valued.columns:
        valued = calculate_goat_index(valued)

    year_numbers = pd.Series(range(1, len(valued) + 1), index=valued.index)
    valued["annual_value_m"] = valued["goat_index"] * dollars_per_goat_point_m
    valued["intrinsic_value_m"] = (
        valued["annual_value_m"] / ((1 + discount_rate) ** year_numbers)
    ).round(2)
    valued["surplus_value_m"] = (
        valued["intrinsic_value_m"] - valued["estimated_market_value_m"]
    ).round(2)
    valued["value_efficiency"] = (
        valued["intrinsic_value_m"] / valued["estimated_market_value_m"]
    ).round(2)
    return valued
