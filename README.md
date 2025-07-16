

* ✅ No pagination yet
* ✅ Updated folder structure with `cart`, `orders`, `reviews`, `products`, `favorites`, `core`, `users`

---

### ✅ Final `README.md`

```markdown
# 🍏 Apple API – Django REST Framework Project

A modular and secure e-commerce-style RESTful API built using Django REST Framework with features like authentication, product and order management, favorites, and more.

---

## 🚀 Features

- 🔐 JWT Authentication (Login, Register, Secure endpoints)
- 📦 Product Management
- 🛒 Cart & Order System
- ❤️ Favorite System
- 🧾 Reviews
- 🧑‍💼 Admin Panel
- 🧪 Swagger (drf-yasg) API Docs
- 💬 Search and Ordering (via query params)

---

## 🧰 Tech Stack

- Python 3.10+
- Django 4.2+
- Django REST Framework
- SimpleJWT for authentication
- SQLite (default) – easy local dev
- drf-yasg for Swagger documentation
- django-cors-headers

---

## 📁 Folder Structure

```

apple\_api/
│
├── cart/
├── orders/
├── reviews/
├── products/
├── favorites/
├── core/
├── users/
├── manage.py
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/yourname/apple_api.git
cd apple_api
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, generate it after installing packages:

```bash
pip install django djangorestframework djangorestframework-simplejwt drf-yasg django-cors-headers Pillow
pip freeze > requirements.txt
```

---

### 4. Migrate the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📑 API Documentation

### Swagger/OpenAPI

* 📄 Swagger UI:
  [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

* 🧬 OpenAPI JSON (for Postman import):
  [http://127.0.0.1:8000/swagger/?format=openapi](http://127.0.0.1:8000/swagger/?format=openapi)

---

## 🔐 Authentication with JWT

### 1. Register a user

**POST** `/api/auth/register/`

```json
{
  "username": "admin",
  "password": "1234"
}
```

### 2. Get JWT token

**POST** `/api/token/`

```json
{
  "username": "admin",
  "password": "1234"
}
```

**Response:**

```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

### 3. Use access token in Postman

* Go to **Authorization tab**
* Type: `Bearer Token`
* Paste the **access token**

Now you can access any protected endpoint.

---

## 🧪 How to Import Swagger into Postman

1. Copy this URL:
   `http://127.0.0.1:8000/swagger/?format=openapi`

2. Open Postman → **Import**

3. Select "Link" → paste the URL above

4. Postman will generate all endpoints ready for use

---

## 🛍️ Create Product via Postman

**POST** `/api/products/`
**Authorization:** Bearer Token
**Body (JSON):**

```json
{
  "name": "iPhone 15",
  "description": "Latest model",
  "price": 999.99,
  "category_id": 1
}
```

---

## 🔧 Notes

* ✅ Pagination: **Not implemented yet**
* ✅ Upload images: Optional (add with `ImageField` and media setup)
* ✅ Deploy with PostgreSQL for production  **Not implemented yet**

---

## 📜 License

MIT © 2025 Riyam

```

---

