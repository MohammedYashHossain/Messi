from src.data_loader import load_messi_data
from src.valuation import estimate_intrinsic_value


def test_valuation_positive():
    df = estimate_intrinsic_value(load_messi_data())

    assert (df["intrinsic_value_m"] > 0).all()


def test_surplus_value_exists():
    df = estimate_intrinsic_value(load_messi_data())

    assert "surplus_value_m" in df.columns
