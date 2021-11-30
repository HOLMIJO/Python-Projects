<<<<<<< HEAD
from os import name
import sqlite3
from sqlite3.dbapi2 import Connection

def SQLite_connection():
    conn = None;
    try:
        conn = sqlite3.connect('Roster.db')
        print("Database connection established successfully!")
        conn = sqlite3.connect(':memory:')
        print("Established database connection to a database\
        that resides in the memory!")
        cursor_object = Connection.cursor()

        """CREATE TABLE IF NOT EXISTS roster(
                id integer PRIMARY KEY,
                name text NOT NULL,
                species text NOT NULL,
                iq integer NOT NULL
        ); """

        sql = ''' INSERT INTO roster(name,species,iq)
                    VALUES(?,?,?) '''

        #execute insert statement for supplied person data
        with sqlite3.connect('Roster.db') as connection:
            c = connection.cursor()
            line = "INSERT INTO roster VALUES ('"+ name +"', '"+ Species +"', " +str(IQ) +")"
            c.execute(roster)

        rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak''not', 'Mangalore', -5))

        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        SQLite_connection()

        c.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
        while True:
            row = c.fetchone()
            if row is None:
                    break
            print (row)

        new_func(conn)

def new_func(conn):
            finally:
                if conn:
                    conn.close()

if __name__ == '__main__':
    create_connection()
=======
from os import name
import sqlite3
from sqlite3.dbapi2 import Connection

def SQLite_connection():
    conn = None;
    try:
        conn = sqlite3.connect('Roster.db')
        print("Database connection established successfully!")
        conn = sqlite3.connect(':memory:')
        print("Established database connection to a database\
        that resides in the memory!")
        cursor_object = Connection.cursor()

        """CREATE TABLE IF NOT EXISTS roster(
                id integer PRIMARY KEY,
                name text NOT NULL,
                species text NOT NULL,
                iq integer NOT NULL
        ); """

        sql = ''' INSERT INTO roster(name,species,iq)
                    VALUES(?,?,?) '''

        #execute insert statement for supplied person data
        with sqlite3.connect('Roster.db') as connection:
            c = connection.cursor()
            line = "INSERT INTO roster VALUES ('"+ name +"', '"+ Species +"', " +str(IQ) +")"
            c.execute(roster)

        rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak''not', 'Mangalore', -5))

        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        SQLite_connection()

        c.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
        while True:
            row = c.fetchone()
            if row is None:
                    break
            print (row)

            new_func(conn)

def new_func(conn):
            finally:
                if conn:
                    conn.close()

if __name__ == '__main__':
    create_connection()
>>>>>>> aed72f5c282db2dc5b27b44a61b5f5f9c2fd569c
