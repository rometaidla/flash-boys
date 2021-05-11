import pandas as pd
import yfinance as yf


def read_stock_prices(stocks):
    results = []
    for stock in stocks:
        ticker = yf.Ticker(stock)
        hist = ticker.history(period="ytd")
        hist["Stock"] = stock
        price_data = hist[["Stock", "Close"]]
        price_data.reset_index(inplace=True)
        results.append(price_data)

    price_data = pd.concat(results)
    return price_data
