
from flask.wrappers import Response
from crud.access import get_all_access
from crud.post import create_post, get_post, get_posts
from flask import Flask, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
from db.db import session

from db import db

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

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
      return render_template('404.html'), 404
    else:
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
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
   app.run(host='0.0.0.0', port='3111', debug=True)
