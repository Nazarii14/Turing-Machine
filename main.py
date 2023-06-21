def change_head_position(direction, head_position):
    return head_position + 1 if direction == "R" else head_position - 1


def add_unary_numbers(num1, num2):
    tape = num1 + "+" + num2 + " "

    transition_rules = {
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "+"): ("q1", "1", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", " "): ("q2", " ", "L"),
        ("q2", "1"): ("q2", " ", "R"),
        ("q2", " "): ("qf", " ", "L"),
    }

    state, head_position = "q0", 0

    while state != "qf":
        symbol = tape[head_position]
        new_state, new_symbol, direction = transition_rules[(state, symbol)]
        tape = tape[:head_position] + new_symbol + tape[head_position + 1:]

        head_position = change_head_position(direction, head_position)
        state = new_state

    result = tape[:-2]
    return result


def add_binary_numbers(num1, num2):
    tape = "  " + num1 + "+" + num2 + "  "

    transition_rules = {
        ("q0", " "): ("q0", " ", "R"),
        ("q0", "0"): ("q0", "0", "R"),
        ("q0", "1"): ("q0", "1", "R"),

        ("q0", "+"): ("q1", "+", "R"),
        ("q1", "0"): ("q1", "0", "R"),
        ("q1", "1"): ("q1", "1", "R"),

        ("q1", " "): ("q2", " ", "L"),
        ("q2", "0"): ("q2", "1", "L"),
        ("q2", "1"): ("q3", "0", "L"),

        ("q2", "+"): ("q5", " ", "R"),
        ("q3", "0"): ("q3", "0", "L"),
        ("q3", "1"): ("q3", "1", "L"),

        ("q3", "+"): ("q4", "+", "L"),
        ("q4", "0"): ("q0", "1", "R"),
        ("q4", "1"): ("q4", "0", "L"),

        ("q4", " "): ("q0", "1", "R"),
        ("q5", "1"): ("q5", " ", "R"),
        ("q5", " "): ("qf", " ", "N"),
    }

    state, head_position = "q0", 0

    while state != "qf":
        symbol = tape[head_position]
        new_state, new_symbol, direction = transition_rules[(state, symbol)]
        tape = tape[:head_position] + new_symbol + tape[head_position + 1:]

        head_position = change_head_position(direction, head_position)
        state = new_state

    result = tape
    return int(result)


def subtraction_unary_numbers(num1, num2):
    if num1 < num2:
        return f"Error '{num1}' < '{num2}'"
    tape = "  " + num1 + "-" + num2 + "  "

    transition_rules = {
        ("q0", " "): ("q0", " ", "R"),
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "-"): ("q1", "-", "R"),

        ("q1", "1"): ("q1", "1", "R"),
        ("q1", " "): ("q2", " ", "L"),
        ("q2", "1"): ("q3", " ", "L"),

        ("q2", "-"): ("qf", " ", "N"),
        ("q3", "1"): ("q3", "1", "L"),
        ("q3", "-"): ("q4", "-", "L"),

        ("q4", "1"): ("q4", "1", "L"),
        ("q4", " "): ("q5", " ", "R"),
        ("q5", "1"): ("q0", " ", "R"),
    }

    state, head_position = "q0", 0

    while state != "qf":
        symbol = tape[head_position]
        new_state, new_symbol, direction = transition_rules[(state, symbol)]
        tape = tape[:head_position] + new_symbol + tape[head_position + 1:]

        head_position = change_head_position(direction, head_position)
        state = new_state

    result = tape

    try:
        return int(result)
    except:
        return 0


def multiplication_unary_numbers(num1, num2):
    tape = " " + num1 + "*" + num2 + "=" + " " * len(num1) * len(num2)

    transition_rules = {
        ("q0", "1"): ("q1", "X", "R"),
        ("q0", "*"): ("q11", "*", "L"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "*"): ("q2", "*", "R"),

        ("q2", "1"): ("q4", "Y", "R"),
        ("q2", "="): ("q3", "=", "L"),
        ("q3", "Y"): ("q3", "1", "L"),
        ("q3", "*"): ("q9", "*", "L"),

        ("q4", "1"): ("q4", "1", "R"),
        ("q4", "="): ("q5", "=", "R"),
        ("q5", "1"): ("q5", "1", "R"),
        ("q5", " "): ("q6", "1", "L"),

        ("q6", "1"): ("q6", "1", "L"),
        ("q6", "="): ("q7", "=", "L"),
        ("q7", "1"): ("q7", "1", "L"),
        ("q7", "Y"): ("q8", "Y", "R"),

        ("q8", "1"): ("q4", "Y", "R"),
        ("q8", "="): ("q3", "=", "L"),
        ("q9", "1"): ("q9", "1", "L"),
        ("q9", "X"): ("q0", "X", "R"),

        ("q11", "X"): ("q11", "1", "L"),
        ("q11", " "): ("qf", " ", "R")
    }

    state = "q0"
    head_position = 1

    while state != "qf":
        symbol = tape[head_position]
        new_state, new_symbol, direction = transition_rules[(state, symbol)]
        tape = tape[:head_position] + new_symbol + tape[head_position + 1:]
        if direction == "R":
            head_position += 1
        elif direction == "L":
            head_position -= 1
        state = new_state

    result = tape[1:]
    return result


def transfer_from_unary_to_denary_numbers(num1):
    tape = " " * (len(num1) // 10 + 2) + num1 + " "

    transition_rules = {
        ("q0", "|"): ("q1", "|", "L"),
        ("q0", " "): ("qf", "0", "R"),
        ("q1", " "): ("q2", "=", "L"),
        ("q2", " "): ("q3", "0", "R"),

        ("q3", "="): ("q3", "=", "R"),
        ("q3", "|"): ("q3", "|", "R"),
        ("q3", "0"): ("q3", "0", "R"),
        ("q3", "1"): ("q3", "1", "R"),

        ("q3", "2"): ("q3", "2", "R"),
        ("q3", "3"): ("q3", "3", "R"),
        ("q3", "4"): ("q3", "4", "R"),
        ("q3", "5"): ("q3", "5", "R"),

        ("q3", "6"): ("q3", "6", "R"),
        ("q3", "7"): ("q3", "7", "R"),
        ("q3", "8"): ("q3", "8", "R"),
        ("q3", "9"): ("q3", "9", "R"),

        ("q3", " "): ("q4", " ", "L"),
        ("q4", "|"): ("q5", " ", "L"),
        ("q4", "="): ("qf", " ", "L"),
        ("q5", "|"): ("q5", "|", "L"),

        ("q5", "="): ("q6", "=", "L"),
        ("q6", "9"): ("q6", "0", "L"),
        ("q6", " "): ("q3", "1", "R"),
        ("q6", "0"): ("q3", "1", "R"),

        ("q6", "1"): ("q3", "2", "R"),
        ("q6", "2"): ("q3", "3", "R"),
        ("q6", "3"): ("q3", "4", "R"),
        ("q6", "4"): ("q3", "5", "R"),

        ("q6", "5"): ("q3", "6", "R"),
        ("q6", "6"): ("q3", "7", "R"),
        ("q6", "7"): ("q3", "8", "R"),
        ("q6", "8"): ("q3", "9", "R"),
    }

    state, head_position = "q0", len(num1)//10+2

    while state != "qf":
        symbol = tape[head_position]
        new_state, new_symbol, direction = transition_rules[(state, symbol)]
        tape = tape[:head_position] + new_symbol + tape[head_position + 1:]

        head_position = change_head_position(direction, head_position)
        state = new_state

    result = tape
    return int(result)


def task_1():
    print("Додавання двох чисел в унарній системі:")
    a, b = "111", "111"
    result = add_unary_numbers(a, b)
    print(f"'{a}' + '{b}' = '{result}'")
    a, b = "11", "11111"
    result = add_unary_numbers(a, b)
    print(f"'{a}' + '{b}' = '{result}'")


def task_2():
    print("Додавання двох чисел у двійковій системі:")
    a, b = "111", "111"
    result = add_binary_numbers(a, b)
    print(f"'{a}' + '{b}' = '{result}'")
    a, b = "11", "1001"
    result = add_binary_numbers(a, b)
    print(f"'{a}' + '{b}' = '{result}'")


def task_3():
    print("Віднімання двох чисел в унарній системі:")
    a, b = "111", "111"
    result = subtraction_unary_numbers(a, b)
    print(f"'{a}' - '{b}' = '{result}'")
    a, b = "11", "1111"
    result = subtraction_unary_numbers(a, b)
    print(f"'{a}' - '{b}' = {result}")
    a, b = "11111", "11"
    result = subtraction_unary_numbers(a, b)
    print(f"'{a}' - '{b}' = '{result}'")


def task_4():
    print("Множення двох чисел в унарній системі:")
    a, b = "111", "111"
    result = multiplication_unary_numbers(a, b)
    print(f"{result}")
    a, b = "11", "111"
    result = multiplication_unary_numbers(a, b)
    print(f"{result}")


def task_5():
    print("Переведення числа в унарному записі у десятковий запис:")
    a = "|||"
    result = transfer_from_unary_to_denary_numbers(a)
    print(f"'{a}' -> {result}")
    a = "||||||||||"
    result = transfer_from_unary_to_denary_numbers(a)
    print(f"'{a}' -> {result}")


functions = [task_1, task_2, task_3, task_4, task_5]

for i in range(len(functions)):
    print(f"Task {i+1}")
    functions[i]()
    print()
