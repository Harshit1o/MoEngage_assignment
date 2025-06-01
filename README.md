# DocAnalyzer - AI-Powered Document Analysis

![DocAnalyzer Banner](https://img.shields.io/badge/DocAnalyzer-AI%20Document%20Analysis-blue?style=for-the-badge)

[![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![REST API](https://img.shields.io/badge/REST%20API-005571?style=flat-square&logo=fastapi&logoColor=white)](https://www.django-rest-framework.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-43853D?style=flat-square&logo=python&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/)

## 🚀 Overview

DocAnalyzer is an intelligent document analysis system that leverages Large Language Models (LLMs) to analyze technical content and make it more accessible to non-technical audiences. This project was developed as part of the **MoEngage Internship Assignment** to demonstrate the power of AI in content optimization.

The system can analyze technical articles, identify areas for improvement, and automatically revise content to enhance readability, clarity, and engagement.

## ✨ Features

- **URL-based Content Analysis**: Analyze any web article by simply providing its URL
- **AI-Powered Document Assessment**: Leverages Google's Gemini model to evaluate content
- **Intelligent Content Revision**: Automatically improves technical articles for non-technical audiences
- **REST API Integration**: Easy-to-use API endpoints for seamless integration

## 🧠 AI Technology Stack

### Large Language Models (LLMs)

This project harnesses the power of Google's Gemini, a state-of-the-art large language model designed to understand context, analyze text, and generate human-quality content. LLMs like Gemini represent a breakthrough in AI capabilities:

- **Natural Language Understanding**: Comprehends text with near-human level accuracy
- **Context Awareness**: Maintains understanding across long documents
- **Domain Adaptation**: Can be specialized for specific content types and industries

### AI Agents

The system implements AI agents that work together to analyze and optimize content:

- **Analyzer Agent**: Evaluates content structure, readability, jargon usage, and overall clarity
- **Revision Agent**: Transforms technical content based on analysis feedback

## 🛠️ Technical Architecture

- **Backend**: Django + Django REST Framework
- **AI Integration**: Google Gemini API
- **Web Scraping**: BeautifulSoup4
- **Text Processing**: Python's native regex and text processing capabilities

## 📋 Installation & Setup

1. Clone the repository:
   ```bash
   git clone 😎
   cd docanalyzer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # For Windows PowerShell
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 🔍 Usage

### API Endpoints

#### 1. Analyze URL Content
```bash
POST /api/analyze-url/
```
Request body:
```json
{
  "url": "https://example.com/technical-article"
}
```
Response:
```json
{
  "analysis": {
    "readability_score": 65,
    "technical_jargon_density": "high",
    "structural_issues": ["long paragraphs", "inconsistent headings"],
    "improvement_suggestions": [...]
  }
}
```

#### 2. Revise Content
```bash
POST /api/revise-content/
```
Request body:
```json
{
  "url": "https://example.com/technical-article",
  "analysis": "Analysis text from previous endpoint"
}
```
Response:
```json
{
  "revised_article": "The revised, more accessible content..."
}
```

### Example Workflow

1. Submit a technical article for analysis
2. Review the AI's assessment
3. Generate a revised version optimized for non-technical readers

## 🔄 How It Works

1. **Content Extraction**: When a URL is submitted, the system uses BeautifulSoup to extract the main content
2. **Analysis Phase**: The Google Gemini model evaluates the content based on multiple factors
3. **Structured Feedback**: The analysis is returned as structured data
4. **Content Revision**: Using the analysis as guidance, the AI generates an improved version

## 🌟 MoEngage Internship Assignment

This project was developed as part of the MoEngage Internship Assignment, demonstrating capabilities in:

- Full-stack development with Django
- AI integration via the Gemini API
- REST API design and implementation
- Text processing and analysis
- Modern software architecture principles

## 📝 License

This project is intended for educational and demonstration purposes.

## 🙏 Acknowledgments

- Google's Gemini API for powerful AI capabilities
- Django and Django REST Framework for robust backend infrastructure
- MoEngage for the opportunity to demonstrate these skills

---

<div align="center">
  <strong>Built with 💻 and ❤️ by Harshit</strong>
</div>
