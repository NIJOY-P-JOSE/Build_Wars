# 🏆 Build Wars – Live Ranking System

A real-time, high-performance leaderboard and competition management system built with **Django**. Designed for live events, this application features a tech-focused UI, automatic rank calculation, and dynamic celebration effects for top finishers.

---

## ✨ Features

- 🚀 **Real-Time Updates**  
  Background API polling ensures the leaderboard is always current without manual refreshing.

- 🥇 **Dynamic Podium**  
  Automatic highlighting for 1st, 2nd, and 3rd place with custom gold, silver, and bronze badges.

- 🎉 **Celebration Engine**  
  Triggers a full-screen confetti explosion and sound fanfare whenever a new participant enters the Top 3.

- 🔦 **New Topper Highlight**  
  Temporarily pulses and glows the card of the new rank holder to catch the audience's attention.

- 📱 **Responsive Design**  
  Optimized for large screens, tablets, and mobile devices.

- 🛠️ **Competition Management**  
  Simple forms to register participants and update scores on the fly.

- 💾 **Persistent State**  
  Uses Browser LocalStorage to track rank changes across page reloads.

---

## 🛠️ Tech Stack

- **Backend:** Python / Django 5.x  
- **Database:** SQLite (default)  
- **Frontend:** HTML5, CSS3 (Custom Glassmorphism), Bootstrap 5  
- **Animations:** Canvas-Confetti API  
- **Fonts:** Orbitron & Roboto (Modern Tech Aesthetics)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Buld_Wars.git
cd Buld_Wars
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Mac/Linux)
source venv/bin/activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Database Initialization

```bash
python manage.py makemigrations App
python manage.py migrate
```

### 5. Run the Application

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 📂 Project Structure

```
Build_Wars/
├── App/
│   ├── static/
│   │   ├── audio/        # celebration.mp3
│   │   ├── css/          # Bootstrap & custom styles
│   │   └── js/           # confetti.js & ranking_update.js
│   ├── templates/
│   │   └── App/
│   │       ├── leaderboard.html
│   │       └── participant_form.html
│   ├── models.py         # Participant data structure
│   ├── views.py          # Ranking logic & API
│   └── forms.py          # Styled participant forms
├── db.sqlite3
└── manage.py
```

---

## 🎮 Usage

- **Register:** Click the floating **+** button to add participants.
- **Score:** Click **Edit** on any participant to enter their score after the build phase.
- **Display:** Open the main leaderboard on a projector. As scores are saved, the ranks will shift automatically, and the celebration will trigger if a new person takes the lead!

---

## 📝 License

This project was developed for the **Build Wars Event (Velur, Kerala)**.  
Feel free to use and modify it for your own local competitions!
