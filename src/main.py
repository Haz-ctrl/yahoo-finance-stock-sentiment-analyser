import yfinance as yf
import sentimentAnalyser as sa
from colorama import init, Fore, Style

def print_title(title):
    print(Fore.YELLOW + Style.BRIGHT + f"\n{'#'*40}")
    print(Fore.YELLOW + Style.BRIGHT + f"{title:^40}")
    print(Fore.YELLOW + Style.BRIGHT + f"{'#'*40}")

def main():
    init(autoreset=True)

    while True:
        stock = input(Fore.CYAN + "Please enter the stock code you wish to download info on: " + Style.RESET_ALL).upper()
        try:
            ticker = yf.Ticker(stock)
            data = ticker.info
            news = ticker.news
            break
        except Exception as err:
            print(Fore.RED + "Invalid stock code. Please enter a valid stock code." + Style.RESET_ALL)

    print_title("Stock Information")
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
                if key == "forwardPE":
                    value = f"{value:.2f}"
                else:
                    value = f"${value:,.2f}"
            print(f"{label}: {Fore.GREEN}{value}{Style.RESET_ALL}")
        except KeyError:
            print(f"{label}: {Fore.RED}Data not available{Style.RESET_ALL}")

    print("\nDescription:")
    try:
        description = data['longBusinessSummary']
        print(description + "\n")
    except KeyError:
        print(Fore.RED + "Description not available" + Style.RESET_ALL)

    newsLinks = []
    for item in news:
        newsLinks.append(item['link'])

    overall_sentiment = sa.get_overall_sentiment(newsLinks)

    print_title("Sentiment Analysis")
    if overall_sentiment == 0.0:
        print(Fore.YELLOW + "No valid news articles found for sentiment analysis." + Style.RESET_ALL)
    else:
        print(Fore.CYAN + f"The overall sentiment portrayed by the news articles is: {format(overall_sentiment, '.2f')}" + Style.RESET_ALL)
        sa.determineSentiment(overall_sentiment)

if __name__ == "__main__":
    main()
