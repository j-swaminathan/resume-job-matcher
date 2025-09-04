from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_top_keywords(resume_text: str, job_text: str, top_n: int = 10):
    """
    Returns top_n keywords that overlap between resume and job description.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_text])

    feature_names = vectorizer.get_feature_names_out()
    resume_vector = tfidf_matrix.toarray()[0]
    job_vector = tfidf_matrix.toarray()[1]

    # Take min weight (common importance in both)
    common_weights = np.minimum(resume_vector, job_vector)

    top_indices = common_weights.argsort()[-top_n:][::-1]
    top_keywords = [feature_names[i] for i in top_indices if common_weights[i] > 0]

    return top_keywords


def tfidf_match(resume_text: str, job_text: str) -> float:
    """
    Calculate similarity between resume and job description using TF-IDF + cosine similarity.
    Returns a score between 0 and 100 (%).
    """
    documents = [resume_text, job_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = similarity[0][0] * 100  # convert to %
    keywords = get_top_keywords(resume_text, job_text)
    return round(score, 2),keywords