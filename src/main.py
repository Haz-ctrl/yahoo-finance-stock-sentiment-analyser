import yfinance as yf
import json
import sentimentAnalyser as sa

stock = input("Please enter the stock code you wish to download info on: ")
ticker = yf.Ticker(stock)

# Convert the JSON object to a formatted string
data = ticker.info  # For general information about the company
news = ticker.news

# Convert the data to a formatted JSON string
pretty_data = json.dumps(news, indent=4)

# Print the formatted data
print(f"Company name: {data['shortName']}")
print(f"Current trading price: ${format(data['currentPrice'], '.2f')}")
print(f"Price at open: ${format(data['regularMarketOpen'], '.2f')}")
print(f"Forward P/E ratio: {data['forwardPE']}")
print(f"Market cap: ${data['marketCap']:,d}")
print(f"Day high: ${format(data['dayHigh'], '.2f')}")
print(f"Day low: ${format(data['dayLow'], '.2f')}")

print(f"\nDescription:\n{data['longBusinessSummary']}\n")

newsLinks = []
for item in news:
    newsLinks.append(item['link'])

overall_sentiment = sa.get_overall_sentiment(newsLinks)

if overall_sentiment is not None:
    print('\nThe overall sentiment portrayed by the news articles is:', format(overall_sentiment, ".2f"))
else:
    print('\nNo valid news articles found for sentiment analysis.')

sa.determineSentiment(overall_sentiment)