import openai 
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def classify_text(text):
    categories = [
        'art',
        'science',
        'sports',
        'economy',
        'education',
        'entertainment',
        'environment',
        'politic',
        'health',
        'technology'
    ]

    prompt = f"Please, classify the following text: '{text}' in one of these categories: {','.join(categories)}. The category is: "
    answer = openai.Completion.create(
        model = "davinci-002",
        prompt = prompt, 
        n = 1, 
        max_tokens = 50, 
        temperature = 0.5
    )

    return answer.choices[0].text.strip()

text_to_classify = input("Enter a text: ")
classification = classify_text(text_to_classify)
print(classification)
