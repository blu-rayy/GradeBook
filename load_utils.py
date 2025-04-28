import sqlite3
from PyQt5.QtGui import QFontDatabase


def load_tables(db_name, schema_file):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Open the schema.sql
        with open(schema_file, 'r') as f:
            schema = f.read()

        cursor.executescript(schema)

        conn.commit()

    except sqlite3.Error as e:
        print(f"Error loading tables: {e}")
    
    finally:
        if conn:
            conn.close()

def load_fonts():
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Bold.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-ExtraBold.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Medium.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-Regular.ttf")
    QFontDatabase.addApplicationFont(r"assets\fonts\Narnoor-SemiBold.ttf")