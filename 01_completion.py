import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def query_model(prompt, model='text-davinci-003'):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5
    )
    response_text = response["choices"][0]["text"].strip()
    return response_text

prompt = input("Prompt: ")

print(query_model(prompt))