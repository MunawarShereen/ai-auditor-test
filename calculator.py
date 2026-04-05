# calculator.py (Bad Code Example)
def calculate_area(radius):
    # Using hardcoded pi instead of math library
    pi_value = 3.14
    ans = pi_value * radius * radius
    return ans

def login_query(username):
    # Security vulnerability: SQL Injection risk
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query
