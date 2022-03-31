import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"./p2pchat.db")
 
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('p2pchat.db')
    
    # cursor object
    cursor_obj = connection_obj.cursor()
    
    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS CHAT")
    
    # Creating table
    table = """ CREATE TABLE CHAT (
            SOURCE CHAR(255) NOT NULL,
            DEST CHAR(25) NOT NULL,
            MESSAGE VARCHAR(255),
            TIME CHAR(25)
        ); """
    
    cursor_obj.execute(table)
    
    print("Table is Ready")
    
    # Close the connection
    connection_obj.close()