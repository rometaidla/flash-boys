import pandas as pd
import yfinance as yf
from sklearn import preprocessing

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


def normalize_price(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    price = df[['Price']].values.astype(float)
    norm_price = min_max_scaler.fit_transform(price)
    df['NormPrice'] = norm_price
    return norm_price
