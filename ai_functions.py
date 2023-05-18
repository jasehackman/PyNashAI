import openai
from rich.console import Console

console = Console()

# Taken from https://github.com/Torantulino/AI-Functions

def ai_function(function, args, description, model = "gpt-4"):
    # parse args to comma separated string
    args = ", ".join(args)
    messages = [{"role": "system", "content": f"You are now the following python function: ```# {description}\n{function}```\n\nOnly respond with your `return` value. Do not include any other explanatory text in your response."},{"role": "user", "content": args}]
    console.print(messages)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message["content"]

function = "def add(a,b):"
args = ["1","4"]
description = "Adds two numbers together"
print(ai_function(function, args, description))

function = "def multiply(a,b):"
args = ["1","4"]
description = "Multiplies two numbers together"
print(ai_function(function, args, description))