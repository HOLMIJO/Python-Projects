<<<<<<< HEAD
import sqlite3
with sqlite3.connect('test.db') as connection:
    c=connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)
=======
import sqlite3
with sqlite3.connect('test.db') as connection:
    c=connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)
>>>>>>> aed72f5c282db2dc5b27b44a61b5f5f9c2fd569c
