def arithmetic_arranger(problems, solve=False):
    # 1) Validate number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    for prob in problems:
        parts = prob.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        a, op, b = parts

        # 2) Validate operator
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # 3) Validate digits
        if not (a.isdigit() and b.isdigit()):
            return "Error: Numbers must only contain digits."

        # 4) Validate length
        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width for this problem
        width = max(len(a), len(b)) + 2

        # Build lines
        top_line.append(a.rjust(width))
        bottom_line.append(op + b.rjust(width - 1))
        dash_line.append('-' * width)

        if solve:
            result = str((int(a) + int(b)) if op == '+' else (int(a) - int(b)))
            answer_line.append(result.rjust(width))

    arranged = '    '.join(top_line) + '\n' + '    '.join(bottom_line) + '\n' + '    '.join(dash_line)
    if solve:
        arranged += '\n' + '    '.join(answer_line)

    return arranged
