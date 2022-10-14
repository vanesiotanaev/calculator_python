exp = 0

def init(user_exp):
    global exp
    exp = user_exp

def operation(exp):
    math_ops = {'*': lambda x, y: int(x) * int(y),
            '/': lambda x, y: int(x) / int(y),
            '+': lambda x, y: int(x) + int(y),
            '-': lambda x, y: int(x) - int(y)}

    exp = exp.replace(' ', '').strip()
    exp = exp.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    exp = list(exp.split())

    if exp[0] == '-':
        exp.pop(0)
        exp[0] = str(int(exp[0]) * (-1))

    while "*" in exp or "/" in exp:    
        for i in range(len(exp)):
            if exp[i] in math_ops.keys() and exp[i] == '*':      
                exp[i - 1] = math_ops.get(exp[i])(int(exp[i-1]), int(exp[i+1])) 
                del exp[i: i+2] 
                break
            elif exp[i] in math_ops.keys() and exp[i] == '/':
                if not exp[i+1] == '0': 
                    exp[i - 1] = math_ops.get(exp[i])(int(exp[i-1]), int(exp[i+1]))
                    del exp[i: i+2]
                    break
                else:
                    return False
    while "+" in exp or "-" in exp: 
        for i in range(len(exp)):   
            if exp[i] in math_ops.keys() and exp[i] == '+':      
                exp[i - 1] = math_ops.get(exp[i])(int(exp[i-1]), int(exp[i+1])) 
                del exp[i: i+2]
                break
            elif exp[i] in math_ops.keys() and exp[i] == '-':
                exp[i - 1] = math_ops.get(exp[i])(int(exp[i-1]), int(exp[i+1]))
                del exp[i: i+2]
                break
    return exp[0]