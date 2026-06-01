# Task Tracker

Flask ile geliştirilmiş basit görev takip uygulaması.

## Özellikler

- Kullanıcı kayıt / giriş / çıkış
- Şifre hashleme
- Kullanıcıya özel görev listeleme
- Görev ekleme, tamamlama/geri alma ve silme
- Flask Blueprint yapısı
- SQLite veritabanı
- Docker ile çalıştırma desteği

## Yerel Çalıştırma

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Tarayıcıdan aç:

```text
http://127.0.0.1:5000
```

## Docker ile Çalıştırma

```powershell
docker compose up --build
```

Tarayıcıdan aç:

```text
http://127.0.0.1:5000
```

## Ana Sayfalar

- Kayıt: `/auth/register`
- Giriş: `/auth/login`
- Görevler: `/tasks/`


## Proje Özellikleri

- Kullanıcı Kimlik Doğrulaması
- Görev Yönetimi
- Docker Desteği