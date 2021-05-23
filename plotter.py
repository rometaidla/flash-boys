import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn import preprocessing
import seaborn as sns


def normalize_price(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    price = df[['Price']].values.astype(float)
    df['NormPrice'] = price
    return min_max_scaler.fit_transform(price)


def plot_correlations(df, stocks, factors):
    n_stocks = len(stocks)
    n_factors = len(factors)

    correlations = np.zeros((n_stocks, n_factors))

    for s_idx, stock in enumerate(stocks):
        for f_idx, factor in enumerate(factors):
            stock_df = df[(df['Stock'] == stock) & (df['Factor'] == factor)]
            if len(stock_df) > 0:
                normalize_price(stock_df)
                correlations[s_idx, f_idx] = stock_df['Sentiment'].corr(stock_df['NormPrice'])

    sns.heatmap(correlations, xticklabels=factors, yticklabels=stocks, linewidths=.5, cmap="RdYlGn", annot=True);
    plt.yticks(rotation=0)
    plt.title("Sentiment correlation with stock price")

def plot_sentiments(df, stocks, factors, save_figure=False):
    columns = 2
    rows = len(stocks) // columns + (len(stocks) % columns > 0)
    fig, axs = plt.subplots(rows, columns, figsize=(columns*10, rows*7), facecolor="white")
    fig.autofmt_xdate()
    axs = axs.reshape(-1)
    for i, stock in enumerate(stocks):
        ax = axs[i]
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_prop_cycle('color', ['#6ce5e8', '#ffbd59', '#b1b3b3'])

        for f_idx, factor in enumerate(factors):
            stock_df = df[(df['Stock'] == stock) & (df['Factor'] == factor)]
            ax.plot(stock_df['Date'], stock_df['Sentiment'], label=factor)

            if f_idx == 0:  # price should be same for all factors, so just plot it once
                ax2 = ax.twinx()
                ax2.plot(stock_df['Date'], stock_df["Price"], color="red", label="Stock price")
                if i == 0:
                    ax2.legend()
                if i % columns == 1:
                    ax2.set_ylabel("Stock price")

        ax.set_title(f"{stock} sentiment")
        if i % columns == 0:
            ax.set_ylabel("Twitter sentiment")

    axs[0].legend()
    plt.xticks(rotation=45)

    if save_figure:
        plots_folder = Path("plots")
        plots_folder.mkdir(exist_ok=True)
        plt.savefig(plots_folder / f"{stock}.png")