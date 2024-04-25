import os
import openai 
import spacy
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Preparing the request
model = "davinci-002" 
prompt = "Cuentame una breve historia feliz de un viaje a Rusia"

# Send the request
answer = openai.Completion.create(
    engine = model,
    prompt = prompt,
    n = 3,
    temperature = 0.1,
    max_tokens = 100
)

for index, option in enumerate(answer.choices):
    generated_text = option.text.strip()
    print(f'Answer {index + 1}: {generated_text}\n')

'''
Processing and analyzing answers from ChatGPT

Step 1: Analyze the answer 

Step 2: Use the extracted information

Step 3: Iterate and improve the interaction
'''

#Natural Language Processing in Spanish
print('***')
spacy_model = spacy.load('es_core_news_md')
analysis = spacy_model(generated_text)

# for token in analysis:
#     print(token.text, token.pos_, token.dep_, token.head.text)

# print('***')

# for ent in analysis.ents:
#     print(ent.text, ent.label_)

for ent in analysis.ents:
    if ent.label_ == 'LOC':
        location = ent
        break 

if location:
    prompt2 = f'Tell me more about {location}'
    answer2 = openai.Completion.create(
        engine = model.capitalize,
        prompt = prompt2,
        n = 3,
        max_tokens = 100 
    )
    print(answer2.choices[0].text.strip())
