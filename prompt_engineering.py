import openai
import os
from rich.console import Console

console = Console()

openai.api_key = os.getenv("OPENAI_API_KEY")

# OpenAI Completions Model
model_engine = "text-davinci-003"

def query_model(prompt, model_engine):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )
    response_text = response["choices"][0]["text"].strip()
    return response_text

def formater(prompt_type, prompt, response_text):
    console.print("")
    console.print(f"[blue underline]{prompt_type}:")
    console.print("")
    console.print("[green underline]Prompt:")
    console.print(prompt)
    console.print("")
    console.print("[green underline]Response:")
    console.print(response_text)
    console.print("")

# Zero Shot
prompt = "Would you recommend Django?"
# formater("Zero Shot", prompt, query_model(prompt, model_engine))


# Role prompting
prompt = """Role: Sr Software Engineer
            "Would you recommend Django?"""
# formater("Role Prompting", prompt, query_model(prompt, model_engine))

# Few Shot

# Zero Shot Chain of Thought
prompt = 'If John has 5 pears, then eats 2, and buys 5 more, then gives 3 to his friend, how many pears does he have?'

# formater(
#     "Zero Shot",
#     prompt,
#     query_model(prompt, model_engine)
# )

chain_of_thought = prompt + " Let's think step by step."
# formater(
#     "Zero Shot with Chain of Thought",
#     chain_of_thought,
#     query_model(chain_of_thought, model_engine)
# )

# Role prompting
role = "You are a math teacher. How would you explain to 5th graders how to find the answer to this question?" + prompt
# formater(
#     "Role Prompting",
#     role,
#     query_model(role, model_engine)
# )

ask = "Write some python code that will return the correct answer." + prompt

formater(
    "Role Prompting",
    ask,
    query_model(ask, model_engine)
)

role = "You are a sr Software Engineer. Write some python code that will return the correct answer." + prompt

formater(
    "Role Prompting",
    role,
    query_model(role, model_engine)
)


