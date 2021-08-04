
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from drone_inventory.forms import UserLoginForm
from drone_inventory.models import User, db, check_password_hash


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm() #instantiates a UserLoginForm class with variable 'form' from forms.py
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print([email, password])
        
        user = User(email, password)
        db.session.add(user)
        db.session.commit()
        #flash message for successful signup
        flash(f'You have successfully created a new account {email}','user-created')
        #after successfully adding a new user, redirect, in this case to home
        return redirect(url_for('site.home')) 

    return render_template('signup.html', form=form)

# Creating a new user instance and adding to the User table

@auth.route('/signin', methods = ['GET','POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print([email,password])
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash('You were successfully logged in.', 'auth-success')
            return redirect(url_for('site.home'))
        else:
            flash('Your email/password is incorrect', 'auth-failed')
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))