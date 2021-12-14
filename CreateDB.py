import sqlite3
connection = sqlite3.connect("C:/A/test_database.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    """)
