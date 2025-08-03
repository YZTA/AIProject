import google.generativeai as genai
from app.core.config import settings

# Google Gemini'yi API anahtarımızla yapılandırıyoruz
genai.configure(api_key=settings.GEMINI_API_KEY)

# Gemini modelini seçiyoruz. 'gemini-pro' metin görevleri için idealdir.
model = genai.GenerativeModel('gemini-pro')


def analyze_comment_with_gemini(comment_text: str) -> dict:
    """
    Verilen yorum metnini Gemini kullanarak analiz eder ve yapılandırılmış
    bir sözlük olarak sonucu döndürür.
    """
    # Gemini'ye ne yapacağını net bir şekilde anlatan prompt'u hazırlıyoruz.
    # Sonucun JSON formatına yakın olmasını istiyoruz.
    prompt = f"""
    Analyze the following book review and provide the sentiment and a brief summary.
    The sentiment must be one of: 'Positive', 'Negative', 'Neutral'.
    The summary should be a concise, one-sentence explanation of the user's main point.

    Review: "{comment_text}"

    Output format should be like this, and only this:
    Sentiment: [The sentiment]
    Summary: [The summary]
    """

    try:
        # Gemini API'sine isteği gönderiyoruz
        response = model.generate_content(prompt)

        # Gelen cevabı ayrıştırıyoruz
        analysis_text = response.text
        sentiment = "Unknown"
        summary = "Could not generate summary."

        sentiment_match = re.search(r"Sentiment:\s*(Positive|Negative|Neutral)", analysis_text, re.IGNORECASE)
        if sentiment_match:
            sentiment = sentiment_match.group(1).capitalize()

        summary_match = re.search(r"Summary:\s*(.*)", analysis_text, re.IGNORECASE)
        if summary_match:
            summary = summary_match.group(1).strip()

        return {"sentiment": sentiment, "summary": summary}

    except Exception as e:
        print(f"Gemini API Error: {e}")
        return {"sentiment": "Error", "summary": f"Analysis failed: {str(e)}"}


# Gemini'nin regex import'una ihtiyacı var.
import re