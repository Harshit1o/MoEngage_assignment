# analyzer/gemini_utils.py
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

def analyze_document(content, url):
    prompt = f"""
You are an AI documentation improvement assistant. Analyze the following documentation content from the given URL:
URL: {url}

CONTENT:
{content}

Return a structured report with:
- Readability for a marketer (score + explanation + improvement suggestions)
- Structure and flow (explanation + issues + suggestions)
- Completeness (missing info, unclear parts, example quality)
- Style guide adherence (voice, tone, clarity, jargon)
Use a JSON format with keys: "url", "readability", "structure", "completeness", "style".
    """
    response = model.generate_content(prompt)
    return response.text
