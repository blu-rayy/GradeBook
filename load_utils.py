import sqlite3
from PyQt5.QtGui import QFontDatabase
import os


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

def load_stylesheet(css_file):
    """
    Load CSS from an external file and return it as a string.
    
    Args:
        css_file: Path to CSS file
    
    Returns:
        str: CSS content or empty string if file not found
        
    Example:
        widget.setStyleSheet(load_stylesheet("assets/styles/main.css"))
    """
    try:
        # Ensure the path uses proper separators for the OS
        css_path = os.path.normpath(css_file)
        
        if not os.path.exists(css_path):
            print(f"Warning: CSS file not found: {css_path}")
            return ""
            
        with open(css_path, 'r') as f:
            return f.read()
            
    except Exception as e:
        print(f"Error loading stylesheet {css_file}: {e}")
        return ""

def apply_stylesheet(widget, css_file):
    """
    Apply CSS from file directly to a widget.
    
    Args:
        widget: PyQt widget to apply stylesheet to
        css_file: Path to CSS file
        
    Example:
        apply_stylesheet(my_widget, "assets/styles/scroll_area.css")
    """
    css_content = load_stylesheet(css_file)
    if css_content:
        widget.setStyleSheet(css_content)