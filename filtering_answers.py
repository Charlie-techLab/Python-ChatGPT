'''
Step 1: Variables and configuration
Step 2: Function to filter words
Step 3: Intercept answers
'''

import openai 
import os 
import spacy
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key 

previous_questions = []
previous_answers = []
spacy_model = spacy.load("es_core_news_md")
forbidden_words = ['word1', 'word2']

def filter_words(text, black_list):
    token = spacy_model(text)
    result = []

    for t in token:
        if t.text.lower() not in black_list:
            result.append(t.text)
        else:
            result.append("[***]")

    return " ".join(result)


def ask_chat_gpt(prompt, model="davinci-002"):
    answer = openai.Completion.create(
        engine = model,
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        temperature = 1.5
    )

    answer_without_filter = answer.choices[0].text.strip()
    filtered_answer = filter_words(answer_without_filter, forbidden_words)
    return filtered_answer

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
