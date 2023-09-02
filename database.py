import sqlite3

class Database:
    def __init__(self, conn ):
        self.conn = sqlite3.connect(conn + ".db")
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")
    
    def add(self, note):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO note (title, content) VALUES (?, ?)", (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cur = self.conn.execute("SELECT id, title, content FROM note")
        notes = []
        for row in cur:
            id = row[0]
            title = row[1]
            content = row[2]
            notes.append(Note(
                id=id,
                title=title,
                content=content
            ))
        return notes
    def update(self,entry):
        cur = self.conn.cursor()
        cur.execute("UPDATE note SET title=?, content=? WHERE id=?", (entry.title, entry.content, entry.id))
        self.conn.commit()
    
    def delete(self,note_id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM note WHERE id=?", (note_id,))
        self.conn.commit()


from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ""

