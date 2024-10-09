import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def get_response(system , prompt = None):

    model = genai.GenerativeModel(
    model_name= "gemini-1.5-flash",
    generation_config= generation_config,
    system_instruction= system,
    )

    chat_session = model.start_chat(
        history=[]
    )

    response = chat_session.send_message(prompt)
    model_response = response.text
    
    return model_response
