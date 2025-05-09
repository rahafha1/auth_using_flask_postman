import os

class Config:
    # مفتاح التشفير العام للتطبيق (ضروري لـ Flask و JWT)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')

    # إعداد قاعدة البيانات - SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # إعداد مفتاح JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')

    # إعدادات البريد الإلكتروني 
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  # من .env
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')  # من .env
