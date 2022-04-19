from sqlite3 import connect
from flask import flash
import re
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt 

class User:
  db = "recipes"
  def __init__(self, db_data):
    self.id = db_data['id']
    self.first_name = db_data['first_name']
    self.last_name = db_data['last_name']
    self.email = db_data['email']
    self.password = db_data['password']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    self.recipes = []
    
  @classmethod
  def save(cls,data):
    query = "INSERT INTO user (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
    return connectToMySQL(cls.db).query_db(query,data) 

  @classmethod
  def get_one(cls,data):
    query = "SELECT * FROM user WHERE id = %(id)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    if len(results) < 1:
      return False
    return cls(results[0])

  @classmethod
  def get_email(cls,data):
    query = "SELECT * FROM user WHERE email = %(email)s;"
    result = connectToMySQL(cls.db).query_db(query,data)
    if len(result) < 1:
      return False
    return cls(result[0])
  
  @staticmethod
  def validate(user):
    is_valid = True
    query = "SELECT * from user WHERE email = %(email)s"
    results = connectToMySQL(User.db).query_db(query,user)
    if len(user['first_name']) < 2:
      flash ('First Name needs to be at least 2 characters', 'register')
      is_valid = False
    if len(user['last_name']) < 2:
      flash ("Last Name needs to be at least 2 characters", 'register')
      is_valid = False
    if len(results) >= 1:
      flash('Email is already taken!', 'register')
      is_valid = False
    # if EMAIL_REGEX.match(user['email']):
    #   flash('Email is already taken!')
    #   is_valid = False
    if not EMAIL_REGEX.match(user['email']):
      flash('Please enter a valid email address', 'register')
      is_valid = False
    if user['password'] != user['confirm_pass']:
      flash('Passwords must match', 'register')
      is_valid = False
    return is_valid
    