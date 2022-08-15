from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    print(session)
    return render_template('index.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    users = User.get_user_by_email(request.form)
    if len(users) != 1:
        flash('Invalid email')
        return redirect('/')
    user = users[0]
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid password')
        return redirect('/')
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/home')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/process/register', methods=['POST'])
def process_register():
    if User.validate_user(request.form) == False:
        return redirect('/register')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'username': request.form['username'],
        'password': bcrypt.generate_password_hash(request.form['password']),
    }
    User.add_user(data)
    return redirect ('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')