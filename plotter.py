import matplotlib.pyplot as plt
from pathlib import Path
from sklearn import preprocessing


def normalize_price(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    price = df[['Price']].values.astype(float)
    df['NormPrice'] = price
    return min_max_scaler.fit_transform(price)


def plot(df, stock, factors, save_figure=False):

    fig = plt.figure(figsize=(10, 7), facecolor="white")
    ax = plt.axes(frameon=True)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_prop_cycle('color', ['#ffbd59', '#6ce5e8', '#b1b3b3', '#2c5696'])
    plt.rcParams.update({'font.size': 14})
    plt.xticks(rotation=45)

    for i, factor in enumerate(factors):
        stock_df = df[(df['Stock'] == stock) & (df['Factor'] == factor)]
        normalized_price = normalize_price(stock_df)
        if i == 0:  # normalised price should be same for all factors, so just plot it once
            plt.plot(stock_df['Date'], normalized_price)

        plt.plot(stock_df['Date'], stock_df['Sentiment'])
        print(f"{factor } correlation: {stock_df['Sentiment'].corr(stock_df['NormPrice']):0.2f}")

    plt.legend(["Normalised price"] + factors)
    plt.title(f"{stock} sentiment")
    plt.xlabel("Date")
    plt.ylabel("Normalised price / Twitter sentiment")

    if save_figure:
        plots_folder = Path("plots")
        plots_folder.mkdir(exist_ok=True)
        plt.savefig(plots_folder / f"{stock}.png")