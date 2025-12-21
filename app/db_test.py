# FIRST TEST, handshake to see if connection between sqlalchemy and postgres db existed
    # command to test: docker compose exec fast-api python -m app.db_test
# from sqlalchemy import text 
# from app.db import SessionLocal

# def main():
#     db = SessionLocal()
#     try:
#         result = db.execute(text("SELECT 1")).scalar()
#         print("DB test result:", result)
#     finally:
#         db.close()

# if __name__ == "__main__":
#     main()



# test for initializing database (check is ContactMessage table is created properly)
# docker compose exec fast-api python -m app.db_test
# docker-compose exec db psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}
from app.db import engine, Base, SessionLocal
from app.models import ContactMessage
from sqlalchemy import text

def main():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables Created successfully!")

if __name__ == "__main__":
    main()
