import _datetime
import ast

while 1 :
    print('Введите паспортные данные:')
    passport = ast.literal_eval(input())
    print('Введите информацию о клиенте:')


    name = [passport['fname'], passport['mname'], passport['lname']]
    input_data = list(input().split(','))
    input_data[1] = input_data[1][2:len(input_data[1])-1]

    birth = list(map(int, passport['birth'].split(':')))
    today = _datetime.date.today()
    date1 = _datetime.date(birth[2],birth[1],birth[0])
    years =(today-date1).days//360
    error = 0
    error += abs(years-int(input_data[0]))

    k = list(map(str, input_data[1].split(" ")))
    if len(k)==3:
        k[0], k[1] = k[1], k[0]
        k[1], k[2] = k[2], k[1]

    for i in range(len(k)):
        if len(k[i]) >= len(name[i]):
            for c in range(len(k[i])):
                if name[i].find(k[i][c], c) != c:
                    error +=1
        else:
            for c in range(len(name[i])):
                if k[i].find(name[i][c], c) != c:
                    error +=1

    if error>2:
        print("Отказать")
    else: 
        print("Пропустить")