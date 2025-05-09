from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import db, User
import datetime

auth_bp = Blueprint('auth', __name__)

# ✅ تسجيل مستخدم
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'message': 'all fields are required'}), 400

    # التأكد من عدم تكرار الإيميل
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 409

    # تشفير الباسورد
    hashed_password = generate_password_hash(password)

    # إنشاء مستخدم جديد
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # طباعة إيميل ترحيبي (حاليًا فقط طباعة)
    print(f"📧 Welcome {name}! You have successfully registered. (Email sent to: {email})")

    return jsonify({'message': 'User created successfully ✅'}), 201

# ✅ تسجيل الدخول
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Please provide email and password'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password ❌'}), 401

    # إنشاء JWT
    access_token = create_access_token(identity=str(user.id), expires_delta=datetime.timedelta(hours=1))

    return jsonify({'access_token': access_token}), 200
