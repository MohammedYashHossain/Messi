# Messi the Goat

Messi the Goat is a small Python project about Lionel Messi's career. It uses season stats to create a simple score, estimate a rough player value, and forecast the next few seasons.

## Project Overview

The project uses sample season data from Messi's time at Barcelona, PSG, and Inter Miami. The data is already included, so the app can run without an API key.

The main idea is simple: take Messi's goals, assists, expected stats, passing, dribbling, carries, trophies, and minutes, then turn them into one score from 0 to 100. I called that score the GOAT Index.

The app also turns that score into a rough dollar value. It is not meant to be a perfect football model. It is meant to show how sports stats, Python, charts, and a little finance logic can fit together in one project.

## What This Shows

- Loading and cleaning data with Pandas
- Creating new stats like goals per 90
- Building a custom weighted score
- Estimating value with a basic discounting formula
- Making a simple forecast with scikit-learn
- Showing everything in a Streamlit dashboard
- Testing the main functions with pytest

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Pytest

## Features

- Sample Messi season data
- GOAT Index for each season
- Rough model value for each season
- Market value vs model value chart
- Extra value chart
- Short forecast for future seasons
- Tests for the score and value functions

## Setup Instructions

```bash
cd messi-the-goat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS or Linux:

```bash
cd messi-the-goat
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run The App

```bash
streamlit run app.py
```

## Run Tests

```bash
pytest
```

## Project Structure

```text
messi-the-goat/
|-- app.py
|-- README.md
|-- requirements.txt
|-- data/
|   |-- messi_seasons.csv
|-- src/
|   |-- __init__.py
|   |-- data_loader.py
|   |-- metrics.py
|   |-- valuation.py
|   |-- forecasting.py
|   |-- visuals.py
|-- tests/
    |-- test_metrics.py
    |-- test_valuation.py
```

## Model Notes

The GOAT Index is a score from 0 to 100. It uses:

- Goals per 90
- Assists per 90
- xG per 90
- xA per 90
- Key passes per 90
- Successful dribbles per 90
- Progressive carries per 90
- Trophies
- Minutes played

The value model is basic. It turns the GOAT Index into a dollar value, then discounts it:

```text
annual_value_m = goat_index * 1.5
intrinsic_value_m = annual_value_m / ((1 + discount_rate) ** year_number)
```

This is a simple model on purpose. The goal is to make the project easy to understand and easy to explain.

## Future Improvements

- Use real data from a football data source
- Add league difficulty
- Adjust old market values for inflation
- Compare Messi with other players
- Show which stats matter most in the forecast
- Deploy the app online

## Resume Bullets

- Built a Python dashboard that scores Messi's seasons using goals, assists, expected stats, dribbling, passing, trophies, and minutes.
- Used Pandas, scikit-learn, and Streamlit to calculate a GOAT Index, estimate player value, and forecast future performance.
- Created Plotly charts to compare Messi's performance score, market value, model value, and future trend.
