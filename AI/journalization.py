import google.generativeai as genai
import os


with open('Data/geminiapi.dat', 'r') as f:
    api_key = f.read()

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

def journalize():
    with open(rf"Data/record.dat", "r", encoding="utf-8") as f:
        conversation = f.read()

    prompt  = f"Rewrite the narrative into a diary entry. Highlight the user's key experiences, emotions, and reflections as shared in the narrative. Craft a narrative that accurately reflects the user's story, avoiding assumptions or additions. Maintain a natural and engaging style:\n{conversation}"
    
    journal = model.generate_content(prompt).text

    return journal

