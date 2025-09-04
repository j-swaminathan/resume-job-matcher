Work in Progress

An **AI-powered tool** that compares your resume against job descriptions and generates a **match score** using NLP techniques.  
Helps job seekers quickly understand how well their resume aligns with a given role.  

---

##  Features
- Upload your **resume (PDF)** and **job description (TXT)**
- Choose between multiple models:
  - **TF-IDF** 
  - **Embeddings** 
- Generates:
  - ✅ Match Score (%)
  - ✅ Highlighted Keywords
  - ✅ Model Type Used
- Clean **frontend** with drag-and-drop file uploads

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/j-swaminathan/resume-job-matcher.git
    cd resume-job-matcher 
    ```
2. **Set up a virtual environment in backend:**

    ```bash
    cd backend
    conda create -n ResumeMatcher python=3.11.0
    conda activate ResumeMatcher
    
    ```
3. **Install dependencies:**

```
pip install -r requirements.txt
```

4. **Run backend locally**
```

fastapi dev app.py


```
5. **Run frontend locally**
```
npm install 
npm run dev
```
