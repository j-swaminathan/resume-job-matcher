from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def embedding_match(resume, job, top_n=10):
    emb1 = model.encode(resume, convert_to_tensor=True)
    emb2 = model.encode(job, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item() * 100
    return round(score, 2),[]
