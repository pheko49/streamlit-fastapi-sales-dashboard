# Streamlit & FastAPI Retail Analytics Dashboard

## Live Demo

### Frontend
https://sales-dashboard-frontend-olee.onrender.com

### Backend Swagger Docs
https://sales-dashboard-api-4ci8.onrender.com/docs

---

## Project Overview

This project is an end-to-end retail analytics dashboard built using Streamlit, FastAPI, SQLite, Docker, and Render.

The application provides KPI summaries, retail sales analytics, and interactive visual insights using a frontend/backend architecture.

The project demonstrates:
- data ingestion
- API development
- frontend/backend communication
- Docker containerization
- cloud deployment
- CI/CD workflow using GitHub and Render

---

## Architecture

### Frontend
- Streamlit

### Backend
- FastAPI REST API

### Database
- SQLite

### Deployment
- Docker
- Docker Compose
- Render

### Version Control
- Git
- GitHub

---

## Tech Stack

- Python
- Streamlit
- FastAPI
- SQLite
- Pandas
- Requests
- Docker
- Docker Compose
- Git
- GitHub
- Render

---

## Features

- KPI dashboard
- Interactive visualizations
- FastAPI backend endpoints
- Multi-page Streamlit application
- Dockerized deployment
- Public cloud deployment on Render
- REST API architecture
- CI/CD workflow integration

---

## API Endpoints

Some available API endpoints include:

- `/preview_data`
- `/superstore_data`
- `/sales_by_region`
- `/profit_by_category`
- `/profit_by_segment`
- `/top_state_sales`

---

## Screenshots

### Homepage

(Add screenshot here)

---

### KPI Dashboard

(Add screenshot here)

---

### Charts Dashboard

(Add screenshot here)

---

## Local Development Setup

Clone repository:

```bash
git clone https://github.com/pheko49/streamlit-fastapi-sales-dashboard.git
```

Move into project folder:

```bash
cd streamlit-fastapi-sales-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally with Docker Compose:

```bash
docker compose up --build
```

---

## Deployment

The application is deployed using Render.

The frontend and backend are deployed as separate Docker services.

### Frontend Deployment
https://sales-dashboard-frontend-olee.onrender.com

### Backend Deployment
https://sales-dashboard-api-4ci8.onrender.com/docs

---

## CI/CD Workflow

This project uses a CI/CD workflow with GitHub and Render.

Workflow:

```text
VS Code
↓
Git
↓
GitHub
↓
Render Auto Deployment
↓
Live Application
```

Whenever new code is pushed to GitHub:
- Render automatically detects changes
- rebuilds Docker containers
- redeploys the latest application version

---

## Future Improvements

- Authentication system
- PostgreSQL integration
- Advanced filtering
- Real-time analytics
- Environment variables
- Automated testing
- GitHub Actions CI pipeline

---

## Author

Developed by Pheko M.