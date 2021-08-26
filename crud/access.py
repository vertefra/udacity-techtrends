from sqlite3.dbapi2 import Connection
from datetime import datetime

def start_session(conn: Connection) -> datetime:
    '''
    Start a session counting all the db access during this session
    '''
    timestap = datetime.now()

    curs = conn.cursor()
    
    curs.execute(
        f"""
        INSERT INTO access (session_started, access)
        VALUES ('{timestap}', 0)
        """
    )
    curs.close()
    conn.commit()

    return timestap

def inc_session_access(conn: Connection, session: datetime):
    """ does not commit the session"""
    curs = conn.cursor()

    current_count: int = curs.execute(
        f"""
        SELECT access
        FROM access
        WHERE session_started = '{session}';
        """
    ).fetchone()

    if current_count:
        current_count = (tuple(current_count)[0])
        current_count += 1

    curs.execute(
        f"""
        UPDATE access
        SET access={current_count}
        WHERE session_started='{session}'
        """
    )

    curs.close()
    conn.commit()

def get_all_access(conn: Connection, session: datetime):
    access_count = conn.execute(
        f"""
        SELECT * FROM access WHERE session_started='{session}'
        """
    ).fetchone()

    return {
        'session': session,
        'db_access': dict(access_count)['access']
    }

    
    
