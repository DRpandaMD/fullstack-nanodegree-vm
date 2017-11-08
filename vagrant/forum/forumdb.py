# Michael Zarate started here:

# Changing code to implement a PostgreSQL DB
import psycopg2
import bleach

DBNAME = "forum"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    dbconnection = psycopg2.connect(database=DBNAME)
    dbcursor = dbconnection.cursor()
    dbcursor.execute("select content, time from posts order by time desc")
    fetchedposts = dbcursor.fetchall()
    dbconnection.close()
    return fetchedposts


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    dbconnection = psycopg2.connect(database=DBNAME)
    dbcursor = dbconnection.cursor()
    dbcursor.execute("insert into posts values (%s)", (bleach.clean(content), ))  # fixed bug here?
    dbconnection.commit()
    dbconnection.close()


