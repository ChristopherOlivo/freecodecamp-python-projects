# arithmetic_arranger.py

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts[0], parts[1], parts[2]

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'"

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits"

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"

        max_len = max(len(num1), len(num2))

        arranged_problems["top"].append(num1.rjust(max_len + 2))
        arranged_problems["bottom"].append(operator + num2.rjust(max_len + 1))
        arranged_problems["line"].append('-' * (max_len + 2))

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            arranged_problems["result"].append(result.rjust(max_len + 2))

    if show_answers:
        return "\n".join([
            "    ".join(arranged_problems["top"]),
            "    ".join(arranged_problems["bottom"]),
            "    ".join(arranged_problems["line"]),
            "    ".join(arranged_problems["result"])
        ])
    else:
        return "\n".join([
            "    ".join(arranged_problems["top"]),
            "    ".join(arranged_problems["bottom"]),
            "    ".join(arranged_problems["line"])
        ])
