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

## Docker Kullanımı

docker compose up --build

## Gereksinimler

Python 3.12+
Flask
SQLAlchemy

## Kimlik Doğrulama

- Kayıt Ol
- Giriş Yap
- Çıkış Yap

## Kullanıcı Akışı

1. Yeni bir hesap kaydedin.

2. Kimlik bilgilerinizle giriş yapın.

3. Görevler sayfasını açın.

4. Görevler oluşturun ve yönetin.

## Güvenlik Notları

Şifreler karma değerler kullanılarak saklanır.

Formlar CSRF desteğiyle korunmaktadır.

## Uygulamayı Çalıştırma

python run.py

## Rotalar

- /auth/register
- /auth/login
- /tasks/

## Docker Konteyneri

Proje, Docker Compose ile başlatılabilir.

## Teknolojiler

- Flask
- SQLAlchemy
- Flask-Login
- Docker

## Son Notlar

Bu proje, Flask tabanlı bir web uygulaması dönem projesi olarak geliştirilmiştir.

Docker ile Çalıştırma
Gereksinimler
Docker Desktop
Docker Compose
Projeyi Çalıştırma
Repoyu klonlayın:
git clone https://github.com/Ferhat-Yilmaz0/task-tracker-project.git
cd task-tracker-project
Docker containerlarını oluşturun ve başlatın:
docker-compose up --build
Tarayıcıdan uygulamaya erişin:
http://127.0.0.1:5000
Containerları Durdurma
docker-compose down
Yeniden Oluşturma
docker-compose up --build
Kullanılan Servisler
Flask Web Application
SQLite Database
Docker Container Environment

Bu yöntem ile uygulama yerel makinede Docker container içerisinde çalıştırılabilir.