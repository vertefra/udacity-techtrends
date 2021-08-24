
import os
from crud.access import get_all_access
from crud.post import create_post, get_post, get_posts
from flask import Flask, json, render_template, request, url_for, redirect, flash
from db.db import session
from db import db

from log.logger import logging

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Setting up the logger

app.logger = logging

app_logger = app.logger.getLogger("app")

info = app_logger.info
debug = app_logger.debug
error = app_logger.error

# Define the main route of the web application 

@app.route('/')
def index():
    conn = db.get_db_connection()
    posts = get_posts(conn)
    conn.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    conn = db.get_db_connection()
    post = get_post(conn, post_id)
    conn.close()
    if post is None:
        error(f"Article id <{post_id}> does not exists")
        return render_template('404.html'), 404
    else:
        info(f"Article title <{post['title']}> retrieved")
        return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    info(f"About us retrieved")
    return render_template('about.html')

#  Health Status endpoint
@app.route('/healthz')
def healthz():
    response = app.response_class(
        response=json.dumps({
            "result": "OK - healthy",
        }),
        status_code=200,
        mimeType='application/json'
    )
    return response

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = db.get_db_connection()
            create_post(conn, title, content)
            conn.close()
            info(f"Article title<{title}> created")
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/metrics')
def metrics():
    conn = db.get_db_connection()
    access = get_all_access(conn, session['current_session'])
    posts = get_posts(conn)
    conn.close()
    response = app.response_class(
        response = json.dumps({
            "db_connection_count": access['db_access'],
            'post_count': len(posts)
        })
    )
 
    return response

# start the application on port 3111
if __name__ == "__main__":
    DEBUG = os.getenv("DEBUG")

    if DEBUG is None:
        DEBUG = False
    else:
        DEBUG = bool(DEBUG)
    app.run(host='0.0.0.0', port='3111', debug=DEBUG)
