# 🏆 Build Wars - Live Ranking System

<comment-tag id="1">A real-time, high-performance leaderboard and competition management system built with **Django**. Designed for live events, this application features a tech-focused UI, automatic rank calculation, and dynamic celebration effects for top finishers.</comment-tag id="1" text="To make the project look more professional on GitHub, consider adding status badges here (e.g., license, Python version, project status). This gives users immediate technical context.

Example:
" type="suggestion">

## ✨ Features

* **🚀 Real-Time Updates**: Background API polling ensures the leaderboard is always current without manual refreshing.
* **🥇 Dynamic Podium**: Automatic highlighting for 1st, 2nd, and 3rd place with custom gold, silver, and bronze badges.
* **🎉 Celebration Engine**: Triggers a full-screen confetti explosion and sound fanfare whenever a new participant enters the Top 3.
* **🔦 New Topper Highlight**: Temporarily pulses and glows the card of the new rank holder to catch the audience's attention for 5 seconds.
* **📱 Responsive Design**: Optimized for large screens, tablets, and mobile devices.
* **🛠️ Competition Management**: Simple forms to register participants and update scores on the fly.
* **💾 Persistent State**: Uses Browser **LocalStorage** to track rank changes across page reloads.

## 🛠️ Tech Stack

* **Backend**: Python / Django 5.x
* **Database**: SQLite (default)
* **Frontend**: HTML5, CSS3 (Custom Glassmorphism styling), Bootstrap 5
* **Animations**: [Canvas-Confetti JS](https://github.com/catdad/canvas-confetti)
* **Fonts**: Orbitron & Roboto (Modern Tech Aesthetics)

## 🚀 Getting Started

<comment-tag id="2">### 1. Clone the Repository

```
git clone [https://github.com/your-username/Buld_Wars.git](https://github.com/your-username/Buld_Wars.git)
cd Buld_Wars

```</comment-tag id="2" text="There is a small typo in 'Buld_Wars' (should be Build_Wars) and the markdown link inside the code block is unnecessary. Using a clean bash label for the code block improves readability and syntax highlighting.

Example:
```bash
git clone https://github.com/your-username/Build_Wars.git
cd Build_Wars
```" type="suggestion">

### 2. Set Up Virtual Environment

<comment-tag id="3">```
# Create venv
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Mac/Linux)
source venv/bin/activate

```</comment-tag id="3" text="Adding the 'bash' or 'python' language identifier after the opening triple backticks will enable syntax highlighting on GitHub, making the code much easier to read.

Example:
```bash
# Create venv
...
```" type="suggestion">

### 3. Install Django


```

pip install django

```

### 4. Database Initialization


```

python manage.py makemigrations App
python manage.py migrate

```

### 5. Run the Application


```

python manage.py runserver

```

Visit `http://127.0.0.1:8000` in your browser.

<comment-tag id="4">## 📂 Project Structure


```

Build_Wars/
├── App/
│   ├── static/
│   │   ├── audio/        # Place celebration.mp3 here
│   │   ├── css/          # Bootstrap & custom styles
│   │   └── js/           # confetti.browser.min.js & ranking_update.js
│   ├── templates/
│   │   └── App/
│   │       ├── leaderboard.html
│   │       └── participant_form.html
│   ├── models.py         # Participant data structure
│   ├── views.py          # Ranking logic & API
│   └── forms.py          # Styled participant forms
├── db.sqlite3
└── manage.py

```</comment-tag id="4" text="Using the 'text' or 'plaintext' identifier for the tree structure prevents accidental code highlighting. Additionally, it's helpful to specify where the 'manage.py' file is located relative to the folders to help new users navigate.

Example:
```text
Build_Wars/  <-- Root Directory
...
```" type="suggestion">

## 🎮 Usage

1. **Register**: Click the floating **+** button to add participants.

2. **Score**: Click **Edit** on any participant to enter their score after the build phase.

3. **Display**: Open the main leaderboard on a projector. As scores are saved, the ranks will shift automatically, and the celebration will trigger if a new person takes the lead!

<comment-tag id="5">## 📝 License

This project was developed for the **Build Wars Event (Velur, Kerala)**. Feel free to use and modify it for your own local competitions!</comment-tag id="5" text="Standardizing the license section makes it clearer for others who want to use your code. Even if it's for a specific event, explicitly stating a license (like MIT) encourages open-source collaboration.

Example:
Distributed under the MIT License. See `LICENSE` for more information." type="suggestion">

*Suggestions added*

```
