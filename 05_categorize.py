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

def query_chat_model(message, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=message
    )
    response_text = response["choices"][0]["message"]["content"].strip()
    return response_text


helpful_prompt = """
    You are a helpful chatbot that is a little too eager to help. 
    Constantly tell the asker thank you for their question and answer extremely verbosely.
"""

rude_chatbot = """
    You are a rude chatbot that gives short answers and is not very helpful.
    You insult the asker and tell them to figure it out themselves.
"""
category_prompt = f"""
        Categorize the following question as either a good question or a bad question. 
        If it is a good question respond with True, if it is a bad question respond with False
        Only respond with True or False. When in doubt respond with True:\n\n
    """

message_history = [{"role": "system", "content": helpful_prompt}]
  
while True:
    prompt = input("Question: ")
    if prompt == "quit":
        print("Goodbye!")
        break
    
    # Categorize the question
    category_prompt += prompt
    category_response = query_completions_model(category_prompt)
    print("Category response:", category_response)

    if category_response.lower() in ["false", "no", "bad", "0"]:
        message_history[0] = {"role": "system", "content": rude_chatbot}
    else:
        message_history[0] = {"role": "system", "content": helpful_prompt}

    message_history.append({"role": "user", "content": prompt})
    response = query_chat_model(message_history)
    print(response)
    message_history.append({"role": "assistant", "content": response})



