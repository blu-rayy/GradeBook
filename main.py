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
from tkinter import messagebox
from gui import open_file_dialog
from template_config import load_template
from calculations import get_student_scores, calculate_final_grade, get_letter_grade

pd.set_option('display.float_format', '{:.4f}'.format)

def main():
    def process_template(filepath):
        try:
            df = load_template(filepath)
            messagebox.showinfo("Success", "✅ Template Valid!")

            df = get_student_scores(df)
            final_grade = calculate_final_grade(df)
            letter_grade = get_letter_grade(final_grade)

            print("\n📊Grade Breakdown:")
            print(df[['Category', 'Subcategory', 'Subcategory Score (%)', 'Weight (%)', 'Weighted Score']])
            print(f"\n🎯 Final Grade: {final_grade:.4f}% ({letter_grade})")

        except Exception as e:
            messagebox.showerror("Error", f"❌ {e}")

    open_file_dialog(process_template)

if __name__ == "__main__":
    main()




