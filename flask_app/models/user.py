from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
        def __init__(self, data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.email = data['email']
            self.username = data['username']
            self.password = data['password']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

        @classmethod
        def get_user_by_email(cls, data):
            query = "SELECT * FROM users WHERE users.email = %(email)s;"
            result = connectToMySQL('budget_schema').query_db(query, data)
            user = []
            for item  in result:
                user.append(User(item))
            return user

        @classmethod
        def add_user(cls, data):
            query = "INSERT INTO users (first_name, last_name, email, username, password) VALUE (%(first_name)s, %(last_name)s, %(email)s, %(username)s, %(password)s);"
            result = connectToMySQL('budget_schema').query_db(query, data)
            return result

        @staticmethod
        def validate_user(data):
            is_valid = True
            email_regex = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

            # first name needs to be 3-20 characters long
            if len(data['first_name']) < 3 or len(data['first_name']) > 20:
                is_valid = False
                flash('First name needs to be between 3 - 20 characters') 
            # last name needs to be 3-20 characters long
            if len(data['last_name']) < 3 or len(data['last_name']) > 20:
                is_valid = False
                flash('Last name needs to be between 3 - 20 characters')
            # email needs to be unique
            if len(User.get_user_by_email(data)) != 0:
                is_valid = False
                flash('Email is taken')
            if not email_regex.match(data['email']):
                is_valid = False
                flash('needs valid email')
            # username needs to be unique, 2 characters long
            if len(data['username']) < 3 or len(data['username']) > 20:
                is_valid = False
                flash('Username needs to be between 3 - 20 character')
            # username still need to be unique
            # if len(User.get_user_by_email_or_username(data)) != 0:
            #     is_valid = False
            #     flash('Username is taken')
            # password needs to be 8 characters long with special characters
            if len(data['password']) < 8:
                is_valid = False
                flash('Password need to be at least 8 character')
            # confirm password needs to match with password
            if data['password'] != data['confirm_password']:
                is_valid = False
                flash('Passwords need to match')
            # make password regex
            return is_valid