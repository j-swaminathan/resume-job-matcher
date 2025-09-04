import re
import nltk 
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def clean_text(text):
    '''Clean raw text by lowering, removing stopwords and removing punctuation'''
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)