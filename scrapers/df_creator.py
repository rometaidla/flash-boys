# create one dataframe from tweets and add cashtag
import os
import re
import pandas as pd

folder = "./tweets"
filepaths = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

dfs = [pd.read_csv(os.path.join(folder, f)).assign(cashtag=re.search("^([A-Z]+)_", f)[1]) for f in filepaths]

df = pd.concat(dfs, ignore_index=True)
df.to_csv('all_tweets.csv')