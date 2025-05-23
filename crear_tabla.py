import sqlite3

def crear_tabla_citas():
    with sqlite3.connect("chatbot.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            fecha_hora TEXT NOT NULL
        )
        """)
        conn.commit()

if __name__ == "__main__":
    crear_tabla_citas()
    print("Tabla 'citas' creada correctamente.")
