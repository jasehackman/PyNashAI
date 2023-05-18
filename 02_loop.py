import openai
import os
from rich.console import Console
from useful import query_completions_model

console = Console()

openai.api_key = os.getenv("OPENAI_API_KEY")

# In this step we are adding a loop to have a continuous conversation with the model

while True:
    prompt = input("Prompt: ")
    if prompt == "quit":
        print("Goodbye!")
        break
    print(query_completions_model(prompt))
