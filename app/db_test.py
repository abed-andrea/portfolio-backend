from sqlalchemy import text 
from app.db import SessionLocal

def main():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1")).scalar()
        print("DB test result:", result)
    finally:
        db.close()

if __name__ == "__main__":
    main()