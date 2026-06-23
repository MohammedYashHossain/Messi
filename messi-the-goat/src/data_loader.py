from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CLUB_DATA_PATH = PROJECT_ROOT / "data" / "messi_seasons.csv"
DEFAULT_ARGENTINA_DATA_PATH = PROJECT_ROOT / "data" / "messi_argentina.csv"


def _season_to_year(season: str) -> int:
    """Convert a club season or calendar year into one sortable year."""
    season_text = str(season)
    if "-" not in season_text:
        return int(season_text)

    start_year, end_year = season_text.split("-", maxsplit=1)
    if len(end_year) == 2:
        return int(start_year[:2] + end_year)
    return int(end_year)


def _load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV file and fail clearly if it is missing."""
    data_path = Path(path)
    if not data_path.exists():
        raise FileNotFoundError(f"Could not find data file: {data_path}")

    return pd.read_csv(data_path)


def _prepare_rows(df: pd.DataFrame, source_type: str) -> pd.DataFrame:
    """Add shared fields used by the app and model."""
    prepared = df.copy()
    prepared["season"] = prepared["season"].astype(str)
    prepared["year"] = prepared["season"].apply(_season_to_year)
    prepared["source_type"] = source_type
    return prepared.sort_values(["year", "source_type"]).reset_index(drop=True)


def load_club_data(path: str | Path = DEFAULT_CLUB_DATA_PATH) -> pd.DataFrame:
    """Load Messi's club season data."""
    return _prepare_rows(_load_csv(path), "Club")


def load_argentina_data(path: str | Path = DEFAULT_ARGENTINA_DATA_PATH) -> pd.DataFrame:
    """Load Messi's Argentina season data."""
    return _prepare_rows(_load_csv(path), "Argentina")


def load_all_messi_data() -> pd.DataFrame:
    """Load club and Argentina rows together."""
    return pd.concat([load_club_data(), load_argentina_data()], ignore_index=True).sort_values(
        ["year", "source_type"]
    ).reset_index(drop=True)


def load_messi_data() -> pd.DataFrame:
    """Load an overall year-by-year Messi dataset from club and Argentina rows."""
    all_rows = load_all_messi_data()
    combined = (
        all_rows.groupby("year", as_index=False)
        .agg(
            age=("age", "max"),
            appearances=("appearances", "sum"),
            goals=("goals", "sum"),
            assists=("assists", "sum"),
            trophies=("trophies", "sum"),
            estimated_market_value_m=("estimated_market_value_m", "max"),
        )
        .sort_values("year")
        .reset_index(drop=True)
    )
    combined["season"] = combined["year"].astype(str)
    combined["club"] = "Club + Argentina"
    combined["league"] = "Overall"
    combined["source"] = "Club data plus Argentina data"
    combined["source_type"] = "Overall"

    columns = [
        "season",
        "year",
        "age",
        "club",
        "league",
        "appearances",
        "goals",
        "assists",
        "trophies",
        "estimated_market_value_m",
        "source",
        "source_type",
    ]
    return combined[columns]
