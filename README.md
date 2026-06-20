# Task Manager

A full-featured web application for managing personal tasks built with Django. Users can register, log in, create tasks, mark them as complete, and delete them — all within a clean and intuitive interface.

## Features

- **User Authentication** — sign up, log in, and log out with secure password handling
- **Task Management** — create, view, update, and delete tasks
- **Task Prioritization** — mark tasks as important
- **Completion Tracking** — mark tasks as done and review your completed history
- **Personalized Workspace** — each user sees only their own tasks

## Tech Stack

- **Backend:** Django 6.x (Python)
- **Frontend:** HTML5, Bootstrap 5
- **Database:** SQLite (development) — easily swappable to PostgreSQL/MySQL for production

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd django-crud-project

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

### Production Build

```bash
./build.sh
```

The build script installs dependencies, collects static files, and applies migrations.

## Project Structure

```
django-crud-project/
├── djangocrud/          # Project configuration (settings, URLs, WSGI/ASGI)
├── tasks/               # Main app — models, views, forms, templates
│   ├── models.py        # Task model definition
│   ├── views.py         # All view logic (CRUD + auth)
│   ├── forms.py         # Task, Login, and Signup forms
│   └── templates/       # HTML templates
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── build.sh             # Deployment script
```

## API Overview

| Endpoint                      | Method | Description            | Auth Required |
|-------------------------------|--------|------------------------|:-------------:|
| `/`                           | GET    | Home page              | No            |
| `/signup/`                    | GET/POST | User registration   | No            |
| `/login/`                     | GET/POST | User login           | No            |
| `/logout/`                    | GET    | User logout            | Yes           |
| `/tasks/`                     | GET    | List pending tasks     | Yes           |
| `/tasks/create`               | GET/POST | Create a new task   | Yes           |
| `/tasks/<id>/`                | GET/POST | View/edit a task    | Yes           |
| `/tasks/<id>/complete`        | POST   | Mark task as done      | Yes           |
| `/tasks/<id>/delete`          | POST   | Delete a task          | Yes           |
| `/tasks_completed/`           | GET    | View completed tasks   | Yes           |
| `/admin/`                     | GET    | Django admin panel     | Staff         |

## License

[MIT](LICENSE)
