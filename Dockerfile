# Start with a computer that already has Python 3.12 installed
FROM python:3.12-slim

# Think of /src as the project folder inside the container 
WORKDIR /src

# Copy requirements.txt from my laptop into the container’s /src folder
COPY requirements.txt .

# While building the container, install the Python libraries
RUN pip install -r requirements.txt


# Copy my app/ folder into the container (So now inside the container you have: /src/app/main.py)
COPY app ./app

# When someone runs this container, start the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]