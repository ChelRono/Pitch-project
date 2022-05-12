from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import  User

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    message = 'Hello World'
    return render_template('index.html',message = message)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


# @main.route('/pitches')
# def pitches():
# 	return render_template('pitch.html')

@main.route('/pitches', methods = ['GET','POST'])
# @login_required
def pitches():
	return render_template('pitch.html')