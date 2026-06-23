# Messi the Goat

I made this project because I love Messi and I think he is the GOAT.

This is a simple Python app that looks at Messi's club and Argentina records and turns them into a few easy things to understand: an overall score, a rough value estimate, and a short forecast.

It is not supposed to be a perfect football model. I just wanted to build something clean around Messi's career and show his numbers in a fun way.

## How It Works

The app starts with two datasets. One has Messi's club seasons from Barcelona, PSG, and Inter Miami. The other has his Argentina numbers by year.

For each season, it looks at stats like:

- Goals
- Assists
- Trophies
- Appearances

Goals and assists are changed into per-appearance numbers first, so the seasons are easier to compare.

Then the app builds a GOAT Index from 0 to 100. A higher score means the season was stronger based on the stats in the model.

The app combines the club and Argentina rows by year. So instead of only scoring club seasons, it gives one overall Messi score for each year.

After that, the app makes a rough model value and compares it to the estimated market value. It also makes a small forecast for the next few years.

## What You See In The App

- Messi's club and Argentina data
- His overall GOAT Index by year
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
- Lionel Messi international goals and appearances by year on Wikipedia: https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Lionel_Messi
