from faker import Faker
from sqlalchemy.orm import Session
from storage.database import engine
from storage.models import Product, StockStatus
import random


from storage.database import engine, Base

Base.metadata.create_all(bind=engine)


# Initialize Faker
fake = Faker()

# Create a database session
def get_db():
    with Session(engine) as session:
        return session

def generate_fake_products(n=10):
    db = get_db()
    try:
        for _ in range(n):
            product = Product(
                name=fake.company(),
                description=fake.sentence(),
                category=random.choice(["Electronics", "Home & Kitchen", "Fashion", "Books", "Sports"]),
                price=round(random.uniform(5.00, 500.00), 2),
                stock_status=random.choice(list(StockStatus)).value,  # Ensure value is a string
                sku=fake.unique.bothify(text="??#####")  # Example SKU: AB12345
            )
            db.add(product)

        db.commit()
        print(f"Successfully added {n} fake products!")
    except Exception as e:
        db.rollback()
        print(f"Error inserting fake data: {e}")
    finally:
        db.close()

# Run the function
if __name__ == "__main__":
    generate_fake_products(30)  # Generate 10 fake products
