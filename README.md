# LLM Entegreli FastAPI Projesi

Bu proje, bir Büyük Dil Modeli (LLM) içeren profesyonel bir FastAPI web uygulamasıdır.

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

1.  **Sanal Ortam Oluşturma ve Aktive Etme:**
    ```bash
    # Sanal ortamı oluştur
    python -m venv .venv

    # Sanal ortamı aktive et (Windows için: .venv\Scripts\activate)
    source .venv/bin/activate
    ```

2.  **Bağımlılıkları Yükleme:**
    ```bash
    # Gerekli tüm kütüphaneleri yükle
    pip install -e .[dev]
    ```

3.  **Ortam Değişkenlerini Ayarlama:**
    *   Proje ana dizininde `.env` adında bir dosya oluşturun.
    *   `.env.example` dosyasını referans alarak kendi PostgreSQL veritabanı bilgilerinizi girin. (Bu adımı eklemek için projenize bir `.env.example` dosyası da ekleyebilirsiniz, bu iyi bir pratiktir.)

## Veritabanı Yönetimi (Alembic)

Veritabanı şemasında bir değişiklik yaptığınızda (örn: yeni bir model eklediğinizde) aşağıdaki komutları kullanın.

*   **Yeni Migration Oluşturma:**
    ```bash
    alembic revision --autogenerate -m "Yaptığınız değişikliğin kısa açıklaması"
    ```

*   **Migration'ı Veritabanına Uygulama:**
    ```bash
    alembic upgrade head
    ```

## Uygulamayı Çalıştırma

*   **Geliştirme Sunucusu:**
    ```bash
    uvicorn app.main:app --reload
    ```
    Uygulama `http://127.0.0.1:8000` adresinde çalışmaya başlayacaktır.

## Testleri Çalıştırma

Projenin testlerini çalıştırmak için aşağıdaki komutu kullanın:
```bash
pytest
