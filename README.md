# Island Booking System

An elegant, premium-grade Island Resort Vacation Booking Platform. The backend is powered by **Django REST APIs** communicating with **MongoDB Atlas** via **PyMongo**, while the frontend is constructed using modern responsive **HTML5**, **CSS3**, and **JavaScript (ES6)** Fetch API.

---

## 🚀 Getting Started

### 1. Requirements
Ensure you have Python 3 installed. The following packages are required and can be installed via pip:
```bash
pip install django djangorestframework django-cors-headers pymongo
```

### 2. Run the Django REST API Backend
From the project root directory, run the server on port `8001` (to prevent port conflicts with standard dev channels):
```bash
python manage.py runserver 8001
```
The REST API will initialize and connect to the MongoDB Atlas cluster.

### 3. Run the Frontend Client
You can open the static pages directly in your browser or run a simple local web server to host them:
```bash
cd Frontend
python -m http.server 8000
```
Then visit `http://localhost:8000/` in your web browser.

---

## 🔑 Login Credentials

### Traveler Account
- **Email**: `rahul@gmail.com`
- **Password**: `rahul123`

### Administrator Account
- **Email**: `admin@islandgate.com`
- **Password**: `admin123`

---

## 📂 Project Structure

```text
IslandBookingSystem/
├── Backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── db.py           <-- MongoDB Atlas Connection & CRUD functions
│   ├── settings.py     <-- Django configurations & CORS
│   ├── urls.py         <-- REST Endpoint patterns
│   ├── views.py        <-- Django REST Framework function-based views
│   └── wsgi.py
├── Frontend/
│   ├── index.html               <-- Landing Page & Search
│   ├── login.html               <-- Customer/Admin Auth
│   ├── register.html            <-- Customer Registration
│   ├── islands.html             <-- Island Cards & Climate Filter
│   ├── packages.html            <-- Resort & Package listings
│   ├── booking.html             <-- Travel Date & Guest selection
│   ├── payment.html             <-- Transaction simulation gateway
│   ├── customer_dashboard.html  <-- Upcoming stays, payments & favorite islands
│   ├── admin_dashboard.html     <-- Datatables & CRUD popups
│   ├── style.css                <-- Global styling (glassmorphism UI)
│   └── script.js                <-- Session helpers & apiFetch
├── manage.py
└── README.md
```

---

## 🛠️ API Documentation

### 👥 Customer Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/customers/add/` | Add a new customer record |
| **GET** | `/customers/` | Get list of all customers |
| **PUT** | `/customers/update/<id>/` | Update specific customer |
| **DELETE** | `/customers/delete/<id>/` | Delete customer by ID |

### 🌴 Island Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/islands/add/` | Add a new island |
| **GET** | `/islands/` | Get list of all islands |
| **PUT** | `/islands/update/<id>/` | Update specific island |
| **DELETE** | `/islands/delete/<id>/` | Delete island by ID |

### 🎁 Resort & Package Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/packages/add/` | Add a resort package |
| **GET** | `/packages/` | Get list of all packages |
| **PUT** | `/packages/update/<id>/` | Update specific package |
| **DELETE** | `/packages/delete/<id>/` | Delete package by ID |

### 📖 Booking Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/bookings/add/` | Add a new booking |
| **GET** | `/bookings/` | Get list of all bookings |
| **PUT** | `/bookings/update/<id>/` | Update specific booking status |
| **DELETE** | `/bookings/delete/<id>/` | Delete booking by ID |

### 💳 Payment Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/payments/add/` | Create a new payment transaction |
| **GET** | `/payments/` | Get list of all payments |
| **PUT** | `/payments/update/<id>/` | Update specific payment |
| **DELETE** | `/payments/delete/<id>/` | Delete payment by ID |
