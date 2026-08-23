# Cost Manager API

A REST API for personal expense tracking. Users can record expenses,
organize them by category, and manage wallets. Each user can only
access their own data.


**Live demo:** https://django-cost-manager.onrender.com

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- JWT authentication (`djangorestframework-simplejwt`)
- Deployed on Render



## API Endpoints

### Authentication
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Obtain access and refresh tokens |
| POST | `/api/token/refresh/` | Refresh an expired access token |

### Expenses
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/expenses/` | List the user's expenses |
| POST | `/api/expenses/` | Create an expense |
| GET | `/api/expenses/{id}/` | Retrieve one expense |
| PUT | `/api/expenses/{id}/` | Update an expense |
| DELETE | `/api/expenses/{id}/` | Delete an expense |
| GET | `/api/total/` | Sum of the user's expenses |

### Categories
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/categories/` | List categories |
| POST | `/api/categories/` | Create a category |

### Wallets
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/wallets/` | List the user's wallets |
| POST | `/api/wallets/` | Create a wallet |

All endpoints except `/api/token/` require an `Authorization: Bearer <token>` header.


## Local Setup

```bash
git clone https://github.com/khoshru/django-cost-manager.git
cd django-cost-manager

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=costdb
DB_USER=costuser
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

Then run:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


## Running with Docker

The only prerequisite is Docker. Python and PostgreSQL do not need to be installed locally.

```bash
git clone https://github.com/khoshru/<repo-name>.git
cd <repo-name>
cp .env.example .env
docker compose up --build
```

In a second terminal, create the database tables and an admin user:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

The app is available at `http://127.0.0.1:8000`.

### Services

| Service | Image | Role |
|---|---|---|
| `web` | Built from `Dockerfile` | Django + DRF application |
| `db` | `postgres:16` | PostgreSQL database with a persistent volume |

### Common commands

```bash
docker compose up -d              # run in the background
docker compose down               # stop containers; data is preserved
docker compose logs -f web        # follow logs for one service
docker compose exec web bash      # open a shell inside the container
```

### Environment variables

Copy `.env.example` to `.env` and fill in the values:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for local development, `False` otherwise |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts |
| `DB_NAME` | Database name |
| `DB_USER` | Database user |
| `DB_PASSWORD` | Database password |
| `DB_HOST` | `db` when running with Docker Compose |
| `DB_PORT` | `5432` |