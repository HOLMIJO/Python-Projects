import sqlite3
connection = sqlite3.connect("C:\\Users\\joeho\\Dropbox\\School\\Python-Projects\\test.db")
with sqlite3.connect('test.db') as connection:
    c.connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)
