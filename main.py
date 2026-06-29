import re
import json
import sys
import config
import prompts
import tools



# -----------------------------
# User Input
# -----------------------------

user_input = input(
    """
Ask me about:
- Current Time
- Age (e.g. I was born in 1993)
- Day of Week (e.g. 2026-08-15)
- Percentage (e.g. Calculate percentage of 425 out of 500)
- BMI (e.g. Calculate BMI for 72 kg and 175 cm)
- Calculator (e.g. 5 + 3 * (2 - 1))
- Ask Gemini (e.g. What is the capital of France?)

Your Question:
"""
)

# -----------------------------
# Build Tool Selection Prompt
# -----------------------------

tool_selection_prompt = prompts.TOOL_SELECTION_TEMPLATE.format(
    tools=prompts.TOOLS_DESCRIPTION,
    user_input=user_input
)


# -----------------------------
# Gemini Call #1
# Tool Selection
# -----------------------------

response = config.CLIENT.models.generate_content(
    model=config.MODEL_NAME,
    contents=tool_selection_prompt
)

# -----------------------------
# Clean JSON Response
# -----------------------------

model_response = re.sub(
    r"^```json\s*|\s*```$",
    "",
    response.text.strip()
)

# -----------------------------
# Parse JSON
# -----------------------------

try:
    tool_call = json.loads(model_response)
except json.JSONDecodeError:
    print("Invalid JSON received from Gemini.")
    sys.exit()

tool_name = tool_call.get("tool")

# -----------------------------
# Execute Tool
# -----------------------------

try:

    if tool_name == "calculate_age":

        result = tools.calculate_age(
            tool_call["birth_year"]
        )

    elif tool_name == "get_current_time":

        result = tools.get_current_time()

    elif tool_name == "calculate_percentage":

        result = tools.calculate_percentage(
            obtained=tool_call["obtained"],
            total=tool_call["total"]
        )

    elif tool_name == "calculate_day_of_week":

        result = tools.calculate_day_of_week(
            tool_call["date_string"]
        )
    elif tool_name == "calculate_bmi":

        result = tools.calculate_bmi(
            weight=tool_call.get("weight", 72),
            height_cm=tool_call.get("height_cm", 175)
        )
    elif tool_name == "calculator":
        expression = tool_call["expression"]
        result = tools.calculator(expression)

    elif tool_name == "ask_gemini":
        question = tool_call["question"]
        result = tools.ask_gemini(question)

    else:

        print(f"Unknown tool selected: {tool_name}")
        sys.exit()

except Exception as e:

    print(f"Tool execution failed: {e}")
    sys.exit()

# -----------------------------
# Build Final Response Prompt
# -----------------------------

final_prompt = prompts.FINAL_RESPONSE_TEMPLATE.format(
    user_input=user_input,
    tool_name=tool_name,
    result=result
)

# -----------------------------
# Gemini Call #2
# Final Response
# -----------------------------

final_response = config.CLIENT.models.generate_content(
    model=config.MODEL_NAME,
    contents=final_prompt
)

# -----------------------------
# Output
# -----------------------------

print("\nSmart AI Assignment:")
print(final_response.text)