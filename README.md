# Learning Log

A Django-based web application for tracking learning topics and entries. Users can create topics, add detailed learning entries, and track their progress.

## Features

- **User Authentication**: Register, login, logout with Django's built-in auth system
- **Topic Management**: Create and view learning topics
- **Entry Tracking**: Add detailed entries to topics to document learning
- **Responsive Design**: Bootstrap-based UI for mobile and desktop
- **Admin Panel**: Django admin interface for data management

## Tech Stack

- **Backend**: Django 5.2.8
- **Frontend**: Bootstrap 4, HTML/CSS
- **Database**: SQLite (development), PostgreSQL (production)
- **Server**: Gunicorn + WhiteNoise for static files
- **Deployment**: Render (free tier)

## Prerequisites

- Python 3.12+
- pip or uv (package manager)
- Git

## Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/int-arsh/learning_log.git
cd learning_log
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 6. Run development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Project Structure

```
learning_log/
├── learning_log/          # Main project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py            # Root URL routing
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── learning_logs/         # Learning log app
│   ├── models.py          # Topic & Entry models
│   ├── views.py           # App views
│   ├── urls.py            # App URL routing
│   ├── forms.py           # Django forms
│   └── templates/         # App templates
├── users/                 # User authentication app
│   ├── views.py           # Registration & auth views
│   ├── urls.py            # Auth URL routing
│   └── templates/         # Auth templates
├── manage.py              # Django CLI
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment configuration
└── README.md              # This file
```

## Deployment on Render (Free)

### Prerequisites
- GitHub account with repo pushed
- Render.com free account

### Steps

#### 1. Prepare repo
```bash
# Ensure all changes are committed
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

#### 2. Create Render Web Service
- Go to [render.com/dashboard](https://render.com/dashboard)
- Click "New +" → "Web Service"
- Select your GitHub repo
- Choose runtime: **Python 3.12**

#### 3. Configure Build & Start Commands

**Build Command**:
```
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start Command**:
```
gunicorn learning_log.wsgi --log-file -
```

#### 4. Set Environment Variables
Add these in Render's Environment tab:

| Key | Value |
|-----|-------|
| `DEBUG` | `false` |
| `SECRET_KEY` | [Generate strong key](https://djecrety.ir/) |
| `ALLOWED_HOSTS` | `.onrender.com` |

#### 5. Deploy
Click "Deploy". Render will:
1. Install dependencies
2. Collect static files
3. Run migrations
4. Start the app

Your app will be live at `https://<your-service-name>.onrender.com`

### Database Persistence (Optional)
SQLite on Render's free tier is ephemeral (data lost on redeploy). For production:
- Add a Render PostgreSQL database
- Copy its `DATABASE_URL` to environment variables
- Render auto-configures the connection

## Usage

### Register
1. Visit `/users/register/`
2. Create account with username & password

### Create a Topic
1. Login
2. Click "New Topic"
3. Enter topic name and save

### Add an Entry
1. Click a topic
2. Click "New Entry"
3. Write your learning notes and save

### Admin Panel
1. Visit `/admin/`
2. Login with superuser credentials
3. Manage users, topics, and entries

## Troubleshooting

### Migrations Failed
```bash
python manage.py showmigrations
python manage.py migrate learning_logs
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

### Render Deployment Issues
- Check build logs in Render dashboard
- Verify `SECRET_KEY` is set in environment
- Ensure `gunicorn` is in `requirements.txt`

## License

MIT License - feel free to use and modify.

## Contributing

Contributions welcome! Fork, create a feature branch, and submit a pull request.

## Author

int-arsh | [GitHub](https://github.com/int-arsh)