from crypt import methods
from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/new')
def new():
  return render_template("new.html")

@app.route('/new/recipe', methods = ["POST"])
def new_recipe():
  data = {
    'name': request.form['name'],
    'description': request.form['description'],
    'instructions': request.form['instructions'], 
    
  }