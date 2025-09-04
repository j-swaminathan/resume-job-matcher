from fastapi import FastAPI, UploadFile, Form
from models.tfidf_model import tfidf_match
from models.embedding_model import embedding_match
from utils.clean_text import clean_text
import PyPDF2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/match/")
async def match_resume(
    resume: UploadFile,
    job_desc: UploadFile,
    model: str = Form("tfidf")
):
    # Read resume PDF
    pdf_reader = PyPDF2.PdfReader(resume.file)
    resume_text = "".join([page.extract_text() for page in pdf_reader.pages])

    # Read job description TXT
    job_text = job_desc.file.read().decode("utf-8")

    # Clean both
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    # Select model
    if model == "tfidf":
        score, keywords = tfidf_match(resume_clean, job_clean)
    else:
        score, keywords = embedding_match(resume_clean, job_clean)

    return {"model": model, "score": score, "keywords": keywords}
