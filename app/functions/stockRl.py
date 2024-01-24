import yfinance as yf
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

plt.style.use('ggplot')

today = date.today()
start = dt.datetime(2013, 1, 1)
end = dt.datetime(today.year, today.month, today.day)

tickers = ['AAPL', 'AMZN', 'MSFT', 'GOOGL', 'TSLA']

# Download stock prices
stocks = yf.download(tickers, start=start, end=end, progress=False)['Adj Close']

def calculate_metrics(returns):
    # Calculate annual returns
    annual_returns = returns.resample('Y').last().pct_change().mean() * 252

    # Calculate daily drawdown using the provided formula
    roll_max = returns.rolling(window=len(returns), min_periods=1).max()
    daily_drawdown = returns / roll_max - 1.0

    # Calculate max daily drawdown using the provided formula
    max_daily_drawdown = daily_drawdown.rolling(window=len(daily_drawdown), min_periods=1).min()

    # Calculate max drawdown as the minimum (negative) max daily drawdown
    max_drawdown = -max_daily_drawdown.min()

    # Calculate annualized volatility
    annualized_volatility = returns.std() * np.sqrt(252)

    # Calculate Sharpe ratio
    sharpe_ratio = annual_returns / annualized_volatility

    # Calculate Calmar ratio
    calmar_ratio = annual_returns / abs(max_drawdown)
    
   
    return {
        'Annual Returns': annual_returns,
        'Max Drawdown': max_drawdown,
        'Sharpe Ratio': sharpe_ratio,
        'Calmar Ratio': calmar_ratio,
    }



# Calculate metrics for each stock
metrics_dict = {}
for ticker in tickers:
    metrics_dict[ticker] = calculate_metrics(stocks[ticker])

# Convert metrics to a DataFrame for better readability
metrics_df = pd.DataFrame(metrics_dict)

# Display the calculated metrics
print(metrics_df)
def get_results():
    # Calculate metrics for each stock
    metrics_dict = {}
    for ticker in tickers:
        metrics_dict[ticker] = calculate_metrics(stocks[ticker])

    # Convert metrics to a DataFrame for better readability
    metrics_df = pd.DataFrame(metrics_dict)

    return metrics_df
