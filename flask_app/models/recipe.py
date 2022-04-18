from dataclasses import dataclass
from flask import flash
import re
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Recipe:
  db = 'recipes'
  def __init__ (self, db_data):
    self.id = db_data['id']
    self.name = db_data['name']
    self.description = db_data['description']
    self.instructions = db_data['instructions']
    self.date_made = db_data['date_made']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    self.under_30 = db_data['under_30']
    self.user_id = db_data['user_id']
  
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM recipe;"
    results = connectToMySQL(cls.db).query_db(query)
    recipes = []
    for r in results:
      recipes.append(cls(r))
    return recipes
  
  @classmethod
  def save(cls,data):
    query = "INSERT INTO recipe (name, description, instructions, date_made, under_30, user_id), Values(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM recipe WHERE recipe.id = %(id)s;"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def get_one(cls,data):
    query = "SELECT * FROM recipe WHERE id = %(id)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    if len(results) < 1:
      return False
    return cls(results[0])
