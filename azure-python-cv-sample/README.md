# Azure + Python (Flask & Django) CV Sample Project

This repository is a compact sample you can include in your CV to demonstrate:
- Python web development with Flask (microservice / API)
- Python web development with Django (full-stack web app)
- Containerization using Docker
- Continuous deployment to Azure Web Apps via GitHub Actions (example workflow)

Project layout
- `flask_app/` : Minimal Flask API that returns JSON and demonstrates a simple computation endpoint.
- `django_app/` : Minimal Django site with one page.
- `.github/workflows/azure-deploy.yml` : Example GitHub Actions workflow to build and deploy Docker image to Azure Web App.

Why this is CV-friendly
- Shows both microservice-style API (Flask) and traditional web app (Django).
- Includes Dockerfiles to demonstrate containerization knowledge.
- Includes example CI/CD workflow to show Azure deployment knowledge.

Requirements (local)
- Python 3.11+ (virtualenv recommended)
- Docker (optional, for building containers)
- Git (for versioning)
- An Azure subscription and an Azure Web App for container deployment (optional for push-to-Azure demos)

How to run locally

Flask app:
```powershell
# from the flask_app folder
python -m venv .venv; .\.venv\Scripts\Activate
pip install -r requirements.txt
python app.py
# API available at http://127.0.0.1:5000/api/hello
```

Django app:
```powershell
# from the django_app folder
python -m venv .venv; .\.venv\Scripts\Activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Site available at http://127.0.0.1:8000/
```

Docker (build & run example)
```powershell
# Flask
docker build -t sample-flask ./flask_app
docker run -p 8000:8000 sample-flask

# Django
docker build -t sample-django ./django_app
docker run -p 8000:8000 sample-django
```

Azure deployment (high-level)
1. Create an Azure Resource Group, App Service Plan and Web App (Linux) capable of running containers.
2. In GitHub repository, add the Azure publish profile or service principal secrets (the example workflow expects `AZURE_WEBAPP_PUBLISH_PROFILE`).
3. Push to `main` (or configured branch) — workflow will build and deploy.

Example Azure CLI commands
```powershell
# login
az login

# create resource group
az group create --name cv-sample-rg --location eastus

# create app service plan
az appservice plan create --name cv-sample-plan --resource-group cv-sample-rg --sku B1 --is-linux

# create webapp for containers
az webapp create --resource-group cv-sample-rg --plan cv-sample-plan --name <YOUR-UNIQUE-NAME> --deployment-container-image-name mcr.microsoft.com/azuredocs/aci-helloworld
```

Notes and next steps you can ask me for
- I can add an Azure ARM/Bicep or Terraform example to provision infra.
- I can create an Azure DevOps pipeline instead of GitHub Actions.
- I can wire a managed database (Azure Database for PostgreSQL) or Cosmos DB demo.
- I can commit this scaffold into a Git repo and help you push it to GitHub and configure the GitHub Actions secrets.

License
- Public sample for CV use.
