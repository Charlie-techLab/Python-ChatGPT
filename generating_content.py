'''
Step 1: Function for generating content
Step 2: Function for generating summarizes
Step 3: Test both functions
'''

import openai 
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key 

def create_content(topic, tokens, temperature, model="davinci-002"):
    prompt = f'Please write a short article about: {topic}\nn'
    answer = openai.Completion.create(
        engine = model,
        prompt = prompt,
        n = 1,
        max_tokens = tokens, 
        temperature = temperature
    )
    
    return answer.choices[0].text.strip()

def summarize_text(text, tokens, temperature, model = "davinci-002"):
    prompt = f'Please summarize the following text: {text}'
    answer = openai.Completion.create(
        engine = model,
        prompt = prompt,
        n = 1, 
        max_tokens = tokens, 
        temperature = temperature
    )

    return answer.choices[0].text.strip()

# topic = input('Choose a topic for your article: ')
# tokens = int(input('How many tokens will have your article? '))
# temperature = int(input('From 1 to 10, how creative do you want your article? '))/10

# generated_article = create_content(topic, tokens, temperature)
# print(generated_article)

text_to_summarize = input('Paste here your article to summarize: ')
tokens = int(input('How many tokens will have your article? '))
temperature = int(input('From 1 to 10, how much creative do you want your summary? '))/10

generated_summary = summarize_text(text_to_summarize, tokens, temperature)
print(generated_summary)
