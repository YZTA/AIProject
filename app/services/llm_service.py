from transformers import pipeline, set_seed


class LLMService:
    def __init__(self):
        """
        Modeli ve pipeline'ı uygulama başlangıcında bir kez yükler.
        """
        print("LLM Modeli ve pipeline yükleniyor...")
        # "text-generation" pipeline'ı, metin üretme görevleri için en kolayıdır.
        # distilgpt2, hızlı bir demo için harika bir modeldir.
        self.generator = pipeline('text-generation', model='distilgpt2')
        print("LLM Modeli başarıyla yüklendi.")

    def generate_response(self, prompt: str) -> str:
        """
        Verilen prompt'a göre bir metin üretir.
        """
        # Her seferinde aynı sonucu almak için bir seed belirleyebiliriz (opsiyonel)
        set_seed(42)

        # Modeli kullanarak metin üretme
        # max_length: Üretilecek metnin maksimum uzunluğu
        # num_return_sequences: Kaç farklı cevap üretileceği
        results = self.generator(prompt, max_length=50, num_return_sequences=1)

        # Pipeline bir liste döndürür, biz ilk elemanı alıyoruz
        return results[0]['generated_text']

# Projenin her yerinden erişmek için bir singleton nesne oluşturabiliriz
# AMA BİZ DAHA İYİ BİR YÖNTEM KULLANACAĞIZ (FastAPI Lifespan)