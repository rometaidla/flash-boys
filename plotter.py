import matplotlib.pyplot as plt
from pathlib import Path
from sklearn import preprocessing


def normalize_price(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    price = df[['Price']].values.astype(float)
    df['NormPrice'] = price
    return min_max_scaler.fit_transform(price)


def plot(df, stock, save_figure=False):

    plt.figure(figsize=(15, 7))
    plt.rcParams.update({'font.size': 14})

    stock_df = df[df['Stock'] == stock]
    normalized_price = normalize_price(stock_df)
    plt.plot(stock_df['Date'], stock_df['Sentiment'])
    plt.plot(stock_df['Date'], normalized_price)
    plt.legend(["Twitter sentiment", "Normalised stock price"])
    plt.title(f"{stock} sentiment")
    plt.xlabel("Date")
    plt.ylabel("Normalised price / Twitter sentiment")
    print(f"Correlation: {stock_df['Sentiment'].corr(stock_df['NormPrice']):0.2f}")

    if save_figure:
        plots_folder = Path("plots")
        plots_folder.mkdir(exist_ok=True)
        plt.savefig(plots_folder / f"{stock}.png")