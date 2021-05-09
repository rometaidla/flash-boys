# snscrape needs python >= 3.8
#!pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

import os
import pandas as pd
import snscrape.modules.twitter as sntwitter

ticker = "GME"
since = "2021-01-01"
until = "2021-01-03" # exclusive
folder = "tweets3"

for date in pd.date_range(since, until)[:-1]:
    search = f'"${ticker}" lang:en since:{date.date()} until:{date.date() + pd.Timedelta(days=1)} -filter:replies'
    print(f"Starting scraping for day {date.date()} ...")
    print("Search query is:", search)
    # get_items() returns generator
    scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()
    try:
        df = pd.DataFrame(scraped_tweets)[["url", "date", "content"]]
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder,f"{ticker}_{date.date()}.csv")
        df.to_csv(filename, index=False)
        print(f"Tweets saved to file {filename}")
        print(f"Tweet dataframe shape is {df.shape}")
    except KeyError:
        print(f"No tweets for day {date.date()}")

    print(f"Finished scraping for day {date.date()}")
    