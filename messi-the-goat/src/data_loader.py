from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "messi_seasons.csv"


def load_messi_data(path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load season-level Messi data from a CSV file."""
    data_path = Path(path)
    if not data_path.exists():
        raise FileNotFoundError(f"Could not find data file: {data_path}")

    df = pd.read_csv(data_path)
    return df.sort_values(["age", "season"]).reset_index(drop=True)
