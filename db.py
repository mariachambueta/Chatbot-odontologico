# db.py
import sqlite3

DB_PATH = "chatbot.db"

def conectar_db():
    return sqlite3.connect(DB_PATH)

def crear_tabla_citas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        fecha_hora TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def guardar_cita(chat_id, fecha_hora):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO citas (chat_id, fecha_hora) VALUES (?, ?)", (chat_id, fecha_hora))
    conn.commit()
    conn.close()

def obtener_citas(chat_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, fecha_hora FROM citas WHERE chat_id = ?", (chat_id,))
    citas = cursor.fetchall()
    conn.close()
    return citas

def eliminar_cita(cita_id, chat_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM citas WHERE id = ? AND chat_id = ?", (cita_id, chat_id))
    conn.commit()
    eliminado = cursor.rowcount > 0  # Verifica si se eliminó efectivamente
    conn.close()
    return eliminado
