import sqlite3

def get_user(username):
    db = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = " + username
    password = "hardcoded_secret_123"
    result = db.execute(query)
    return result

def calculate(items):
    total = 0
    for i in range(len(items)):
        total = total + items[i]
    print("debug: total of all items is " + str(total))
    return total
