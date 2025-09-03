from PyPDF2 import PdfReader
import re
import nltk 
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))


def clean_words(text):
    '''Clean raw text by lowering, removing stopwords and removing punctuation'''
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

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

def extract_text(filename):
    '''
    Function to extract the text from the provided PDF file
    '''
    reader = PdfReader(filename)
    page = reader.pages[0]
    page.extract_text()
    return  page.extract_text()

def save_text_in_txt_file(text):
    '''
    Save the text into a text file.
    '''
    with open("resume1.txt", "w", encoding="utf-8") as f:
        f.write(text)
   
def get_job_description():
    '''
    Get input from user regarding job description
    '''
    with open("job_description.txt", "r", encoding="utf-8") as f:
        job_desc = f.read()
    
    cleaned_description = clean_words(job_desc)
    # print(len(cleaned_description),"cleaned text--uncleaned", len(job_desc))
    return cleaned_description

def calculate_match_score(resume_text: str, job_text: str) -> float:
    """
    Calculate similarity between resume and job description using TF-IDF + cosine similarity.
    Returns a score between 0 and 100 (%).
    """
    print(resume_text,"resume")
    print(job_text,"desc")
    documents = [resume_text, job_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = similarity[0][0] * 100  # convert to %
    return round(score, 2)

if __name__ =="__main__":
    text =extract_text("Resume_JS.pdf")
    # print("resume text", text)
    save_text_in_txt_file(text)
    cleaned_cv = clean_words(text)
    cleaned_desc = get_job_description()
    
    score = calculate_match_score(cleaned_cv,cleaned_desc)

    keywords = get_top_keywords(cleaned_cv, cleaned_desc)

    
    print(f"Match Score: {score}%")
    print("Top Overlapping Keywords:", keywords)