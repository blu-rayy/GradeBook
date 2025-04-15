import pandas as pd

def load_template(filepath, has_lab=False):
    try:
        df = pd.read_csv(filepath)

        # Check required columns
        required_columns = {'Category', 'Subcategory', 'Weight (%)'}
        if not required_columns.issubset(df.columns):
            raise ValueError("Template Structure Error: CSV must contain the columns: Category, Subcategory, and Weight (%)")

        # Convert weights to numeric
        df['Weight (%)'] = pd.to_numeric(df['Weight (%)'], errors='coerce')
        if df['Weight (%)'].isnull().any():
            raise ValueError("Weight Breakdown Error: Some weights in the CSV are not valid numbers.")

        # Validate weights based on if lab is included
        validate_category_weights(df, has_lab)

        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        raise ValueError(str(e))

def validate_category_weights(df, has_lab):
    if has_lab:
        # Check if L-CS and L-E categories are present
        if 'L-CS' not in df['Category'].values or 'L-E' not in df['Category'].values:
            raise ValueError("Template Structre Error: Template does not include categories for lab courses")

        # Validate L-CS and L-E categories for laboratory subject
        cs_weight = df[df['Category'] == 'L-CS']['Weight (%)'].sum()
        e_weight = df[df['Category'] == 'L-E']['Weight (%)'].sum()
        errors = []
        
        if abs(cs_weight - 60) > 0.01:
            errors.append(f"Weight Breakdown Error: L-CS for Lab category must total 60% (currently {cs_weight}%)")
        if abs(e_weight - 40) > 0.01:
            errors.append(f"Weight Breakdown Error: L-E for Lab category must total 40% (currently {e_weight}%)")

        if errors:
            raise ValueError(" | ".join(errors))
    else:
        # Validate regular CS and E categories
        cs_weight = df[df['Category'] == 'CS']['Weight (%)'].sum()
        e_weight = df[df['Category'] == 'E']['Weight (%)'].sum()
        errors = []

        if abs(cs_weight - 60) > 0.01:
            errors.append(f"Weight Breakdown Error: CS category must total 60% (currently {cs_weight}%)")
        if abs(e_weight - 40) > 0.01:
            errors.append(f"Weight Breakdown Error: E category must total 40% (currently {e_weight}%)")

        # Check if there are any L-CS or L-E categories when lab is not included
        if 'L-CS' in df['Category'].values or 'L-E' in df['Category'].values:
            errors.append("Template Structure Error: Template includes lab courses when it should not exist.")

        if errors:
            raise ValueError(" | ".join(errors))
