


import pandas as pd
import numpy as np
import yfinance as yf
from textblob import TextBlob
import streamlit as st


# 1. Fetch stock data using yfinance
def fetch_stock_data(ticker, start, end):
    try:
        stock_data = yf.download(ticker, start=start, end=end)
        stock_data.reset_index(inplace=True)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
        return None


# 2. Sentiment analysis with TextBlob
def analyze_sentiment(news):
    sentiments = []
    for headline in news:
        if headline.strip():
            analysis = TextBlob(headline)
            sentiments.append(analysis.sentiment.polarity)
        else:
            sentiments.append(None)  # Handle empty lines
    return sentiments


# 3. Stock Performance Analysis
def analyze_stock_performance(ticker, date, price):
    return f"The closing price of {ticker} stock on {date} was {price}. Based on this data, we can infer the stock's market performance."

# 4. News Summary Analysis
def summarize_news_sentiment(headline, sentiment):
    return f"The headline '{headline}' indicates a sentiment of {sentiment}. Overall, it suggests {('positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral')} market sentiment."


# 5. Streamlit UI
st.title("AI-Powered Financial Market Analysis")

# 5.1. Stock Data Section
st.subheader("Stock Data Analysis")
ticker = st.text_input("Enter Stock Ticker", "AAPL")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Fetch Stock Data"):
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')
    data = fetch_stock_data(ticker, start_date_str, end_date_str)
    if data is not None and not data.empty:
        st.write(data.head())  # Display the first few rows of the stock data
        st.line_chart(data['Close'].dropna())
    else:
        st.error("No data available for the given input.")

# 5.2. Sentiment Analysis Section
st.subheader("Sentiment Analysis")
headlines = st.text_area("Enter News Headlines (separated by line)")

if st.button("Analyze Sentiment"):
    if headlines.strip():
        news = headlines.split("\n")
        sentiments = analyze_sentiment(news)
        sentiment_df = pd.DataFrame({'Headline': news, 'Sentiment': sentiments})
        st.dataframe(sentiment_df)
    else:
        st.error("Please enter valid headlines for analysis.")

# 5.3. Stock and News Analysis
st.subheader("Stock and News Analysis Example")
if st.button("Run Example Analysis"):
    # Example inputs
    example_ticker = "AAPL"
    example_date = "2023-01-01"
    example_price = 150
    example_headline = "Apple stock rises after record earnings."
    example_sentiment = 0.8

    # Perform analysis
    stock_result = analyze_stock_performance(example_ticker, example_date, example_price)
    news_result = summarize_news_sentiment(example_headline, example_sentiment)

    # Display results
    st.write("Stock Analysis Output:")
    st.write(stock_result)

    st.write("News Summary Output:")
    st.write(news_result)


























