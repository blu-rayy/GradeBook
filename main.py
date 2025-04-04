'''
Phase 1: Grade Calculator
Grade Breakdown
template.txt
Lecture Grade First
Persistent data via .txt first
Numeric and Letter Grade 


Phase 2: Persistent Data on SQLite
Phase 3: GUI with Tkinter

Phase 4: Grade Calculator
'''

# main.py

from template_config import load_template
from calculations import get_student_scores, calculate_final_grade

def main():
    filepath = input("📂 Enter path to grading template CSV: ")

    try:
        df = load_template(filepath)
        print("✅ Template Valid!")

        df = get_student_scores(df)
        final_grade = calculate_final_grade(df)

        print("\n📊 Grade Breakdown:")
        print(df[['Category', 'Subcategory', 'Subcategory Score (%)', 'Weight (%)', 'Weighted Score']])
        print(f"\n🎯 Final Grade: {final_grade:.2f}%")

    except Exception as e:
        print(f"❌ {e}")

if __name__ == "__main__":
    main()

