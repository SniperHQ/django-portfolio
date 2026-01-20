# Mcondisi Ntshangase | Django Portfolio Website

A modern, responsive personal portfolio website built with **Django**.
This project showcases my skills, projects, professional journey, and provides a downloadable CV, all managed through a custom Django Admin dashboard.

---

## 🚀 Live Preview

> Deployed on **Render** (Free Tier)

---

## ✨ Key Features

* Professional **About Me** section with profile image
* **Downloadable CV (PDF)** hosted on Cloudinary
* Interactive **Skills** section with animated progress indicators
* **Timeline / Journey** section for education and experience
* **Projects** showcase with tech stack & features
* Fully functional **Admin Dashboard**
* **Cloudinary** integration for images & documents
* Responsive design (Mobile, Tablet, Desktop)
* Clean, modern UI with animations

---

## 🧠 Tech Stack

**Backend**

* Python 3.12
* Django 6.0.1

**Frontend**

* HTML5
* CSS3
* JavaScript (Vanilla)

**Storage**

* Cloudinary (Images & CVs)

**Database**

* SQLite (Local)
* Render persistent database (Production)

**Deployment**

* Render
* Whitenoise (Static files)

---

## 📂 Project Structure

```
django-portfolio/
├── core/                # Hero, About, Skills, Timeline, CV
├── projects/            # Projects app
├── contact/             # Contact form app
├── templates/           # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/               # Local media (optional)
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SniperHQ/django-portfolio.git
cd django-portfolio
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables (.env)

Create a `.env` file and add:

```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create admin user

```bash
python manage.py createsuperuser
```

### 7️⃣ Start server

```bash


```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

---

## ☁️ Deployment Notes (Render Free Tier)

* Static files handled by **Whitenoise**
* Media files handled by **Cloudinary**
* Database persists across redeploys
* No shell access required

---

## ⚠️ Important Notes

* Cloudinary requires **active internet access**
* If Cloudinary is blocked locally, uploads will fail
* CV and images are **not deleted** during redeploys
* Admin content persists permanently

---

## 📧 Contact

**Name:** Mqondisi Hendry Ntshangase
**Email:** [hendry91234@gmail.com](mailto:hendry91234@gmail.com)
**Phone:** +27 63 682 5103
**GitHub:** [https://github.com/yourusername](https://github.com/SniperHQ)
**LinkedIn:** [https://linkedin.com/in/yourprofile](https://linkedin.com/in/https://linkedin.com/in/mcondisi-hendry-ntshangase-a34054262)

---

⭐ If you like this project, feel free to star the repository!
