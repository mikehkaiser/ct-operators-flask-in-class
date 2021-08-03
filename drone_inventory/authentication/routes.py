from flask import Blueprint, render_template
from drone_inventory.forms import UserLoginForm


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup')
def signup():
    form = UserLoginForm()
    return render_template('signup.html', form=form)

@auth.route('/signin')
def signin():
    return render_template('signin.html')