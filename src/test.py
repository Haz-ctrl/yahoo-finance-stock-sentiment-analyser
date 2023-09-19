import json
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
        print("Compound Sentiment:", compound_sentiment)
        return compound_sentiment

    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None