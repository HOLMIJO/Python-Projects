import sqlite3

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak''not', 'Mangalore', -5))
        
#execute insert statement for supplied person data
with sqlite3.connect('Roster.db') as conn:
    with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS tbl_roster( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    Name TEXT, \
                    Species TEXT, \
                    IQ INT)")
                conn.commit()

    with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_roster(Name, Species, IQ) VALUES (?,?,?)", \
                            ('Jean-Baptiste Zorg', 'Human', '122'))
    with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_roster(Name, Species, IQ) VALUES (?,?,?)", \
                            ('Korben Dallas', 'Meat Popsicle', '100'))
    with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_roster(Name, Species, IQ) VALUES (?,?,?)", \
                            ('Ak''not', 'Mangalore', '-5'))
                cur = conn.cursor()
                cur.execute("UPDATE roster SET Species = Human WHERE IQ = 100")
                cur.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
                for row in cur.fetchall():
                    print(row)

                cur.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
                while True:
                    row = cur.fetchone()
                    if row is None:
                        break



    """c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS roster")
    c.execute("CREATE TABLE roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO roster VALUES(?,?,?)", rosterValues)
    c.execute("UPDATE roster SET Species = ? WHERE IQ = 100", 'Human')
    c.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
    for row in c.fetchall():
 
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
"""