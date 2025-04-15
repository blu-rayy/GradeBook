import pandas as pd

def load_template(filepath):
    try:
        df = pd.read_csv(filepath)

        # Check required columns
        required_columns = {'Category', 'Subcategory', 'Weight (%)'}
        if not required_columns.issubset(df.columns):
            raise ValueError("CSV must contain the columns: Category, Subcategory, and Weight (%)")

        # Convert weights to numeric
        df['Weight (%)'] = pd.to_numeric(df['Weight (%)'], errors='coerce')
        if df['Weight (%)'].isnull().any():
            raise ValueError("Some weights in the CSV are not valid numbers.")

        # Validate weights
        validate_category_weights(df)

        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        raise ValueError(str(e))

def validate_category_weights(df):
    cs_weight = df[df['Category'] == 'CS']['Weight (%)'].sum()
    e_weight = df[df['Category'] == 'E']['Weight (%)'].sum()

    errors = []
    if abs(cs_weight - 60) > 0.01:
        errors.append(f"CS category must total 60% (currently {cs_weight}%)")
    if abs(e_weight - 40) > 0.01:
        errors.append(f"E category must total 40% (currently {e_weight}%)")

    if errors:
        raise ValueError(" | ".join(errors))