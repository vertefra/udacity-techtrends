from sqlite3.dbapi2 import Connection


def get_post(connection: Connection, post_id: int):
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    return post

def get_posts(connection: Connection) -> list:
    posts = connection.execute('SELECT * FROM posts').fetchall()
    return posts

def create_post(connection: Connection, title: str, content: str):
    connection.execute(f"INSERT INTO posts (title, content) VALUES ('{title}', '{content}')")
    connection.commit()
