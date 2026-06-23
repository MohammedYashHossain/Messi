# Messi the Goat

This is a simple Python project about Lionel Messi's career.

It takes Messi's season stats, gives each season a score, estimates a rough value for that season, and shows a short forecast for the next few years.

The project is not trying to be a perfect football model. It is just a clean way to look at Messi's numbers with Python.

## What The App Does

- Loads sample Messi season data
- Creates per-90 stats like goals per 90 and assists per 90
- Builds a GOAT Index score from 0 to 100
- Estimates a rough model value for each season
- Compares model value with market value
- Forecasts the next few seasons
- Shows everything in a Streamlit dashboard

## Tools Used

- Python
- Pandas
- scikit-learn
- Streamlit
- Plotly
- pytest

## How To Run It

```bash
cd messi-the-goat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

On macOS or Linux, use this line to activate the virtual environment:

```bash
source .venv/bin/activate
```

## How To Run Tests

```bash
pytest
```

## How The Score Works

The GOAT Index is a simple weighted score.

It uses stats like:

- Goals
- Assists
- xG
- xA
- Key passes
- Successful dribbles
- Progressive carries
- Trophies
- Minutes played

Most of the stats are turned into per-90 numbers first. Then they are scaled and combined into one score from 0 to 100.

## Project Files

```text
messi-the-goat/
|-- app.py
|-- README.md
|-- requirements.txt
|-- data/
|   |-- messi_seasons.csv
|-- src/
|   |-- data_loader.py
|   |-- metrics.py
|   |-- valuation.py
|   |-- forecasting.py
|   |-- visuals.py
|-- tests/
    |-- test_metrics.py
    |-- test_valuation.py
```

## Things I Would Add Later

- Use real data from a football data source
- Add league difficulty
- Adjust old market values for inflation
- Show which stats matter most in the forecast
