from datetime import date, datetime
from typing import Optional
from crud.access import inc_session_access, start_session
import sqlite3
from sqlite3.dbapi2 import Connection

session = {"current_session": None}


def get_db_connection() -> Connection:
    conn = sqlite3.connect("db/database.db")
    conn.row_factory = sqlite3.Row

    if not session["current_session"]:
        session["current_session"] = start_session(conn)

    # Everytime the the get_db_connection is requested
    # the access count for the current session is incremented

    inc_session_access(conn, session["current_session"])

    return conn
