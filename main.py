'''
Phase 1: Grade Calculator
* Template (DONE)
* Grade Breakdown (DONE)
* Lecture Grade First
* Numeric and Letter Grade (DONE)
* Option for Lecture or Laboratory
* Option for Midterm Breakdown

Phase 2: Persistent Data on SQLite
Phase 3: GUI with Tkinter
'''

import pandas as pd
from template_config import load_template
from calculations import get_student_scores, calculate_final_grade, get_letter_grade

pd.set_option('display.float_format', '{:.2f}'.format)

def main():
    filepath = input("📂 Enter path to grading template CSV: ")

    try:
        df = load_template(filepath)
        print("✅ Template Valid!")

        course_name = input("Enter Course Name: ")
        

        df = get_student_scores(df)
        final_grade = calculate_final_grade(df)
        letter_grade = get_letter_grade(final_grade)

        print("\n📊 " + course_name + " Grade Breakdown: ")
        print(df[['Category', 'Subcategory', 'Subcategory Score (%)', 'Weight (%)', 'Weighted Score']])
        print(f"\n🎯 Final Grade: {final_grade:.2f}% ({letter_grade})")

    except Exception as e:
        print(f"❌ {e}")

if __name__ == "__main__":
    main()