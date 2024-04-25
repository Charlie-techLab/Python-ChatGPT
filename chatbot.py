'''
Step 1: Import libraries and set up the key
Step 2: Function for processing requests
Step 3: Basic functionality
Step 4: Execute the chatbot
'''

import openai 
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key 

def ask_chat_gpt(prompt, model="davinci-002"):
    answer = openai.Completion.create(
        engine = model,
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        temperature = 1.5
    )

    return answer.choices[0].text.strip()

print("Welcome to the chatbot. Write 'quit' when you want to exit")
while True:
    user = input("\nYou: ")
    if user.lower() == 'quit':
        break

    prompt = f"The user asks: {user}\nChatGPT answers: "
    answer_from_gpt = ask_chat_gpt(prompt)
    print(f"Chatbot: {answer_from_gpt}")
