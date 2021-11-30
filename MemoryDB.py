import sqlite3

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak''not', 'Mangalore', -5))
        
#execute insert statement for supplied person data
with sqlite3.connect('Roster.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS roster")
    c.execute("CREATE TABLE roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO roster VALUES(?,?,?)", rosterValues)
    c.execute("UPDATE roster SET Species = ? WHERE IQ = 100", 'Human')
    c.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
    for row in c.fetchall():
        print(row)

    c.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
    while True:
        row = c.fetchone()
        if row is None:
            break
# cur = conn.cursor()
# cur.execute(sql)
# conn.commit()

# SQLite_connection()

# c.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
# while True:
#     row = c.fetchone()
#     if row is None:
#             break
#     print (row)

    