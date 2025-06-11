# Test to see whether sentence transformers works like I think it should
from sentence_transformers import SentenceTransformer

# Loading our pretrained model
model = SentenceTransformer("all-MiniLM-L6-v2")
# The sentences we'll be encoding
sentences = ["Why is the sky blue?", "It's hot today!", "She rode a horse to town."]

# Calculate embeddings
embeddings = model.encode(sentences)
print(embeddings.shape)

# Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print(similarities)
