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
                conn.commit()
    with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_roster(Name, Species, IQ) VALUES (?,?,?)", \
                            ('Korben Dallas', 'Meat Popsicle', '100'))
                conn.commit()
    with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_roster(Name, Species, IQ) VALUES (?,?,?)", \
                            ('Ak''not', 'Mangalore', '-5'))
                conn.commit()


                cur = conn.cursor()
                cur.execute("UPDATE roster SET Species = 'Human' WHERE IQ = '100'")
                cur.execute("SELECT Name, IQ FROM roster WHERE Species = 'Human'")
                for row in cur.fetchall():
                    print(row)

                cur.execute("SELECT Name, IQ FROM roster WHERE Species = 'Human'")
                while True:
                    row = cur.fetchone()
                    if row is None:
                        break


    #cur = connection.cursor()
    #cur.execute("DROP TABLE IF EXISTS roster")
    #cur.execute("CREATE TABLE roster(Name TEXT, Species TEXT, IQ INT)")
    #cur.executemany("INSERT INTO roster VALUES(?,?,?)", rosterValues)
    #cur.execute("UPDATE roster SET Species = ? WHERE IQ = 100", 'Human')
    #cur.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
    #for row in cur.fetchall():
 
# cur = conn.cursor()
# cur.execute(sql)
# conn.commit()

# SQLite_connection()

# cur.execute("SELECT Name, IQ FROM roster WHERE Species = Human")
# while True:
#     row = cur.fetchone()
#     if row is None:
#             break
#     print (row)
