import json
import openai
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_embedding(input_val):
    response = openai.Embedding.create(
        input=input_val,
        model="text-embedding-ada-002",
    )
    return response["data"]

# Read and parse the JSON data from the file
with open('pokemon.json', 'r') as file:
    data = json.load(file)

# Access the pokedex array
pokedex = data['pokedex']

pokedex_strings = [json.dumps(pokemon) for pokemon in pokedex]

# Get the embeddings for each pokemon
data = get_embedding(pokedex_strings)
# Zip the pokedex and embeddings together
pokedex_embeddings_zip = [(pokedex_entry, embedding["embedding"]) for pokedex_entry, embedding in zip(pokedex, data)]


while True:
    # Ask the user for a question
    question = input("Ask me about a pokemon: ")
    # Get the embedding for the question
    question_embedding = get_embedding(question)[0]["embedding"]

    # Calculate the similarity between the question and each pokemon
    similarities = []
    for pokedex_string, embedding in pokedex_embeddings_zip:
        # Calculate the cosine similarity between the question and the pokemon
        similarity = cosine_similarity(question_embedding, embedding)
        similarities.append((pokedex_string, similarity))
    # Sort the similarities by the highest similarity
    similarities.sort(key=lambda x: x[1], reverse=True)
    # Print the top 5 results
    results = [(pokedex_entry["name"], similarity) for pokedex_entry, similarity in similarities[:5]]
    print(results)