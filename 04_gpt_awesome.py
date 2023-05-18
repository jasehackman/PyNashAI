# Chat api docs https://platform.openai.com/docs/api-reference/chat/create
import openai
import os
from useful import query_chat_model

openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = """
    You are a helpful chatbot that is a little too eager to help. 
    Constantly tell the asker thank you for their question and answer extremely verbosely.
"""

message_history = [{"role": "system", "content": system_prompt}]
while True:
    prompt = input("Prompt: ")
    if prompt == "quit":
        print("Goodbye!")
        break
    message_history.append({"role": "user", "content": prompt})
    response = query_chat_model(message_history)
    print(response)
    message_history.append({"role": "assistant", "content": response})
