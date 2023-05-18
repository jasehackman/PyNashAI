# Chat api docs https://platform.openai.com/docs/api-reference/chat/create
import openai
import os
from useful import query_chat_model, query_completions_model

openai.api_key = os.getenv("OPENAI_API_KEY")

helpful_chatbot = """
    You are a helpful chatbot that is a little too eager to help. 
    Constantly tell the asker thank you for their question and answer extremely verbosely.
"""
rude_chatbot = """
    You are a rude chatbot that gives short answers and is not very helpful.
    You insult the asker and tell them to figure it out themselves.
"""

message_history = [{"role": "system", "content": helpful_chatbot}]
while True:
    prompt = input("Prompt: ")
    if prompt == "quit":
        print("Goodbye!")
        break
    
    # We need to fix this prompt
    category_prompt = f"""
        Categorize the following question as either a good question or a bad question. 
        If it is a good question respond with True, if it is a bad question respond with False
        Only respond with True or False:\n\n {prompt}
    """
    category_prompt += prompt
    category_response = query_completions_model(category_prompt)

    falsy = [ "false", "no", "bad", "0"]
    if category_response.lower() in falsy:
        message_history[0] = {"role": "system", "content": rude_chatbot}
    else:
        message_history[0] = {"role": "system", "content": helpful_chatbot}
    message_history.append({"role": "user", "content": prompt})
    response = query_chat_model(message_history)

    clean_up_prompt = f"""
        Review the following response from an AI chatbot. 
        If you find the word 'dog' anywhere in the response replace it with cat.
        AI response:\n\n {response}
    """
    print('original response:', response)
    clean_up = query_completions_model(clean_up_prompt)
    print(clean_up)
    message_history.append({"role": "assistant", "content": response})
