```markdown
# PRK WEBSITE PROJECT
# Rayaneh Kerman - Company Internal Dashboard

![PRK Dashboard Screenshot](https://github.com/danyallya/rayaneh-kerman-company-dashboard/blob/master/static/images/user.png?raw=true )

> 🏢 Internal HR & Task Management System for Rayaneh Computer Co., Kerman, Iran  
> Built with HTML, CSS, jQuery, Python & Django

![Rayaneh Logo](https://github.com/danyallya/rayaneh-kerman-company-dashboard/blob/master/static/images/prk-logo.png?raw=true )


An internal dashboard and HR management system for **Rayaneh Computer Company in Kerman**, Iran. Built with **HTML5**, **CSS3**, **jQuery**, and powered by **Python Django**, this platform supports company introduction, candidate testing, task management, and time tracking (effort logging).

## 💼 Overview
This project serves as an internal web-based platform for **Rayaneh Computer Company**, offering tools to:
- Introduce the company and its services
- Evaluate job candidates through online tests
- Assign and manage tasks among employees
- Track time spent on each task (Effort Logging)
- Monitor overall team performance

The design is clean, modern, and optimized for all screen sizes.

## 🔑 Features
- Company overview page
- Candidate test assignment & result tracking
- Task management system (assign, update, complete)
- Employee effort/time logging per task
- Admin dashboard for managing users and tasks
- Fully responsive layout for desktop and mobile

## 💻 Technologies Used
### Frontend
- **HTML5** – Semantic structure and accessibility
- **CSS3** – Responsive layout, animations, Flexbox/Grid
- **jQuery** – Dynamic UI interactions (form validation, modal popups)

### Backend
- **Python**
- **Django** – Web framework
- **SQLite / PostgreSQL** – Database (configurable)
- **REST views** – For dynamic data loading

## 📁 Project Structure
rayaneh-kerman-company-dashboard/
├── templates/
│ ├── index.html # Company overview
│ ├── candidates.html # Candidate management/test view
│ ├── tasks.html # Task list for employees
│ ├── effort-logging.html # Time tracking form
│ └── base.html # Base template
├── static/
│ ├── css/
│ │ └── style.css # Stylesheet
│ ├── js/
│ │ └── main.js # jQuery scripts
│ └── assets/
│ ├── images/
│ └── icons/
├── rayaneh/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── core/
│ ├── models.py # Company info, Tasks, Candidates
│ ├── views.py # View logic
│ ├── urls.py # App routes
│ └── admin.py # Admin panel setup
└── manage.py
```