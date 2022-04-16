from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/register', methods =['POST'])
def register():
  if not User.validate(request.form):
    return redirect('/')
  pw_hash = bcrypt.generate_password_hash(request.form['password'])
  print(pw_hash)
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email':request.form['email'],
    'password': pw_hash
  }
  id = User.save(data)
  if not id:
    flash("Email already taken, please register")
    return redirect('/')
  session['user_id'] = id
  return redirect ('/display')

@app.route('/login', methods = ['POST'])
def login():
  data = {'email': request.form['email']}
  user_in_db = User.get_email(data)
  if not user_in_db:
    flash('invalid Email/Password')
    return redirect('/')
  if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    flash("Invalid Email/Password")
    return redirect('/')
  session['user_id'] = user_in_db.id
  return redirect ('/display')

@app.route('/display')
def diplay():
  if 'user_id' not in session:
    return redirect ('/logout')
  data = {
    'id':session['user_id']
  }
  return render_template("display.html")