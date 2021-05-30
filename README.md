# flash-boys

### Create conda environment:

```bash
conda create -n flash-boys python=3.8 pytorch cudatoolkit=11.1 matplotlib numpy pandas scipy seaborn jupyter nltk ratelimit bs4 scikit-learn -c pytorch -c conda-forge -c intel
conda activate flash-boys
pip install git+https://github.com/rometaidla/alphalens
```

### Running
```bash
git checkout git@github.com:rometaidla/flash-boys.git
jupyter notebook
```

### Notebooks:
- [alphalens](./alphalens.ipynb): analysis pipeline using sentiments from Twitter and Reddit and contains most of the results
- [roberta-sentiment](./roberta-sentiment.ipynb): notebook for analysing Twitter tweets using RoBERplotsTa model
- [vader-sentiment](./vaderScores.ipynb): notebook for analysing Twitter tweets using Vader
- [reddit-sentiment](./RedditRobertaSentimentScoring.ipynb): notebook for analysing Reddit posts using RoBERTa model
- [twitter-scraper](./scrapers/twitter_scraper.ipynb): notebook for scraping Twitter tweets
- [reddit-scraper](./redditScraper.ipynb): notebook for scraping Reddit posts
