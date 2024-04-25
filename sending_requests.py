'''
Make basic requests to ChatGPT

Step 1: Prepare the request
Step 2: Send the request
Step 3: Process and show the answer
'''

import os
import openai 
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Preparing the request
model = "davinci-002" 
prompt = "Give me a good name for a raccoon"

# Send the request
answer = openai.Completion.create(
    engine = model,
    prompt = prompt,
    n = 3,
    temperature = 0.1,
    max_tokens = 100
)

# Process and show the answer (when there is only one answer)
#generated_text = answer.choices[0].text.strip()
#print(generated_text)

'''
Fine-tuning requests

Step 1: Temperature (creatividad)
less creative -> 0.1
more creativity -> 1

Step 2: Maximum tokens (length)

Step 3: Quantity of answers
'''

for index, option in enumerate(answer.choices):
    generated_text = option.text.strip()
    print(f'Answer {index + 1}: {generated_text}\n')

'''
Processing and analyzing answers from ChatGPT

Step 1: Analyze the answer 

Step 2: Use the extracted information

Step 3: Iterate and improve the interaction
'''
