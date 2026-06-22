import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


CHART_TEMPLATE = "plotly_white"


def plot_goat_index(df: pd.DataFrame) -> go.Figure:
    """Plot Messi's season-by-season GOAT Index."""
    fig = px.line(
        df,
        x="season",
        y="goat_index",
        markers=True,
        color="club",
        title="Messi Score by Season",
        template=CHART_TEMPLATE,
    )
    fig.update_layout(yaxis_title="GOAT Index", xaxis_title="Season")
    return fig


def plot_value_comparison(df: pd.DataFrame) -> go.Figure:
    """Compare model intrinsic value with estimated market value."""
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["season"],
            y=df["estimated_market_value_m"],
            mode="lines+markers",
            name="Market value",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["season"],
            y=df["intrinsic_value_m"],
            mode="lines+markers",
            name="Model value",
        )
    )
    fig.update_layout(
        title="Market Value vs Model Value",
        xaxis_title="Season",
        yaxis_title="Value in millions",
        template=CHART_TEMPLATE,
    )
    return fig


def plot_surplus_value(df: pd.DataFrame) -> go.Figure:
    """Plot surplus value by season."""
    colors = ["#16a34a" if value >= 0 else "#dc2626" for value in df["surplus_value_m"]]
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["season"],
                y=df["surplus_value_m"],
                marker_color=colors,
                name="Extra value",
            )
        ]
    )
    fig.update_layout(
        title="Extra Value by Season",
        xaxis_title="Season",
        yaxis_title="Value in millions",
        template=CHART_TEMPLATE,
    )
    return fig


def plot_forecast(forecast_df: pd.DataFrame) -> go.Figure:
    """Plot the predicted future GOAT Index aging curve."""
    fig = px.line(
        forecast_df,
        x="age",
        y="predicted_goat_index",
        markers=True,
        title="Next Few Years Forecast",
        template=CHART_TEMPLATE,
    )
    fig.update_layout(yaxis_title="Predicted score", xaxis_title="Age")
    return fig
