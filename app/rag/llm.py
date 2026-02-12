import google.generativeai as genai
from app.core.config import settings


genai.configure(api_key=settings.GEMINI_KEY)
    
llm = genai.GenerativeModel("gemini-2.5-flash")

# response = llm.generate_content("What is the capital of France? give me some places to simit in the city")
# print(response.text)

