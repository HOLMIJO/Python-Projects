import sqlite3

conn = sqlite3.connect('Roster.db')        
#execute insert statement for supplied person data
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
                
    cur.execute("INSERT INTO tbl_roster(Name, Species, IQ) VALUES (?,?,?)", \
                ('Korben Dallas', 'Meat Popsicle', '100'))

    cur.execute("INSERT INTO tbl_roster(Name, Species, IQ) VALUES (?,?,?)", \
                ('Ak''not', 'Mangalore', '-5'))
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("UPDATE tbl_roster SET Species = 'Human' WHERE IQ = '100'")
    cur.execute("SELECT Name, IQ FROM tbl_roster WHERE Species = 'Human'")
    conn.commit()

conn.close()
