# Superstore Sales Dashboard

An interactive business intelligence dashboard built using Streamlit, FastAPI, SQLite, and Docker.

## Features

- Interactive KPI dashboard
- Sales analysis visualizations
- FastAPI backend
- SQLite database integration
- Dockerized application
- Multi-page Streamlit application

## Tech Stack

- Python
- Streamlit
- FastAPI
- SQLite
- Docker
- Pandas

## Project Structure

data analysis project/
├── data/
├── database/
├── notebooks/
├── src/
├── streamlit_app/
├── Dockerfile
├── requirements.txt
└── README.md

## Running Locally

### Start FastAPI

uvicorn src.api:app --reload

### Start Streamlit

streamlit run streamlit_app/Homepage.py

## Docker

Build image:

docker build -t superstore-dashboard .

Run container:

docker run -p 8501:8501 superstore-dashboard

## Future Improvements

- Docker Compose integration
- Render deployment
- Enhanced API architecture

## Author

Pheko Mantlhasi