import json
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .gemini_utils import model  
import requests
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from .gemini_utils import analyze_document

@api_view(['POST'])
def analyze_url(request):
    url = request.data.get('url')
    if not url:
        return Response({"error": "URL is required"}, status=400)

    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        # Extract main article content
        content = ' '.join(p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'li']))
        
        result = analyze_document(content, url)
        return Response({"analysis": result})
    
    except Exception as e:
        return Response({"error": str(e)}, status=500)
# analyzer/views.py


def extract_json_from_code_block(analysis_text):
    match = re.search(r'```json\s*(\{.*?\})\s*```', analysis_text, re.DOTALL)
    return json.loads(match.group(1)) if match else {}

@api_view(['POST'])
def revise_content(request):
    url = request.data.get('url')
    analysis_text = request.data.get('analysis')

    if not url or not analysis_text:
        return Response({"error": "Both 'url' and 'analysis' fields are required."}, status=400)

    try:
        # Fetch article content
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        original_content = ' '.join(p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'li']))

        # Parse JSON suggestions
        analysis_json = extract_json_from_code_block(analysis_text)

        # Prompt Gemini to revise
        revision_prompt = f"""
You are an AI editor.

Here is a technical article from MoEngage:
---
{original_content}
---

Here is a structured analysis of the article's weaknesses:
{json.dumps(analysis_json, indent=2)}

Please revise the original article to:
- Improve readability for a non-technical marketer
- Apply structural fixes (clarity, grouping, formatting)
- Clarify examples and jargon
- Improve tone and style (simplify, active voice, friendly tone)

Return only the **revised version** of the article.
"""
        revision = model.generate_content(revision_prompt)
        return Response({"revised_article": revision.text})
    
    except Exception as e:
        return Response({"error": str(e)}, status=500)
