# Yahoo Finance Stock Sentiment Analyser

This project was a collaboration between Haz-ctrl and malik1234, where we made a Python program to display stock information using the Yahoo Finance API, in addition to using NLP techniques to provide a recent news analysis sentiment about the selected stock.

At the time of writing (22/10/2023), the yfinance API is experiencing some issues in that a 404 HTTPS error is returned when trying to access any stock ticker data. A workaround for this is to use a VPN connected to the US. In the UK, it doesn't appear to work. It is unclear when the issue will be fixed, but a ticket has been submitted at the [yfinance repo](https://github.com/ranaroussi/yfinance/issues/1729)

Instructions for generating a requirements.txt file:\
`pip install pipreqs`\
`pipreqs /path/to/src`

Installing packages from a requirements.txt file:\
`pip install -r requirements.txt`