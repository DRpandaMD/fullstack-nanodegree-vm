# Michael Zarate started here:

# Changing code to implement a PostgreSQL DB
import psycopg2

DBNAME = "forum"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    dbconnection = psycopg2.connect(database=DBNAME)
    dbcursor = dbconnection.cursor()
    dbcursor.execute("select content, time from posts order by time desc")
    return dbcursor.fetchall()
    dbconnection.close()


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    dbconnection = psycopg2.connect(database=DBNAME)
    dbcursor = dbconnection.cursor()
    dbcursor.execute("insert into posts values ('%s')" % content)
    dbconnection.commit()
    dbconnection.close()


