import _datetime
import ast

passports = []
clients = []
errors = []

f = 1

while f == 1:
    passports.append(ast.literal_eval(input('Паспорт:')))
    input_data = list(input('Клиент:').split(','))
    input_data[1] = input_data[1][2:len(input_data[1])-1]
    clients.append(input_data)
    f = int(input('1 - Добавить данные , 2 - Проверка: '))

black_city = input('запретный город: ' + '\n')

for i in range(len(passports)):
    
    birth = list(map(int, passports[i]['birth'].split(':')))
    today = _datetime.date.today()
    date1 = _datetime.date(birth[2],birth[1],birth[0])
    years =(today-date1).days//360
    ageError = 0
    ageError += abs(years-int(clients[i][0]))

    nameError = 0
    name = [passports[i]['fname'], passports[i]['mname'], passports[i]['lname']]
    k = list(map(str, clients[i][1].split(" ")))
    if len(k)==3:
        k[0], k[1] = k[1], k[0]
        k[1], k[2] = k[2], k[1]

    for i in range(len(k)):
        if len(k[i]) >= len(name[i]):
            for c in range(len(k[i])):
                if name[i].find(k[i][c], c) != c:
                    nameError +=1
        else:
            for c in range(len(name[i])):
                if k[i].find(name[i][c], c) != c:
                    nameError +=1
    

    if ageError == 0 and nameError == 0 and passports[i]['city'] != black_city:
        errors.append([])
    else:
        error = []
        if ageError != 0:
            error.append('Неправильный возраст.')
        
        if nameError > 2:
            error.append('Неправильное фио.')
        
        if passports[i]['city'] == black_city:
            error.append('Запрещённый город.')
        
        errors.append(error)


for i in range(len(errors)):
    errors[i] = ''.join(errors[i])

for i in range(len(errors)):
    if len(errors[i]) != 0:
        print(f'{i + 1} клиент. Не пропускать:'+ errors[i])
    else:
        print(f'{i + 1} клиент. Пропускать')

