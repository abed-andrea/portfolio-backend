# test for initializing database (check is ContactMessage table is created properly)
# run: docker compose exec fast-api python -m app.db_test
from app.db import engine, Base, SessionLocal
from app.models import ContactMessage
from sqlalchemy import text

def main():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables Created successfully!")

if __name__ == "__main__":
    main()
