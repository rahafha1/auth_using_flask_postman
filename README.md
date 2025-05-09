# 🛡️ User Authentication API using Flask

This project is a simple yet complete user authentication system built using **Flask**, including registration, login with JWT tokens, protected routes, and basic email welcome (printed to console).

## 🚀 Features

- User Registration with password hashing
- User Login with JWT Token (expires in 1 hour)
- Protected route that returns user profile
- Email welcome message (simulated via console print)
- Clean project structure using Blueprints
- SQLite database
- CORS enabled for cross-origin frontend requests

---

## ⚙️ Tech Stack

- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-CORS
- Werkzeug security
- SQLite
- Postman (for testing)

---

## 📂 Project Structure

project/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
│
├── routes/
│ ├── init.py
│ ├── auth_routes.py
│ └── protected_routes.py



---

## 🧪 API Endpoints

### 🔐 Authentication Routes

#### `POST /auth/register`

Register a new user.

- **Body (JSON)**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
  }


# Responses :

201 Created: User created

409 Conflict: Email already used

400 Bad Request: Missing fields

POST /auth/login
Login with email and password.


# Body(JSON) :

{
  "email": "john@example.com",
  "password": "securepassword"
}

Responses :
200 OK: Returns JWT token

401 Unauthorized: Invalid credentials


### Protected Routes:
GET /api/profile
Returns user profile data. Requires JWT token in the header.

# header:
Authorization: Bearer <your_token>
 Response:
 {
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-05-01T12:34:56"
}

##### Setup & Run:
1- Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2-Create virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
3-Create .env file (optional):
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
4-Run the app:
python app.py



##### Requirements
Create a requirements.txt using:
pip freeze > requirements.txt

