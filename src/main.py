import yfinance as yf
import json

stock = input("Please enter the stock code you wish to download info on: ")
ticker = yf.Ticker(stock)

# Current price, price at start of day, high, low, mkt cap, p/e ratio
# Convert the JSON object to a formatted string
data = ticker.info  # For general information about the company
news = ticker.news

# Convert the data to a formatted JSON string
pretty_data = json.dumps(news, indent=4)

# Print the formatted data
print(f"Company name: {data['shortName']}")
print(f"Current trading price: ${data['currentPrice']}")
print(f"Price at open: ${data['regularMarketOpen']}")
print(f"Forward P/E ratio: {data['forwardPE']}")
print(f"Market cap: ${data['marketCap']}")
print(f"Day high: ${data['dayHigh']}")
print(f"Day low: ${data['dayLow']}")

print(f"\nDescription: {data['longBusinessSummary']}")

newsLinks = []
for item in news:
    newsLinks.append(item['link'])