from re import L
from mysqlconnection import connectToMySQL

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email_signup;"
        results = connectToMySQL('mydb').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    @classmethod
    def save(cls, data):
        query = "INSET INTO email_signup (email, created_at) VALUES (%(femail)s, NOW())";
