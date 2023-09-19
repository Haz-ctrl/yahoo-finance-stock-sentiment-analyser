import yfinance as yf
import json

stock = input("Please enter the stock code you wish to download info on:")
btc = yf.Ticker("TSLA")

# Current price, price at start of day, high, low, mkt cap, p/e ratio
# Convert the JSON object to a formatted string
data = btc.info  # For general information about the company

# Convert the data to a formatted JSON string
pretty_data = json.dumps(data, indent=4)

# Print the formatted data
print(f"Day high: ${data['dayHigh']}")
print(f"Day low: ${data['dayLow']}")