# Internship Logging & Evaluation System (ILES)

ILES is a full-stack web application for managing internship placements, weekly student logs, supervisor review cycles, evaluations and notifications.

## Live Application

- **Frontend:** https://iles-frontend.onrender.com
- **Backend API:** https://iles-project.onrender.com


## Repository

https://github.com/pleasurenayebare-tech/ILES-PROJECT

## Tech Stack

- **Backend:** Django + Django REST Framework + JWT auth
- **Frontend:** React (Vite) + React Router + Axios
- **Database:** PostgreSQL (hosted on Render)
- **Deployment:** Render

## Project Structure

- `backend/` — Django REST API
- `web/` — React frontend

## Getting Started

Visit https://iles-frontend.onrender.com and register an account to get started.

## User Roles

- **Admin** — Full system access and user management
- **Student** — Submit and manage weekly internship logs
- **Workplace Supervisor** — Review and approve student logs
- **Academic Supervisor** — Oversee evaluations and review cycles

## API Endpoints

- **Auth:** `POST /api/auth/register/`, `POST /api/auth/login/`, `GET /api/auth/me/`
- **Placement:** `GET/POST /api/placements/`
- **Weekly Logs:** `GET/POST /api/weekly-logs/`, `PATCH /api/weekly-logs/{id}/transition/`
- **Evaluation:** `GET/POST /api/evaluations/`
- **Notifications:** `GET /api/notifications/`, `PATCH /api/notifications/{id}/mark_read/`