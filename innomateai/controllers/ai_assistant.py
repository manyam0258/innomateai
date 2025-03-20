"""from google import genai
import google.generativeai as genai

import frappe
from frappe.utils import today
from pydantic import BaseModel

class Response(BaseModel):
    message: str

class AiAssistant:
    def __init__(self):
        apiKey = frappe.db.get_single_value("ChatBot Settings","gemini_api_key")
        self.client = genai.Client(api_key=apiKey)

    def generate_response(self, prompt, chat_history):
        try:
            content = f''' You are a chat assistant on erpnext system server, Today is {today()} and User ask : {prompt},
                chat history is: { chat_history}.
                You don't have access to data.
                give the answer in details.
                '''
            response = self.client.models.generate_content(
                model="gemini-2.0-flash", contents=content,
                config={
                    'response_mime_type': 'application/json',
                    'response_schema': Response,
                },
            )
            return response.text
        except Exception as e:
            return str(e)
"""
import google.generativeai as genai
import frappe
from frappe.utils import today
from pydantic import BaseModel

class Response(BaseModel):
    message: str

class AiAssistant:
    def __init__(self):
        # Fetch API key from ChatBot Settings in ERPNext
        apiKey = frappe.db.get_single_value("ChatBot Settings", "gemini_api_key")

        # ✅ Correctly configure the API
        genai.configure(api_key=apiKey)

        # ✅ Correctly initialize the model
        self.model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro"

    def generate_response(self, prompt, chat_history):
        try:
            # Constructing the prompt with chat history
            content = f"""You are a chatbot assistant for an ERPNext system.
            Today is {today()}, and the chat history is: {chat_history}.
            You don't have access to internal data.
            Please provide a detailed response."""

            # ✅ Generating response
            response = self.model.generate_content(content)

            # ✅ Extract text response
            return response.text
        except Exception as e:
            return str(e)
