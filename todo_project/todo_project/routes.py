from flask import render_template, url_for, flash, redirect, request
from todo_project import db, bcrypt
from todo_project.models import User, Task
from todo_project.forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=['POST', 'GET'])
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('all_tasks'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login Successful', 'success')
            return redirect(url_for('all_tasks'))
        else:
            flash('Login Unsuccessful. Please check Username or Password', 'danger')
    
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('user_login'))

# Adicione suas outras rotas aqui