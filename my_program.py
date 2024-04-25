'''
Connecting to the OpenAI API

Step 1: Install the OpenAI library with the command
pip install openai

Step 2: Import and configure the API key
using import openai and openai.api_key = api_key

Step 3: Verify the connection
'''

import os
import openai 
from dotenv import load_dotenv 

load_dotenv()

# Configure the API key 
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Verify the connection
models = openai.Model.list()
print(models)
