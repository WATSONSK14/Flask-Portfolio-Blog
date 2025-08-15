# 🚀 Flask Web Portfolio & Social Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

---

## 🇹🇷 Türkçe

### 📋 Proje Açıklaması
Bu proje, **Flask** web framework kullanılarak geliştirilmiş modern bir **blog** uygulamasıdır. Kullanıcıların programlama dilleri hakkında oy kullanabildiği, destek mesajları gönderebildiği interaktif bir web sitesidir.

### ✨ Özellikler
- 🔐 **Kullanıcı Yönetimi**: Kayıt, giriş, profil yönetimi
- 🗳️ **Oylama Sistemi**: Programlama dilleri için like/dislike
- 💬 **İletişim Sistemi**: Destek mesajları ve takip
- 👨‍💼 **Admin Panel**: Kullanıcı ve mesaj yönetimi
- 🎨 **Modern UI**: Bootstrap 5 ile responsive tasarım
- 📱 **Mobil Uyumlu**: Tüm cihazlarda mükemmel görünüm
- 🗄️ **Veritabanı**: SQLAlchemy ile güçlü veri yönetimi

### 🛠️ Teknolojiler
- **Backend**: Flask 2.3.2, SQLAlchemy 2.0.35
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Veritabanı**: SQLite (Development), PostgreSQL (Production)
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF, WTForms
- **Admin**: Flask-Admin
- **Deployment**: Gunicorn, Heroku

### 🚀 Kurulum

#### Gereksinimler
```bash
Python 3.8+
pip
```

#### Adımlar
1. **Repository'yi klonlayın**
```bash
git clone https://github.com/WATSONSK14/flask-portfolio.git
cd flask-portfolio
```

2. **Virtual environment oluşturun**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **Environment variables ayarlayın**
```bash
# .env dosyası oluşturun
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///portfolio.db
```

5. **Veritabanını başlatın**
```bash
flask db init
flask db migrate
flask db upgrade
```

6. **Uygulamayı çalıştırın**
```bash
python main.py
# veya
flask run
```

### 📁 Proje Yapısı
```
flask-portfolio/
├── main.py              # Ana uygulama dosyası
├── models.py            # Veritabanı modelleri
├── forms.py             # Form tanımları
├── admin.py             # Admin panel konfigürasyonu
├── config.py            # Uygulama ayarları
├── requirements.txt     # Python bağımlılıkları
├── Procfile            # Heroku deployment
├── static/             # Statik dosyalar (CSS, JS, resimler)
├── templates/          # HTML şablonları
└── migrations/         # Veritabanı migration dosyaları
```

### 🌐 Sayfalar
- **Ana Sayfa** (`/`) - Carousel ve oylama sistemi
- **Kayıt** (`/register`) - Kullanıcı kaydı
- **Giriş** (`/login`) - Kullanıcı girişi
- **Kullanıcı Paneli** (`/user_panel`) - Profil yönetimi
- **İletişim** (`/contact`) - Destek mesajı gönderme
- **Galeri** (`/gallery`) - Görsel portföy
- **Hakkında** (`/about`) - Bilgi sayfası
- **Admin Panel** (`/admin`) - Yönetim arayüzü

### 🔒 Güvenlik Özellikleri
- Şifre hash'leme (pbkdf2:sha256)
- CSRF koruması
- Admin yetki kontrolü
- Güvenli oturum yönetimi

### 📱 Deployment
```bash
# Heroku için
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

---

## 🇺🇸 English

### 📋 Project Description
This project is a modern **blog** application developed using the **Flask** web framework. It is an interactive website where users can vote on programming languages and send support messages.

### ✨ Features
- 🔐 **User Management**: Registration, login, profile management
- 🗳️ **Voting System**: Like/dislike for programming languages
- 💬 **Communication System**: Support messages and tracking
- 👨‍💼 **Admin Panel**: User and message management
- 🎨 **Modern UI**: Responsive design with Bootstrap 5
- 📱 **Mobile Friendly**: Perfect appearance on all devices
- 🗄️ **Database**: Powerful data management with SQLAlchemy

### 🛠️ Technologies
- **Backend**: Flask 2.3.2, SQLAlchemy 2.0.35
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF, WTForms
- **Admin**: Flask-Admin
- **Deployment**: Gunicorn, Heroku

### 🚀 Installation

#### Requirements
```bash
Python 3.8+
pip
```

#### Steps
1. **Clone the repository**
```bash
git clone https://github.com/WATSONSK14/flask-portfolio.git
cd flask-portfolio
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables**
```bash
# Create .env file
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///portfolio.db
```

5. **Initialize database**
```bash
flask db init
flask db migrate
flask db upgrade
```

6. **Run the application**
```bash
python main.py
# or
flask run
```

### 📁 Project Structure
```
flask-portfolio/
├── main.py              # Main application file
├── models.py            # Database models
├── forms.py             # Form definitions
├── admin.py             # Admin panel configuration
├── config.py            # Application settings
├── requirements.txt     # Python dependencies
├── Procfile            # Heroku deployment
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
└── migrations/         # Database migration files
```

### 🌐 Pages
- **Home** (`/`) - Carousel and voting system
- **Register** (`/register`) - User registration
- **Login** (`/login`) - User login
- **User Panel** (`/user_panel`) - Profile management
- **Contact** (`/contact`) - Send support message
- **Gallery** (`/gallery`) - Visual portfolio
- **About** (`/about`) - Information page
- **Admin Panel** (`/admin`) - Management interface

### 🔒 Security Features
- Password hashing (pbkdf2:sha256)
- CSRF protection
- Admin permission control
- Secure session management

### 📱 Deployment
```bash
# For Heroku
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Katkılarınız bekleniyor! Lütfen Pull Request göndermekten çekinmeyin.**

## 📄 License

This project is currently unlicensed. Please contact the author for usage permissions.

Bu proje şu anda lisanssızdır. Kullanım izinleri için yazarla iletişime geçin.

## 📞 Contact

- **GitHub**: [@WATSONSK14](https://github.com/WATSONSK14)
- **Website**: [Portfolio Project](https://github.com/WATSONSK14/flask-portfolio)

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=WATSONSK14/flask-portfolio&type=Date)](https://star-history.com/#WATSONSK14/flask-portfolio&Date)

---

<div align="center">
  <p>Made with ❤️ by <strong>Serhat Kutlu</strong></p>
  <p>💻 <strong>Flask Web Portfolio</strong></p>
</div>
