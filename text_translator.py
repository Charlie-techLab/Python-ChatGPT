'''
Step 1: Function to translate text
Step 2: Test the function
'''

import openai 
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def translate_text(text, language):
    prompt = f"Translate the text '{text}' to {language}."
    prompt = ""
    response = openai.Completion.create(
        engine = "davinci-002",
        prompt = prompt,
        n = 1, 
        temperature = 0.5,
        max_tokens = 1000
    )

    return response.choices[0].text.strip()

my_text = input('Write the text you want to translate: ')
my_language = input('What language do you want to translate into? ')
translation = translate_text(my_text, my_language)
print(translation)
