import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_completions_model(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5
    )
    response_text = response["choices"][0]["text"].strip()
    return response_text

def query_chat_model(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    response_text = response["choices"][0]["message"]["content"].strip()
    return response_text