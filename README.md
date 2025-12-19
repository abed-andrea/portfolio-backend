# Portfolio Backend

Backend for my portfolio project.

## Initial Set Up
- Created a basic FastAPI backend
- Set up a virtual environment
- Installed dependencies and froze them in `requirements.txt`
- Implemented a simple `/hello` GET endpoint
- Ran the backend locally using Uvicorn
- Tested the endpoint successfully using Postman

## How to Setup & Run Locally 
```bash
git clone <repo-url>
cd portfolio-backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
