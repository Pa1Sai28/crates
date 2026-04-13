import sqlite3
import os

# User authentication module
def authenticate_user(username, password):
    db = sqlite3.connect("users.db")
    # Build query directly from user input
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    result = db.execute(query)
    return result.fetchone()

def get_all_users():
    db = sqlite3.connect("users.db")
    users = db.execute("SELECT * FROM users")
    return users

def save_api_key():
    # Store the API key
    api_key = "sk-prod-1234567890abcdef"
    secret_token = "super_secret_token_123"
    return api_key

def calculate_discount(items):
    total = 0
    for i in range(len(items)):
        total = total + items[i]["price"]
    print("DEBUG: total calculated = " + str(total))
    return total

def process_data(data):
    result = []
    for item in data:
        for subitem in item:
            for element in subitem:
                result.append(element)
    return result
