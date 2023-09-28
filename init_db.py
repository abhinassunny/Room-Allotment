import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO rooms (title, capacity, location) VALUES (?, ?, ?)",
            ('Seminar Hall', '60', 'Main Building')
            )

cur.execute("INSERT INTO rooms (title, capacity, location) VALUES (?, ?, ?)",
            ('Conference Hall', '100', 'NLHC')
            )

cur.execute("INSERT INTO admin (username, password) VALUES (?, ?)",
            ('visakh', 'visakh123' )
            )
cur.execute("INSERT INTO admin (username, password) VALUES (?, ?)",
            ('abhina', 'abhina123' )
            )
cur.execute("INSERT INTO admin (username, password) VALUES (?, ?)",
            ('aleena', 'aleena123' )
            )
cur.execute("INSERT INTO admin (username, password) VALUES (?, ?)",
            ('sami', 'sami123' )
            )

cur.execute("INSERT INTO user (username, password) VALUES (?, ?)",
            ('visakh', 'visakh1234' )
            )

cur.execute("INSERT INTO user (username, password) VALUES (?, ?)",
            ('abhina', 'abhina1234' )
            )

cur.execute("INSERT INTO user (username, password) VALUES (?, ?)",
            ('aleena', 'aleena1234' )
            )

cur.execute("INSERT INTO user (username, password) VALUES (?, ?)",
            ('sami', 'sami1234' )
            )

connection.commit()
connection.close()