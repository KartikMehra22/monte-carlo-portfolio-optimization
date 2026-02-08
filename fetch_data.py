import yfinance as yf
import pandas as pd
import os

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

tickers = ["AAPL", "MSFT", "GOOGL", "SPY"]

# Download data for multiple tickers
# By default yfinance returns a multi-index DataFrame if multiple tickers are provided.
# However, selecting "Close" directly might behave differently depending on version.
# Let's verify with the provided code structure first.
data = yf.download(
    tickers,
    start="2020-01-01",
    end="2025-12-31",
    auto_adjust=True
)["Close"]

# Reset index to make Date a column
data = data.reset_index()

# Convert to long format
long_df = data.melt(
    id_vars="Date", 
    var_name="Asset", 
    value_name="Price"
)

# Save to CSV
output_path = "data/asset_prices_long.csv"
long_df.to_csv(output_path, index=False)

print(f"✅ Saved: {output_path}")
