Lost & Found Management System

Overview
A FastAPI-based backend application for managing lost items, found items, claim requests, and item handovers.

Features

User Management
- User Registration
- User Login
- JWT Authentication
- User Profile

Lost Item Management
- Create Lost Item
- View All Lost Items
- View Lost Item by ID
- Update Lost Item
- Delete Lost Item

Found Item Management
- Create Found Item
- View All Found Items
- View Found Item by ID
- Update Found Item
- Delete Found Item

Claim Request System
- Create Claim Request
- View Claims
- Approve Claim
- Reject Claim

Matching System
- Match Lost and Found Items using:
  - Item Name
  - Category
  - Location

Search & Filters
- Filter Lost Items by Category
- Filter Found Items by Status
- Filter Claims by Status

Reports Dashboard
- Total Lost Items
- Total Found Items
- Successful Claims

Bonus Features
- Pagination
- Background Tasks
- Email Notification (Mock)
- Docker Support
- Pytest Testing
- API Versioning (/api/v1)

Tech Stack

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication

Installation

Clone Repository

bash
git clone <repository-url>
cd lost_found_system


Create Virtual Environment

bash
python -m venv venv


Activate Virtual Environment

Windows:

bash
venv\Scripts\activate


Install Dependencies

bash
pip install -r requirements.txt

Run Application

bash
uvicorn app.main:app --reload

Swagger Documentation

text
http://127.0.0.1:8000/docs


API Base URL

text
/api/v1


Main Endpoints

Authentication
- POST /api/v1/auth/register
- POST /api/v1/auth/login

Users
- GET /api/v1/users/profile

Lost Items
- POST /api/v1/lost-items
- GET /api/v1/lost-items
- GET /api/v1/lost-items/{id}
- PUT /api/v1/lost-items/{id}
- DELETE /api/v1/lost-items/{id}

Found Items
- POST /api/v1/found-items
- GET /api/v1/found-items
- GET /api/v1/found-items/{id}
- PUT /api/v1/found-items/{id}
- DELETE /api/v1/found-items/{id}

Claims
- POST /api/v1/claims/{found_item_id}
- GET /api/v1/claims
- PUT /api/v1/claims/{claim_id}/approve
- PUT /api/v1/claims/{claim_id}/reject

Matches
- GET /api/v1/matches

Reports
- GET /api/v1/reports/total-lost-items
- GET /api/v1/reports/total-found-items
- GET /api/v1/reports/successful-claims
