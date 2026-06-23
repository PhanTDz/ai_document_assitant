import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")


def ask_gemini(context, question):
    prompt = f"""
    Bạn là AI Document Assistant.

    Hãy trả lời câu hỏi dựa trên tài liệu bên dưới.

    Tài liệu:
    {context}

    Câu hỏi:
    {question}
    """

    response = model.generate_content(prompt)
    return response.text