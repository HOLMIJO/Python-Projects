import sqlite3

'''# get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)
'''
'''# execute insert statement for supplied person data
with sqlite3.connect("C:/A/test_database.db") as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('" + firstName + \
        "', '" + lastName + "', " + str(age) + ")"
    c.execute(line)
'''
'''# execute insert statement for supplied person data
with sqlite3.connect("C:/A/test_database.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES (?, ?, ?)", personData)
'''
peopleValues = (('Ron', 'Obvious', 42),
                ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect("C:/A/test_database.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
    # c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
    # (45, 'Luigi', 'Vercotti'))


# select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    # for row in c.fetchall():
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
