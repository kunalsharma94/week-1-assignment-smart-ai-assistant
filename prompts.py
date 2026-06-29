TOOLS_DESCRIPTION = """
Available tools:

1. calculate_age(birth_year)
   Description: Calculate age from birth year.

2. get_current_time()
   Description: Get the current date and time.

3. calculate_percentage(obtained, total)
   Description: Calculate percentage.

4. calculate_day_of_week(date_string)
   Description: Find the day of the week from a date.

5. calculate_bmi(weight, height_cm)
   Description: Calculate Body Mass Index (BMI) from weight in kg and height in cm.
6. ask_gemini(question)
   Description: Ask Gemini a question and get an answer.
"""

TOOL_SELECTION_TEMPLATE = """
You are an AI agent.

{tools}

Return ONLY valid JSON.

Examples:

{{
    "tool": "calculate_age",
    "birth_year": 1993
}}

{{
    "tool": "get_current_time"
}}

{{
    "tool": "calculate_percentage",
    "obtained": 425,
    "total": 500
}}

{{
    "tool": "calculate_day_of_week",
    "date_string": "2026-08-15"
}}

{{
    "tool": "calculate_bmi",
    "weight": 72,
    "height_cm": 175
}}

{{
    "tool":"calculator",
    "expression":"25+30"
}}

{{
    "tool":"none",
    "answer":"React was created by Jordan Walke..."
}}


Calculator Tool
Supports:
- Addition
- Subtraction
- Multiplication
- Division

User Request:
{user_input}
"""

FINAL_RESPONSE_TEMPLATE = """
User Question:
{user_input}

Tool Used:
{tool_name}

Tool Result:
{result}

Create a helpful and friendly response.

Rules:
- Do not mention JSON.
- Do not mention internal tools.
- Answer naturally.
"""
