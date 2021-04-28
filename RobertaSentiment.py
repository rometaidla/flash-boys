from transformers import pipeline
import csv
import urllib.request
import torch

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"


class RobertaSentimentModel:

    def __init__(self):
        self.pipeline = pipeline('sentiment-analysis',
                                 model=MODEL_NAME,
                                 tokenizer=MODEL_NAME,
                                 return_all_scores=True, device=torch.cuda.current_device())

        self.download_label_mapping()

    def score(self, texts):
        processed_texts = [self.preprocess(t) for t in texts]
        scores = [self.extract_scores(score) for score in self.pipeline(processed_texts)]
        return scores

    def extract_scores(self, score):
        negative_score = score[self.labels.index('negative')]['score']
        neutral_score = score[self.labels.index('neutral')]['score']
        positive_score = score[self.labels.index('positive')]['score']
        total_score = positive_score + -1.0 * negative_score

        return {
            "negative_score": negative_score,
            "neutral_score": neutral_score,
            "positive_score": positive_score,
            "total_score": total_score
        }

    def preprocess(self, text):
        new_text = []

        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    # Preprocess text (username and link placeholders)
    def download_label_mapping(self):
        # download label mapping
        mapping_link = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt"
        with urllib.request.urlopen(mapping_link) as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')
        self.labels = [row[1] for row in csvreader if len(row) > 1]
