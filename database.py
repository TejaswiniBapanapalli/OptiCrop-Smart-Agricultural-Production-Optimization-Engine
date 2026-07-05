import sqlite3

connection = sqlite3.connect('opticrops.db')

with connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nitrogen TEXT,
            phosphorous TEXT,
            potassium TEXT,
            temperature TEXT,
            humidity TEXT,
            ph TEXT,
            rainfall TEXT,
            season TEXT,
            crop TEXT
        );
    """)
