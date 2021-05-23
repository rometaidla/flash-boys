import pandas as pd
import yfinance as yf


def read_stock_prices(stocks, price_type):

    results = []
    for stock in stocks:
        ticker = yf.Ticker(stock)
        hist = ticker.history(period="ytd")
        hist["Stock"] = stock
        price_data = hist[["Stock", price_type]]
        price_data = price_data.rename(columns={price_type: "Price"})
        price_data.reset_index(inplace=True)
        results.append(price_data)

    price_data = pd.concat(results)
    return price_data
