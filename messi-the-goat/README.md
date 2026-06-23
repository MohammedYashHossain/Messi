# Messi the Goat

You can find the live project here: https://ilovemessi.streamlit.app/

I have loved Messi ever since I was a kid. Me and Messi also have the same birthday, so that made me like him even more.

I decided to make a Python project about Messi because he is the GOAT. This project is basically my way of showing how much I love Messi while also using computer science, data, and Python.

The app looks at Messi's club and Argentina records, gives each year a GOAT Index score, compares that score to a rough value estimate, and shows a small forecast.

## What The Project Does

- Uses Messi club and Argentina data
- Combines both into one overall yearly score
- Calculates a GOAT Index from 0 to 100
- Shows market value vs model value
- Shows extra value by year
- Forecasts the next few years

## How To Run It

```bash
cd messi-the-goat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

## Data Sources

- https://en.wikipedia.org/wiki/Lionel_Messi
- https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Lionel_Messi
