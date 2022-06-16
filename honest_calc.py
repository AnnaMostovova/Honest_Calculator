memory = 0
work = True

messages = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            " ... lazy", " ... very lazy", " ... very, very lazy", "You are",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]


def check(v1, v2, v3):
    msg = ''
    msg += messages[6] if is_one_digit(v1) and is_one_digit(v2) else ''
    msg += messages[7] if v1 == 1 or v2 == 2 else ''
    msg += messages[8] if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-') else ''
    if msg != '':
        msg = messages[9] + msg
        print(msg)


def is_one_digit(v):
    return int(v) == v and -10 < v < 10


while work:
    calc = input(messages[0]).split(' ')
    operation = calc[1]

    try:
        x = memory if calc[0] == 'M' else float(calc[0])
        y = memory if calc[2] == 'M' else float(calc[2])
    except ValueError:
        print(messages[1])
        continue

    if operation in ('+', '-', '*', '/'):
        check(x, y, operation)
        if operation == '+':
            res = x + y
        elif operation == '-':
            res = x - y
        elif operation == '*':
            res = x * y
        elif y != 0:
            res = x / y
        else:
            print(messages[3])
            continue
    else:
        print(messages[2])
        continue

    print(res)
    work = False

    store_answer = ''
    while store_answer != 'y' and store_answer != 'n':
        store_answer = input(messages[4])
        if store_answer == 'y':
            if is_one_digit(res):
                msg_index = 10
                answer = ''
                while answer != 'n' and msg_index <= 12:
                    answer = input(messages[msg_index])
                    if answer == 'y':
                        msg_index += 1
                if answer == 'n':
                    break
            memory = res

    cont_answer = ''
    while cont_answer != 'y' and cont_answer != 'n':
        cont_answer = input(messages[5])
        if cont_answer == 'y':
            work = True
