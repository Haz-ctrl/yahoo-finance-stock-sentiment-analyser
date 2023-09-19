import yfinance as yf
import json
import sentimentAnalyser as sa

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

overall_sentiment = sa.get_overall_sentiment(newsLinks)

if overall_sentiment is not None:
    print('\nThe overall sentiment of the news articles is:', overall_sentiment)
else:
    print('\nNo valid news articles found for sentiment analysis.')

if(overall_sentiment < 0.5):
            print("Overall Sentiment: Negative")
if(0.5 < overall_sentiment and overall_sentiment < 0.7): 
            print("Overall Sentiment: Balanced")
if(0.7 < overall_sentiment and overall_sentiment < 1):
            print("Overall Sentiment: Positive")