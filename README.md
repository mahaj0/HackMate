# HackMate; AI-Powered Hackathon Co-Pilot

HackMate is an all-in-one web app designed to supercharge your hackathon workflow. Whether you're brainstorming ideas, organizing sprints, managing team dynamics, or crafting the perfect pitch—HackMate has you covered. With built-in AI features, intuitive UI, and exportable content, it's your ultimate hackathon sidekick.

---

## 🎥 Demo Video

Watch the full walkthrough on YouTube:

[HackMate Playlist](https://www.youtube.com/watch?v=MPH03laePh0)

---

## Features

### Idea Generator
Powered by Gemini AI, generate fresh and refined project ideas with the click of a button. Prompt-based suggestions and easy export.

### Team Dynamics
Quickly add and assign team members with roles. Remove, update, and export team configurations as needed.

### Sprint Planner
Add milestones, set deadlines, mark them complete, and track progress visually with a dynamic progress bar. Export the entire plan.

### Pitch Coach
Step-by-step pitch structuring tool—manually or through AI generation. Export your pitch instantly for submissions or demos.

### Auth System
Signup/Login functionality backed by SQLite for a personalized experience.

---

## Tech Stack

- [Dash](https://plotly.com/dash/) (Frontend + Backend)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [SQLite](https://www.sqlite.org/index.html)
- [Gemini AI (Google Generative AI)](https://ai.google.dev/)
- Python 3.10+

---


## 🛠 Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/hackmate.git
   cd hackmate

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows

4. Install requirements:
   pip install -r requirements.txt

5. Create the SQLite DB:
   python create_db.py

6. Run the app:
   python app.py

**Environment Variables**

    Create a .env file in the root directory:
     GEMINI_API_KEY=your_google_generative_ai_key


** Export Options**

Export team list
Export sprint plan
Export pitch
Export idea suggestions
Inspiration
HackMate was created to reduce the chaos and decision fatigue in fast-paced hackathons. With built-in AI assistance, you focus on building—HackMate handles the rest.

