exp = 0

def init(user_exp):
    global exp
    exp = user_exp

def operation(exp):
    exp = exp.split()
    while '*' in exp or "/" in exp and len(exp) > 1:
        for i in range(len(exp)):
            if exp[i] == '*' or exp[i] == '/':
                if exp[i] == '*':
                    exp[i - 1] = int(exp[i - 1]) * int(exp[i + 1])
                    del exp[i:i+2]
                    print(' '.join(map(str, exp))) # Перевожу поэлементно список 'a' в str.
                    break
                if exp[i] == '/':
                    exp[i - 1] = int(exp[i - 1]) / int(exp[i + 1])
                    del exp[i:i+2]
                    print(' '.join(map(str, exp)))
                    break
    while ('+' in exp or '-' in exp) and len(exp) > 1:
        for i in range(len(exp)):
            if exp[i] == '+' or exp[i] == '-':
                if exp[i] == '+':
                    exp[i-1] = int(exp[i-1]) + int(exp[i+1])
                    del exp[i:i+2]
                    print(' '.join(map(str, exp)))
                    break
                if exp[i] == '-':
                    exp[i-1] = int(exp[i-1]) - int(exp[i+1])
                    del exp[i:i+2]
                    print(' '.join(map(str, exp)))
                    break

    return exp