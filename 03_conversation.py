import openai
import os
from useful import query_completions_model


openai.api_key = os.getenv("OPENAI_API_KEY")

# In this step we are adding chat history so the model has context

message_history = ""
while True:
    prompt = input("Prompt: ")
    if prompt == "quit":
        print("Goodbye!")
        break
    message_history += prompt
    response = query_completions_model(message_history)
    print(response)
    message_history += response
