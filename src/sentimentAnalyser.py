import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_article_sentiment(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract relevant data (e.g., text content)
        text_content = soup.get_text()

        # Perform sentiment analysis using VADER
        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = analyzer.polarity_scores(text_content)

        # Create a dictionary to hold the data including sentiment analysis results
        data = {
            'text_content': text_content,
            'sentiment_scores': sentiment_scores
        }

        # Print the compound sentiment score from the data dictionary
        compound_sentiment = data['sentiment_scores']['compound']
        print(f"Reading article: {url}, Sentiment analysis result: {format(compound_sentiment, '.2f')}")
        return compound_sentiment

    else:
        # print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None

def get_overall_sentiment(urls):
    """Calculates the overall sentiment of an array of news articles."""
    
    overall_sentiment = 0.0
    valid_urls_count = 0  # To keep track of the number of valid URLs
    
    for url in urls:
        article_sentiment = get_article_sentiment(url)
        if article_sentiment is not None:
            overall_sentiment += article_sentiment
            valid_urls_count += 1

    if valid_urls_count > 0:
        return round((overall_sentiment / valid_urls_count), 2)
    else:
        return 0.0  # Return 0.0 if no valid URLs were processed
    
def determineSentiment(overall_sentiment):
    if overall_sentiment < 0.5:
        sentiment_label = "Negative"
    elif overall_sentiment < 0.7:
        sentiment_label = "Balanced"
    elif overall_sentiment < 1:
        sentiment_label = "Positive"
    else:
        sentiment_label = "Undetermined"

    print(f"Overall sentiment: {sentiment_label}")

# Example usage:

# urls = [
#     'https://www.nytimes.com/2023/09/19/business/economy-recession-fears.html',
#     'https://www.washingtonpost.com/business/2023/09/19/stock-market-today-dow-jones-nasdaq/',
#     'https://www.wsj.com/articles/fed-raises-interest-rates-again-in-fight-against-inflation-11663572869'
# ]

# overall_sentiment = get_overall_sentiment(urls)

# print('The overall sentiment of the news articles is:', overall_sentiment)