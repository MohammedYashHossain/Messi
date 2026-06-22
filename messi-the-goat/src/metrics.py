import pandas as pd


GOAT_WEIGHTS = {
    "goals_per90": 0.22,
    "assists_per90": 0.16,
    "xg_per90": 0.14,
    "xa_per90": 0.12,
    "key_passes_per90": 0.10,
    "dribbles_per90": 0.10,
    "progressive_carries_per90": 0.08,
    "trophies": 0.05,
    "minutes": 0.03,
}


def _min_max_normalize(series: pd.Series) -> pd.Series:
    """Scale a numeric series to 0-1 while handling constant inputs."""
    min_value = series.min()
    max_value = series.max()
    if max_value == min_value:
        return pd.Series(1.0, index=series.index)
    return (series - min_value) / (max_value - min_value)


def calculate_goat_index(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate a weighted 0-100 GOAT Index for each season."""
    scored = df.copy()
    minutes_per_90 = scored["minutes"] / 90

    scored["goals_per90"] = scored["goals"] / minutes_per_90
    scored["assists_per90"] = scored["assists"] / minutes_per_90
    scored["xg_per90"] = scored["xg"] / minutes_per_90
    scored["xa_per90"] = scored["xa"] / minutes_per_90
    scored["key_passes_per90"] = scored["key_passes"] / minutes_per_90
    scored["dribbles_per90"] = scored["successful_dribbles"] / minutes_per_90
    scored["progressive_carries_per90"] = scored["progressive_carries"] / minutes_per_90

    weighted_score = pd.Series(0.0, index=scored.index)
    for feature, weight in GOAT_WEIGHTS.items():
        weighted_score += _min_max_normalize(scored[feature]) * weight

    scored["goat_index"] = (weighted_score * 100).round(2)
    return scored
