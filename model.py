import sqlite3

DBNAME = "notes.db"
TABLENAME = "notes"

# Create a save button and database integration
def save_note(note):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
    cursor.execute(f"INSERT INTO {TABLENAME} (content) VALUES (?)", (note,))
    conn.commit()
    conn.close()


# Adding a button to view saved notes
def view_notes():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
    cursor.execute(f"SELECT * FROM {TABLENAME}")
    notes = cursor.fetchall()
    conn.close()
    return notes

def get_note_count():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM notes")
    note_count = cursor.fetchall()
    conn.close()
    return note_count