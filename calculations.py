# calculations.py

def get_student_scores(df):
    print("\n📥 Enter your scores per subcategory:")
    scores = []

    for _, row in df.iterrows():
        category = row['Category'].strip().upper()
        subcat = row['Subcategory'].strip()

        if subcat.lower() == 'attendance':
            while True:
                try:
                    total_days = int(input(f"➤ Total number of classes for {subcat}: "))
                    attended_days = int(input(f"➤ Days attended for {subcat}: "))
                    if 0 <= attended_days <= total_days:
                        percentage = (attended_days / total_days) * 100
                        break
                    else:
                        print("⚠️ Days attended must be between 0 and total days.")
                except ValueError:
                    print("⚠️ Invalid input. Please enter numbers.")
            scores.append(percentage)

        elif category == 'E':
            while True:
                raw = input(f"➤ Enter score for {subcat} (format: score/max): ")
                try:
                    score, max_score = map(float, raw.strip().split('/'))
                    if 0 <= score <= max_score and max_score > 0:
                        percentage = (score / max_score) * 100
                        break
                    else:
                        print("⚠️ Score must be between 0 and max.")
                except:
                    print("⚠️ Invalid format. Use score/max like 45/50")
            scores.append(percentage)

        else:
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

            percentage = (total_score / total_max) * 100 if total_max > 0 else 0
            scores.append(percentage)

    df['Subcategory Score (%)'] = scores
    df['Weighted Score'] = (df['Subcategory Score (%)'] * df['Weight (%)']) / 100
    return df

def calculate_final_grade(df):
    return df['Weighted Score'].sum()
