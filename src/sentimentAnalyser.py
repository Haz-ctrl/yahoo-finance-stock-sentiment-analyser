import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getArticleSentiment(url):
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

        # Determine the sentiment label based on the compound score
        compound_sentiment = sentiment_scores['compound']
        if compound_sentiment >= 0.05:
            sentiment_label = "Positive"
        elif compound_sentiment <= -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        return sentiment_label
    else:
        # Return None for invalid URLs
        return None

def getOverallSentiment(urls):
    overall_sentiment = {
        'Positive': 0,
        'Neutral': 0,
        'Negative': 0
    }
    valid_urls_count = 0  # To keep track of the number of valid URLs

    for url in urls:
        sentiment_label = getArticleSentiment(url)
        if sentiment_label is not None:
            overall_sentiment[sentiment_label] += 1
            valid_urls_count += 1

    if valid_urls_count > 0:
        return overall_sentiment
    else:
        return {'Positive': 0, 'Neutral': 0, 'Negative': 0}
    
def determineSentiment(overall_sentiment):
    total_sentiments = overall_sentiment['Positive'] + overall_sentiment['Neutral'] + overall_sentiment['Negative']
    if total_sentiments > 0:
        positive_ratio = overall_sentiment['Positive'] / total_sentiments
        negative_ratio = overall_sentiment['Negative'] / total_sentiments
    else:
        positive_ratio = 0
        negative_ratio = 0

    if positive_ratio > 0.5:
        sentiment_label = "Positive"
    elif negative_ratio > 0.5:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    print(f"Overall sentiment: {sentiment_label}")