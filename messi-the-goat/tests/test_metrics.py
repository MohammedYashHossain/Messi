from src.data_loader import load_messi_data
from src.metrics import calculate_goat_index


def test_goat_index_range():
    df = calculate_goat_index(load_messi_data())

    assert df["goat_index"].between(0, 100).all()
