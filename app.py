from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db
from routes.auth_routes import auth_bp

from routes.protected_routes import protected_bp

# 1. إنشاء تطبيق Flask
app = Flask(__name__)

# 2. تحميل الإعدادات من config.py
app.config.from_object(Config)

# 3. ربط قاعدة البيانات مع التطبيق
db.init_app(app)

# 4. تفعيل JWT
jwt = JWTManager(app)

# 5. تفعيل CORS للسماح بالوصول من متصفحات مختلفة
CORS(app)

# 6. تسجيل المسارات (Blueprints)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(protected_bp, url_prefix='/api')

# 7. نقطة البداية لتشغيل التطبيق
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # إنشاء الجداول في قاعدة البيانات إن لم تكن موجودة
    app.run(debug=True)
