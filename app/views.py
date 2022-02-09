"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, jsonify
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    profile = {
        "name": "Jon-Daniel Coombs",
        "username": "CoderJon-014",
        "location": "Kingston, Jamaica",
        "join_date": format_date_joined(join),
        "about_me": "I am an UI/UX Designer and Web developer who loves to tinker around to create beautiful and innovative designs for applications. You have an idea? I'll design it for you. Feel free to contact me if you have any questions or comments.",
        "posts" : "12",
        "following" : "334",
        "followers" : "201",
    }

    if request.method == "POST":
        return (jsonify(profile))

    return render_template('profile.html', profile=profile)

join = datetime.date(2022, 10, 10)
def format_date_joined(date):
    return "Joined " + join.strftime('%B, %Y')

print(format_date_joined(join))
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
