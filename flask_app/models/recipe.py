from flask import flash
import re
from flask_app.config.mysqlconnection import MySQLConnection

class Recipe:
  db = 'recipes'
  def __init__ (self, db_data):
    self.id = db_data['id']
    self.name = db_data['name']
    self.description = db_data['description']
    self.instructions = db_data['instructions']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    self.under_30 = db_data['under_30']
    self.user_id = db_data['user_id']
  
  
