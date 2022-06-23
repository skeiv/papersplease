import _datetime
import ast
from random import randint


passports = []
clients = []
errors = []
ent = []
noent=[]
strange = []
stonks = 0
res = []
f = 1

while f == 1:
    passports.append(ast.literal_eval(input('Паспорт:')))
    input_data = list(input('Клиент:').split(','))
    input_data[1] = input_data[1][2:len(input_data[1])-1]
    clients.append(input_data)
    f = int(input('1 - Добавить данные , 2 - Проверка: '))

print()
black_city = input('запретный город: ' + '\n')

for i in range(len(passports)):
    
    birth = list(map(int, passports[i]['birth'].split(':')))
    today = _datetime.date.today()
    date1 = _datetime.date(birth[2],birth[1],birth[0])
    years =(today-date1).days//360
    ageError = 0
    ageError += abs(years-int(clients[i][0]))
    pay =0 
    nameError = 0
    name = [passports[i]['fname'], passports[i]['mname'], passports[i]['lname']]
    k = list(map(str, clients[i][1].split(" ")))
    if len(k)==3:
        k[0], k[1] = k[1], k[0]
        k[1], k[2] = k[2], k[1]

    for j in range(len(k)):
        if len(k[j]) >= len(name[j]):
            for c in range(len(k[j])):
                if name[j].find(k[j][c], c) != c:
                    nameError +=1
        else:
            for c in range(len(name[j])):
                if k[j].find(name[j][c], c) != c:
                    nameError +=1
    
    if passports[i]['city'] == black_city:
        print(f'Клиент {i+1} - не проходишь, запрещенный город\n')
        res.append(f'Клиент {clients[i]} - не проходит. Запрещённый город')
        noent.append(f'Клиент {clients[i]}')
        continue

    if nameError+ageError == 0:
        print(f'Клиент {i+1} - проходишь\n')
        res.append(f'Клиент {clients[i]} - проходит')
        ent.append(f'Клиент {clients[i]}')

    else:
        if ageError >= 1:
            ageError = 1
        else:
            ageError = 0
        f = input(f'Клиент {i+1} - хочешь пройти за {(nameError+ageError)*250} уе?')
        if f == '1':
            stonks += (nameError+ageError)*250
            pay = (nameError+ageError)*250
            if randint(0, 1) == 1:
                print(f'Клиент {i+1} - проходишь (повезло)\n')
                res.append(f'Клиент {clients[i]} - проходит (повезло). Ошибок в фио {nameError}, ошибок в возрасте {ageError}, заплатил {pay}, но странный')
                ent.append(f'Клиент {clients[i]}')
                strange.append(f'Клиент {clients[i]}')

            else:
                print(f'Клиент {i+1} - не проходишь (не повезло)\n')
                res.append(f'Клиент {clients[i]} - не проходит (не повезло). Ошибок в фио {nameError}, ошибок в возрасте {ageError}, заплатил {pay}')
                noent.append(f'Клиент {clients[i]}')
                strange.append(f'Клиент {clients[i]}')

        else:
            print(f'Клиент {i+1} - не проходишь, не захотел платить')
            res.append(f'Клиент {clients[i]} - не проходишь, не захотел платить. Ошибок в фио {nameError}, ошибок в возрасте {ageError}')
            noent.append(f'Клиент {clients[i]}')

print()

for e in res:
    print(e)
print()

print('Прошли:')
for e in ent:
    print(e)
print()
print('Не прошли:')
for e in noent:
    print(e)
print()
print('Странные:')
for e in strange:
    print(e)

print()

print('\n' + f'поднял: {stonks}')