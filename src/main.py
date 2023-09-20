import yfinance as yf
import json
import sentimentAnalyser as sa

def main():

    while True:
        stock = input("Please enter the stock code you wish to download info on: ").upper()

        try:
            ticker = yf.Ticker(stock)
            # Convert the JSON object to a formatted string
            data = ticker.info  # For general information about the company
            news = ticker.news
            # If the Ticker object is successfully created, break out of the loop
            break
        except Exception as err:
            print("Invalid stock code. Please enter a valid stock code.")


    # Convert the data to a formatted JSON string
    pretty_data = json.dumps(news, indent=4)

    # Print the formatted data
    info_keys = [
        ("shortName", "Company name"),
        ("currentPrice", "Current trading price"),
        ("regularMarketOpen", "Price at open"),
        ("forwardPE", "Forward P/E ratio"),
        ("marketCap", "Market cap"),
        ("dayHigh", "Day high"),
        ("dayLow", "Day low"),
    ]

    for key, label in info_keys:
        try:
            value = data[key]
            if isinstance(value, (int, float)):
                # Format numbers with 2 decimal places and comma for thousands
                value = f"${value:,.2f}"
            print(f"{label}: {value}")
        except KeyError:
            print(f"{label}: Data not available")

    print("\nDescription:")
    try:
        description = data['longBusinessSummary']
        print(description + "\n")
    except KeyError:
        print("Description not available")

    newsLinks = []
    for item in news:
        newsLinks.append(item['link'])

    overall_sentiment = sa.get_overall_sentiment(newsLinks)

    if overall_sentiment == 0.0:
        print('\nNo valid news articles found for sentiment analysis.')
    else:
        print('\nThe overall sentiment portrayed by the news articles is:', format(overall_sentiment, ".2f"))
        sa.determineSentiment(overall_sentiment)

if __name__ == "__main__":
    main()