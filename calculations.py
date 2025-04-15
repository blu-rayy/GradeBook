def get_student_scores(df, has_lab=False):
    print("\n📥 Enter your scores per subcategory:")
    scores = []

    # handling lab subjects
    if has_lab:
        lecture_scores = []
        lab_scores = []

        # process Lecture Subjects (70% of final grade)
        lecture_df = df[df['Category'].str.contains('CS|E', regex=True)]
        for _, row in lecture_df.iterrows():
            lecture_scores.append(process_score_for_subcategory(row))

        # process Lab Subjects (30% of final grade)
        lab_df = df[df['Category'].str.contains('L-', regex=True)]
        for _, row in lab_df.iterrows():
            lab_scores.append(process_score_for_subcategory(row))

        lecture_grade = sum(lecture_scores) * 0.7  # 70% weight for lecture
        lab_grade = sum(lab_scores) * 0.3  # 30% weight for lab

        # combine grades
        return lecture_grade + lab_grade
    else:
        for _, row in df.iterrows():
            scores.append(process_score_for_subcategory(row))

    return sum(scores)


def process_score_for_subcategory(row):
    category = row['Category'].strip().upper()
    subcat = row['Subcategory'].strip()

    if subcat.lower() == 'attendance':
        return process_attendance(subcat)

    elif category == 'E':
        return process_exam(subcat)

    else:
        return process_assignments(subcat)


def process_attendance(subcat):
    while True:
        try:
            total_days = int(input(f"➤ Total number of classes for {subcat}: "))
            attended_days = int(input(f"➤ Days attended for {subcat}: "))
            if 0 <= attended_days <= total_days:
                percentage = (attended_days / total_days) * 100
                return percentage
            else:
                print("⚠️ Days attended must be between 0 and total days.")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers.")


def process_exam(subcat):
    while True:
        raw = input(f"➤ Enter score for {subcat} (format: score/max): ")
        try:
            score, max_score = map(float, raw.strip().split('/'))
            if 0 <= score <= max_score and max_score > 0:
                return (score / max_score) * 100
            else:
                print("⚠️ Score must be between 0 and max.")
        except:
            print("⚠️ Invalid format. Use score/max like 45/50")


def process_assignments(subcat):
    while True:
        try:
            num = int(input(f"➤ Enter number of assessments for {subcat}: "))
            if num > 0:
                break
            else:
                print("Must be greater than 0.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    total_score = 0
    total_max = 0
    for i in range(1, num + 1):
        while True:
            raw = input(f"   - Enter score {i} for {subcat} (format: score/max): ")
            try:
                score, max_score = map(float, raw.strip().split('/'))
                if 0 <= score <= max_score and max_score > 0:
                    total_score += score
                    total_max += max_score
                    break
                else:
                    print("⚠️ Score must be between 0 and max.")
            except:
                print("⚠️ Invalid format. Use score/max like 25/30")

    return (total_score / total_max) * 100 if total_max > 0 else 0


def calculate_final_grade(df, has_lab=False):
    return get_student_scores(df, has_lab)


def get_letter_grade(grade):
    if 70 <= grade <= 74: return 1.00
    elif 75 <= grade <= 79: return 1.50
    elif 80 <= grade <= 84: return 2.00
    elif 85 <= grade <= 88: return 2.50
    elif 89 <= grade <= 92: return 3.00
    elif 93 <= grade <= 96: return 3.50
    elif 97 <= grade <= 100: return 4.00
