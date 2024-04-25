'''
Step 1: Function to make sentiment analyzis
Step 2: Function to classify text
'''

import openai 
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def sentiment_analysis(text):
    prompt = f"Please, analize the predominant sentiment in the following text: '{text}'. The feeling is: "
    answer = openai.Completion.create(
        engine = "davinci-002",
        prompt = prompt,
        n = 1, 
        max_tokens = 100,
        temperature = 0.5
    )

    return answer.choices[0].text.strip()

text_for_analysis = input('Enter a text: ')
sentiment = sentiment_analysis(text_for_analysis)
print(sentiment)
