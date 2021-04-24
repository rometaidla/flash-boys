# flash-boys

### Create conda environment:

```bash
conda create -n flash-boys python=3.6
pip install git+https://github.com/rometaidla/alphalens
conda config --add channels conda-forge
conda config --add channels intel
conda install matplotlib numpy pandas scipy seaborn jupyter nltk ratelimit bs4 scikit-learn
conda activate flash-boys
```

### Running
```bash
git checkout git@github.com:rometaidla/flash-boys.git
jupyter notebook
```

### Notebooks:
- project_10k_sec_reports.ipynb: pipeline using SEC 10k reports
- examples/daily_factor_synthetic_data.ipynb: example alphalens pipeline (taken from alphalens git repository) 