import matplotlib.pyplot as plt
from pathlib import Path
from sklearn import preprocessing


def normalize_price(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    price = df[['Price']].values.astype(float)
    df['NormPrice'] = price
    return min_max_scaler.fit_transform(price)


def plot(df, stocks, factors, save_figure=False):
    columns = 2
    fig, axs = plt.subplots(3, columns, figsize=(20, 20), facecolor="white")
    fig.autofmt_xdate()
    axs = axs.reshape(-1)
    for i, stock in enumerate(stocks):
        ax = axs[i]
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_prop_cycle('color', ['#ffbd59', '#6ce5e8', '#b1b3b3', '#2c5696'])

        for f_idx, factor in enumerate(factors):
            stock_df = df[(df['Stock'] == stock) & (df['Factor'] == factor)]
            if len(stock_df):
                normalized_price = normalize_price(stock_df)
                #print(f"{factor} correlation: {stock_df['Sentiment'].corr(stock_df['NormPrice']):0.2f}")

            if f_idx == 0:  # normalised price should be same for all factors, so just plot it once
                ax.plot(stock_df['Date'], normalized_price)

            ax.plot(stock_df['Date'], stock_df['Sentiment'])

        ax.set_title(f"{stock} sentiment")
        if i % columns == 0:
            ax.set_ylabel("Normalised price / Twitter sentiment")

    axs[1].legend(["Normalised price"] + factors)
    plt.xticks(rotation=45)

    if save_figure:
        plots_folder = Path("plots")
        plots_folder.mkdir(exist_ok=True)
        plt.savefig(plots_folder / f"{stock}.png")