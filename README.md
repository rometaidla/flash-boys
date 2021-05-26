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
- alphalens: pipeline using sentiments from Twitter and Reddit
- project_10k_sec_reports.ipynb: pipeline using SEC 10k reports
- roberta-sentiment: notebook for analysising Twitter tweets using RoBERTa model
- scapers/twitter-scraper: notebook for scraping Twitter tweets
