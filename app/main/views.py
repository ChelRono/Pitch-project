from flask import render_template
from . import main
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    message = 'Hello World'
    return render_template('index.html',message = message)


@main.route('/profile')
def profile():

	return render_template('profile.html')


# @main.route('/pitches')
# def pitches():
# 	return render_template('pitch.html')

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def pitches():
	return render_template('pitch.html')