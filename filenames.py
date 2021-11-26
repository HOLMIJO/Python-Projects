import sqlite3
#Opens connection and creates database
conn = sqlite3.connect('filenames.db')


with conn: #Upon connection, set cursor and create table and column
    c = conn.cursor() #sets cursor for connection
    c.execute("CREATE TABLE IF NOT EXISTS tbl_filenames( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename \
        )")
    conn.commit()
conn.close() #Closes connection

conn = sqlite3.connect('filenames.db') #Opens connection to database
# A tuple of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    c = conn.cursor() #sets cursor for connection
    # loop through each object in the tuple to find the file names that end in .txt.
for x in fileList:
    if x.endswith('.txt'):
	# The value for each row will be one name out of the tuple therefore (x,)
	# will denote a one element tuple for each file name ending with .txt.
	     c.execute("INSERT INTO tbl_filenames (col_filename) VALUES (?)", (x,))
	     print(x)

conn.close() #Closes connection to database
    
