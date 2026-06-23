# Messi the Goat

I made this project because I love Messi and I think he is the GOAT.

This is a simple Python app that looks at Messi's real club season records and turns them into a few easy things to understand: a season score, a rough value estimate, and a short forecast.

It is not supposed to be a perfect football model. I just wanted to build something clean around Messi's career and show his numbers in a fun way.

## How It Works

The app starts with Messi season data from Barcelona, PSG, and Inter Miami. The appearances and goals come from Messi's career statistics table. The assists and value numbers are there so the model has enough to score and compare each season.

For each season, it looks at stats like:

- Goals
- Assists
- Trophies
- Appearances

Goals and assists are changed into per-appearance numbers first, so the seasons are easier to compare.

Then the app builds a GOAT Index from 0 to 100. A higher score means the season was stronger based on the stats in the model.

After that, the app makes a rough model value for each season and compares it to the estimated market value. It also makes a small forecast for the next few seasons.

## What You See In The App

- Messi's season data
- His GOAT Index by season
- Market value vs model value
- Extra value by season
- A short future forecast

## How To Run It

```bash
cd messi-the-goat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

On macOS or Linux, activate the virtual environment with:

```bash
source .venv/bin/activate
```

## How To Run Tests

```bash
pytest
```

## Data Source

- Lionel Messi career statistics on Wikipedia: https://en.wikipedia.org/wiki/Lionel_Messi
