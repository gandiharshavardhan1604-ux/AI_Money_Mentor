import plotly.express as px
import pandas as pd

def plot_allocation(alloc):
    df = pd.DataFrame({"Category": ["Equity", "Debt", "Gold"], "Allocation": alloc})
    fig = px.pie(df, values="Allocation", names="Category", title="Recommended Portfolio Allocation")
    return fig

def plot_growth(sip, years, rate=0.12):
    n = years * 12
    r = rate / 12
    months = list(range(1, n+1))
    values = []
    total = 0
    for month in months:
        total = total * (1 + r) + sip
        values.append(total)
    growth_df = pd.DataFrame({"Month": months, "Wealth": values})
    fig = px.line(growth_df, x="Month", y="Wealth", title="Projected Wealth Growth")
    return fig