import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO expenses (category, total, description) VALUES (?, ?, ?)",
            ('Zywnosc', 13.25, 'Dino')
            )

cur.execute("INSERT INTO expenses (category, total, description) VALUES (?, ?, ?)",
            ('Paliwo', 133.80, 'Petropol')
            )

cur.execute("INSERT INTO expenses (category, total, description) VALUES (?, ?, ?)",
            ('Ubrania', 245.80, 'C&A')
            )

connection.commit()
connection.close()