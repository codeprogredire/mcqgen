import os
import json
import pandas as pd
import traceback

from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv() #takes environment variables from env

import os
KEY=os.getenv('OPENAI_API_KEY')

#print(KEY)


llm=ChatOpenAI(openai_api_key=KEY,
               model_name='got-3.5-turbo',
               temperature=0.5)





