'''
Step 1: Create variables
Step 2: Store conversations
Step 3: Develop the functionality
'''

import openai 
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key 

previous_questions = []
previous_answers = []

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
historical_conversation = ""
while True:
    user = input("\nYou: ")
    if user.lower() == 'quit':
        break

    for question, answer in zip(previous_questions, previous_answers):
        historical_conversation += f'User asks: {question}\n'
        historical_conversation += f"ChatGPT answers: {answer}\n"

    prompt = f"The user asks: {user}\nChatGPT answers: "
    historical_conversation += prompt
    answer_from_gpt = ask_chat_gpt(historical_conversation)
    print(f'{answer_from_gpt}')
    
    previous_questions.append(user)
    previous_answers.append(answer_from_gpt)
