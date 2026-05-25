from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_similarity(job_description, resumes):

    # Convert job description into AI embeddings
    job_embedding = model.encode([job_description])

    # Convert resumes into embeddings
    resume_embeddings = model.encode(resumes)

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        job_embedding,
        resume_embeddings
    )[0]

    return similarity_scores