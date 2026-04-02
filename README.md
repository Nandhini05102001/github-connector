# GitHub Cloud Connector

## Overview

This project is a GitHub Cloud Connector built using FastAPI.
It integrates with GitHub APIs to fetch repository data, create issues, and list issues.

---

## Tech Stack

* Python
* FastAPI
* Requests
* GitHub REST API

---

## Authentication

This project uses a GitHub Personal Access Token (PAT).
The token is stored securely using environment variables.

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/Nandhini05102001/github-connector.git
cd github-connector

---

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate  (Windows)

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Create `.env` file

Add your GitHub token:
GITHUB_TOKEN=your_github_token_here

---

##  Run the Project

uvicorn app.main:app --reload

Open in browser:
http://127.0.0.1:8000/docs

---

##  API Endpoints

### Get Repositories

GET /repos/{username}

Example:
/repos/Nandhini05102001

---

###  Create Issue

POST /create-issue

Request Body:
{
"repo_owner": "Nandhini05102001",
"repo_name": "github-connector",
"title": "Test Issue",
"body": "This is a test issue"
}

Response:
{
"id": 123456,
"title": "Test Issue",
"state": "open"
}

---

###  List Issues

GET /list-issues?owner={owner}&repo={repo}

Example:
/list-issues?owner=Nandhini05102001&repo=github-connector

---

##  Sample Response (Issues)

[
{
"id": 4195674115,
"number": 1,
"title": "Test Issue",
"state": "open",
"created_at": "2026-04-02T16:26:07Z"
}
]

---

##  Error Handling

* 401 → Invalid Token
* 404 → Repository not found or no access
* 422 → Invalid request format

---

##  Features

* Fetch repositories from GitHub
* Create issues in a repository
* List repository issues
* Secure token handling using `.env`
* Clean and modular API design
* Filtered API responses

---

##  Author

Nandhini
