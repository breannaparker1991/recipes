
from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/new')
def new():
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id': session['user_id']
  }
  return render_template("new.html", user = User.get_one(data))
  
@app.route('/create/recipe', methods= ['POST'])
def create():
  if 'user_id' not in session:
    return redirect ('/logout')
  if not Recipe.validate(request.form):
    print('oops, theres a problem')
    return redirect('/new')
  print(request.form)
  data = {
    'name': request.form['name'],
    'description': request.form['description'], 
    'instructions': request.form['instructions'], 
    'under_30': request.form['under_30'],
    'date_made':request.form['date_made'],
    'user_id': session['user_id']
  }
  Recipe.save(data)
  return redirect('/display')

@app.route('/destroy/<int:id>')
def destroy(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id' : id
  }
  Recipe.destroy(data)
  return redirect('/display')

@app.route('/view/<int:id>')
def view(id):
  if 'user_id' not in session:
    return redirect('/logut')
  data = {
    'id' : id
  }
  user = {
    'id':session['user_id']
  }
  return render_template('recipes.html', recipe = Recipe.get_one(data), user = User.get_one(user))

@app.route('/edit/<int:id>')
def edit(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id': id
  }
  user = {
    'id': session['user_id']
  }
  return render_template("edit.html", recipe = Recipe.get_one(data), user = User.get_one(user))
  
@app.route('/update', methods= ['POST'])
def update():
  if 'user_id' not in session:
    return redirect ('/logout')
  if not Recipe.validate(request.form):
    return redirect('/new')
  data = {
    'name': request.form['name'],
    'description': request.form['description'], 
    'instructions': request.form['instructions'], 
    'under_30': request.form['under_30'],
    'date_made':request.form['date_made'],
    'id': request.form['id']
  }
  Recipe.update(data)
  return redirect('/display')