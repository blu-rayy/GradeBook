from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QFrame, QScrollArea
from PyQt5.QtCore import Qt
from gui.ui_components import create_section
import sqlite3

class HomeBodyWidget(QWidget):
    def __init__(self, ui_config=None, parent=None):
        super().__init__(parent)
        self.ui_config = ui_config
        self.init_ui()
        
    def init_ui(self):
        # Main layout with no spacing
        layout = QVBoxLayout(self)
        layout.setContentsMargins(70, 0, 70, 0)
        layout.setSpacing(0) 
        self.setStyleSheet("QWidget { margin: 0; padding: 0; }")

        # TITLE_SECTION: 1780x77
        title_section = QWidget()
        title_section.setObjectName("title_section")
        title_section.setFixedSize(1780, 77)
        title_section.setStyleSheet(f"""
            #title_section {{
                background-color: {self.ui_config['colors']['GREEN_TEAL']};
                margin: 0px;
            }}
        """)
        
        title_layout = QHBoxLayout(title_section)
        title_layout.setContentsMargins(80, 0, 80, 0)  # Left and right padding of 80px
        title_layout.setSpacing(0)
        
        title_label = QLabel("Course Name")
        title_label.setStyleSheet(f"""
            font-family: {self.ui_config['fonts']['HEADING_FONT_BOLD']};
            font-size: 24px;
            color: {self.ui_config['colors']['SNOW_WHITE']};
            margin: 0px;
            padding: 0px;
        """)
        title_label.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(title_label)
        
        layout.addWidget(title_section, 0, Qt.AlignTop)

        # BODY_SECTION: 1780x913
        body_section = QWidget()
        body_section.setObjectName("body_section")
        body_section.setFixedSize(1780, 913)
        body_section.setStyleSheet("""
            #body_section {
                margin: 0px;
                padding: 0px;
                margin-top: 0px;
            }
        """)
        
        body_layout = QVBoxLayout(body_section)
        body_layout.setContentsMargins(72, 15, 72, 100) #ADJUSTING PADDING OF BODY_LAYOUT
        body_layout.setSpacing(0)
        body_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        # CONTENT_SECTION: 1635x544 with dynamic height
        content_section = QWidget()
        content_section.setFixedWidth(1635)
        content_section.setObjectName("content_section")
        content_section.setStyleSheet("""
            #content_section {
                background-color: white;
                border-radius: 5px;
                box-shadow: inset 0px 4px 10px rgba(0, 0, 0, 0.1);
            }
        """)
        
        content_layout = QVBoxLayout(content_section)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # TITLE_SUBSECTION: 1635x57
        title_subsection = QWidget()
        title_subsection.setFixedHeight(57)
        title_subsection.setStyleSheet(f"""
            background-color: {self.ui_config['colors']['MID_TEAL']};
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        """)
        
        title_subsection_layout = QHBoxLayout(title_subsection)
        title_subsection_layout.setContentsMargins(0, 0, 0, 0)
        title_subsection_layout.setSpacing(0)
        
        # Column titles with exact dimensions
        column_titles = [
            ("COURSE CODE", 208),
            ("COURSE TITLE", 577),
            ("SECTION", 201),
            ("UNITS", 201),
            ("MIDTERM", 184),
            ("FINAL", 184)
        ]
        
        for title, width in column_titles:
            header_label = QLabel(title)
            header_label.setFixedWidth(width)
            header_label.setStyleSheet(f"""
                font-family: {self.ui_config['fonts']['HEADING_FONT_BOLD']};
                font-size: 16px;
                color: {self.ui_config['colors']['SNOW_WHITE']};
            """)
            header_label.setAlignment(Qt.AlignCenter)
            title_subsection_layout.addWidget(header_label)
        
        content_layout.addWidget(title_subsection)
        
        # ITEMS_SUBSECTION: 1555x533 (dynamic)
        items_subsection = QWidget()
        items_subsection.setObjectName("items_subsection")
        
        items_layout = QVBoxLayout(items_subsection)
        items_layout.setContentsMargins(0, 0, 0, 0)
        items_layout.setSpacing(0)
        
        # fetch database courses
        course_data = self.fetch_course_data()
        
        # creating table rows
        for course in course_data:
            course_item = QWidget()
            course_item.setFixedHeight(70)
            course_item_layout = QHBoxLayout(course_item)
            course_item_layout.setContentsMargins(0, 0, 0, 0)
            course_item_layout.setSpacing(0)
            
            column_widths = [width for _, width in column_titles]
            
            for i, (data, width) in enumerate(zip(course, column_widths)):
                item_label = QLabel(data)
                item_label.setFixedWidth(width)
        
                alignment = Qt.AlignCenter
                item_label.setStyleSheet(f"""
                    font-family: {self.ui_config['fonts']['BODY_FONT']};
                    font-size: 16px;
                    color: {self.ui_config['colors']['DARK_TEAL']};
                 """)
                
                item_label.setAlignment(alignment)
                course_item_layout.addWidget(item_label)
            
            items_layout.addWidget(course_item)
        
        content_layout.addWidget(items_subsection)
        
        # ADD_COURSE_SECTION
        add_course_section = QWidget()
        add_course_section.setFixedHeight(55)
        add_course_section.setStyleSheet("background-color: transparent;")
        
        add_course_layout = QHBoxLayout(add_course_section)
        add_course_layout.setContentsMargins(20, 0, 0, 0)
        add_course_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        add_course_label = QLabel("+ Add New Course")
        add_course_label.setStyleSheet(f"""
            font-family: {self.ui_config['fonts']['HEADING_FONT']};
            font-size: 16px;
            color: {self.ui_config['colors']['GRAY']};
        """)

        # course data via SQL
        add_course_layout.addWidget(add_course_label)
        content_layout.addWidget(add_course_section)
        body_layout.addWidget(content_section)
        layout.addWidget(body_section, 0, Qt.AlignTop)

    def fetch_course_data(self):
        """Fetch course data from database"""
        course_data = []
        try:
            conn = sqlite3.connect('db/gradebook.db')
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT course_code, course_title, section, units, 
                       COALESCE(midterm_grade, '3.50') as midterm, 
                       COALESCE(final_grade, '-') as final
                FROM course
                ORDER BY courseID
            """)
            
            course_data = cursor.fetchall()
            conn.close()
            
            # If no data in database, use sample data
            if not course_data:
                course_data = [
                    ("###00", "Far Eastern University Institute of Technology", "T#00", "0", "-", "-"),
                ]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            course_data = [
                ("CCS43", "Applications Development and Emerging Technologies (LEC)", "TN27", "2", "3.50", "-"),
                ("CCS43L", "Applications Development and Emerging Technologies (LAB)", "TN27", "1", "3.50", "-"),
                ("CCS103", "Technopreneurship (CCS)", "TN27", "3", "4.00", "-"),
                ("CS13", "Networks and Communications 1", "TN27", "3", "3.00", "-"),
                ("CS23", "Automata Theory and Formal Languages", "TN27", "3", "3.00", "-"),
                ("CS48", "CS SPEC 1 - Structured Programming Language (LEC)", "TN27", "2", "3.50", "-"),
                ("CS48L", "CS SPEC 1 - Structured Programming Language (LAB)", "TN27", "1", "3.50", "-"),
                ("CS51", "CS ELECTIVE - Parallel and Distributive COmputing", "TN27", "3", "3.50", "-"),
                ("GED31", "Purposive Communication", "TN27", "3", "4.00", "-"),
                ("CS51", "CS ELECTIVE - Parallel and Distributive COmputing", "TN27", "3", "3.50", "-"),
                ("GED31", "Purposive Communication", "TN27", "3", "4.00", "-")
            ]
        
        return course_data