# UenoCorporation Website & Internal Web Platform (Public Version)

This repository contains the public-safe, non-confidential source code for a web platform developed for a Japan-based trading and logistics company.
It showcases structure, components, and development practices **without containing proprietary business logic, internal data, or sensitive workflow details**.

---

## 📌 Project Overview

This project includes:

* A responsive **company website**
* A **Django backend** with structured templates
* A **React/JavaScript-enhanced frontend**
* Basic internal utility frameworks (non-confidential)
* A modular, scalable architecture for future expansion

All sensitive information has been intentionally removed for public display.

---

## ⚙️ Tech Stack

### Backend

* Python 3
* Django
* Django Templates
* SQLite (development)

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)
* React components

### Other

* Git/GitHub
* Static file system
* Optional Procfile support

---

## 🏗️ Architecture Overview

The system is structured into:

### 1. Backend (Django)

* URL routing
* Template rendering
* Public-safe models
* Static/media management
* Clean app separation

### 2. Frontend

* Responsive HTML templates
* Custom CSS and JS
* Optional interactive sections using React

### 3. Static Assets

* Stylesheets
* Scripts
* Images (public-safe only)

---

## 📁 Repository Structure

```
/uenocorporation
    ├── settings/
    ├── urls.py
    ├── wsgi.py
    ├── asgi.py

/uenowebsite
    ├── views.py
    ├── models.py
    ├── urls.py
    ├── admin.py
    └── static/

/templates
    └── uenowebsite/

/static
    ├── css/
    ├── js/
    ├── images/

/media
    └── placeholder files

manage.py
requirements.txt
Procfile
README.md
```

---

## 🔨 Features (High-Level, Non-Confidential)

### Website

* Responsive, mobile-friendly layout
* Structured company pages
* SEO-ready template system
* Multi-language-friendly framework

### Technical

* Template inheritance
* Modular Django apps
* Organized static file handling

### Internal Utility Foundation


* Basic structure for dashboards
* Placeholder API routes
* Extendable workflow components

---

## 🚀 Getting Started

```
git clone https://github.com/EPT001/uenocorporation.git
cd uenocorporation
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit:
`http://127.0.0.1:8000/`

---

## 🧪 Development Notes

* Clean Django MVC-style structure
* Modular and easily extendable
* Mix of static templates + interactive scripts
* React used selectively for UI components

---

## 🌐 Future Enhancements

* PostgreSQL migration
* Full React SPA option
* Docker support
* API expansion
* Automated testing




