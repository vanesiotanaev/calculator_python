import datetime

def write_log(user_exp, user_res):
    path = "log.txt"
    string = f'{datetime.datetime.now()}: {user_exp} = {user_res}'
    with open(path, 'a', encoding = 'utf_8') as file:
        file.write(f'{string}\n')
