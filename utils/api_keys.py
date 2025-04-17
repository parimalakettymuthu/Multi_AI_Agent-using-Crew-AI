
import os 
def get_openai_api_key():
    api_key = os.environ.get("OPENAI_API_KEY")
    return api_key