from datetime import datetime
# -----------------------------
# Tools
# -----------------------------

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_age(birth_year):
    return datetime.now().year - birth_year


def calculate_day_of_week(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").strftime("%A")


def calculate_percentage(total, obtained):
    if total <= 0:
        raise ValueError("Total marks must be greater than 0")

    return (obtained / total) * 100

def calculate_bmi(weight=72, height_cm=175):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    if height_cm <= 0:
        raise ValueError(
            "Height must be greater than zero."
        )
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return f"BMI: {bmi:.2f} ({category})"

def calculator(expression: str) -> str:
    try:
        # Allow only numbers, operators, parentheses, decimal points, and spaces
        allowed = "0123456789+-*/(). "

        if not all(char in allowed for char in expression):
            return "Invalid expression."

        result = eval(expression, {"__builtins__": None}, {})

        return str(result)

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except Exception:
        return "Invalid mathematical expression."

def ask_gemini(user_query):
    return user_query