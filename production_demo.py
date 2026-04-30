import sqlite3

class UserManager:
    def __init__(self):
        self.db = sqlite3.connect("users.db")
        self.admin_password = "admin123"
    
    def get_user(self, username):
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        return self.db.execute(query).fetchone()

def process_payment(amount, card_number):
    api_key = "sk-live-payment-key-123456"
    print("Card: " + card_number)
    return True
