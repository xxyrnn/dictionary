import sqlite3

conn = sqlite3.connect("dictionary.db")
cursor = conn.cursor()
# cursor.execute("""--sql
# CREATE TABLE IF NOT EXISTS words (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     word VARCHAR(255) NOT NULL,
#     def TEXT NOT NULL
# )
# """)

words = [
    ("test", "A procedure intended to establish the quality, performance, or reliability of something, especially before it is taken into widespread use."),
    ("example", "A representative form or pattern."),
    ("sample", "A small part or quantity intended to show what the whole is like."),
    ("demo", "A demonstration of the capabilities of a product or service."),
    ("prototype", "An early sample or model built to test a concept or process."),
    ("trial", "A test of the performance, qualities, or suitability of something."),
    ("assessment", "The evaluation or estimation of the nature, quality, or ability of someone or something."),
    ("evaluation", "The making of a judgment about the amount, number, or value of something."),
    ("analysis", "A detailed examination of the elements or structure of something."),
    ("review", "A formal assessment or examination of something with the possibility or intention of instituting change if necessary."),
]

for word in words:
    cursor.execute(f"INSERT INTO words (word, def) VALUES (?, ?);", word)
    conn.commit()
conn.close()
