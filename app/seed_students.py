import random
import sys
import os

# Add the project root to sys.path so we can import the app modules
sys.path.append("/Users/sourav07/Desktop/backend")

from app.database.database import SessionLocal, engine
from app.models.student import Student

# Sample data pools for generating realistic mock students
first_names = [
    "Aarav", "Vihaan", "Aditya", "Sai", "Arjun", "Kabir", "Rohan", "Krishna", "Ishaan", "Shaurya", 
    "Ananya", "Diya", "Aadhya", "Priya", "Riya", "Saanvi", "Ishitha", "Kavya", "Sneha", "Neha", 
    "Rahul", "Amit", "Sandeep", "Deepak", "Vikram", "Suresh", "Ramesh", "Rajesh", "Pooja", "Aisha",
    "John", "Alice", "Michael", "Emily", "David", "Sarah", "James", "Jessica", "Robert", "Karen"
]

last_names = [
    "Sharma", "Verma", "Gupta", "Kumar", "Singh", "Patel", "Reddy", "Rao", "Nair", "Iyer", 
    "Joshi", "Mehta", "Chawla", "Bose", "Sen", "Das", "Roy", "Mishra", "Pandey", "Yadav",
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Taylor", "Thomas"
]

departments = [
    "Computer Science",
    "Information Technology",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electronics & Communication",
    "Data Science",
    "Artificial Intelligence"
]

def seed_database():
    db = SessionLocal()
    try:
        # Check existing emails to prevent duplicate key constraint violations
        existing_emails = set(row[0] for row in db.query(Student.email).all())
        
        inserted_count = 0
        attempts = 0
        max_attempts = 1000  # Avoid infinite loop
        
        print(f"Starting seed. Currently {len(existing_emails)} students in database.")
        
        while inserted_count < 200 and attempts < max_attempts:
            attempts += 1
            first = random.choice(first_names)
            last = random.choice(last_names)
            name = f"{first} {last}"
            
            # Generate a unique email
            email_base = f"{first.lower()}.{last.lower()}"
            email = f"{email_base}@example.com"
            
            # If email already exists, append a random number
            counter = 1
            while email in existing_emails:
                email = f"{email_base}{counter}@example.com"
                counter += 1
            
            # Random selections
            dept = random.choice(departments)
            year = random.randint(1, 4)
            cgpa = round(random.uniform(5.5, 9.9), 2)
            
            # Generate 10-digit random phone number
            phone = "".join(str(random.randint(0, 9)) for _ in range(10))
            
            # Create Student model instance
            student = Student(
                name=name,
                email=email,
                department=dept,
                year=year,
                cgpa=cgpa,
                phone=phone
            )
            
            db.add(student)
            existing_emails.add(email)
            inserted_count += 1

        db.commit()
        print(f"Successfully inserted {inserted_count} new student records!")
        
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
