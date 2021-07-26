import re


def arithmetic_arranger(problems, solve=True):

    first = ""
    second = ""
    lines = ""
    sumexp = ""
    string = ""

    # max number of expressions allowed is 5
    if (len(problems) > 5):
        return "Error: Too many problems."

    for problem in problems:
        # check the input as valid digits and operators
        if (re.search("[^\s0-9.+-]", problem)):
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        # split problem into separate variables
        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        # check the length of the number has max 4 digits
        if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
            return "Error: Numbers cannot be more than four digits."

        # store the sum of the expression
        sum = ""
        if (operator == '+'):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == '-'):
            sum = str(int(firstNumber) - int(secondNumber))

        # set length of expression and right align the values
        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)

        # set length of the dashes/lines
        line = ""
        for s in range(length):
            line += "-"

        # right align the sum result
        result = str(sum).rjust(length)

        # add four spaces between each problem EXCEPT the last one (-1)
        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumexp += result + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumexp += result


# if solve is TRUE print the string with result sumexp
    if solve:
        string = first + '\n' + second + '\n' + lines + '\n' + sumexp
    else:
        string = first + '\n' + second + '\n' + lines
    return string
