import pandas as pd


GOAT_WEIGHTS = {
    "goals_per_appearance": 0.35,
    "assists_per_appearance": 0.25,
    "goal_contributions": 0.20,
    "trophies": 0.10,
    "appearances": 0.10,
}


def _min_max_normalize(series: pd.Series) -> pd.Series:
    """Scale a numeric series to 0-1 while handling constant inputs."""
    min_value = series.min()
    max_value = series.max()
    if max_value == min_value:
        return pd.Series(1.0, index=series.index)
    return (series - min_value) / (max_value - min_value)


def calculate_goat_index(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate a weighted 0-100 GOAT Index for each season or year."""
    scored = df.copy()
    scored["goals_per_appearance"] = scored["goals"] / scored["appearances"]
    scored["assists_per_appearance"] = scored["assists"] / scored["appearances"]
    scored["goal_contributions"] = scored["goals"] + scored["assists"]

    weighted_score = pd.Series(0.0, index=scored.index)
    for feature, weight in GOAT_WEIGHTS.items():
        weighted_score += _min_max_normalize(scored[feature]) * weight

    scored["goat_index"] = (weighted_score * 100).round(2)
    return scored
