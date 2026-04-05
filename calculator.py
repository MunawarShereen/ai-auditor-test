```python
import math
from sqlalchemy import text

def calculate_area(radius: float) -> float:
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

def login_query(username: str) -> text:
    """Generate a SQL query to retrieve user data."""
    if not username:
        raise ValueError("Username cannot be empty")
    query = text("SELECT * FROM users WHERE name = :username")
    return query

# Example usage:
try:
    area = calculate_area(5.0)
    print(f"Area: {area}")
except ValueError as e:
    print(f"Error: {e}")

# To execute the login query, use the ORM library's execute method
# For example, using SQLAlchemy:
# from sqlalchemy import create_engine
# engine = create_engine("postgresql://user:password@host:port/dbname")
# with engine.connect() as conn:
#     result = conn.execute(login_query("username"), {"username": "john_doe"})
#     print(result.fetchall())
```