#Реализовать программу, при помощи которой 3 игрока могут играть в игру «Лоскутное одеяло». Правила игры следующие. 
#На поле, имеющем размер 4 на 5 клеток за один ход каждый игрок должен заполнить одну клетку своим символом. 
#Игрок старается, чтобы его символы были как можно дальше друг от друга. В ходе игры ведется подсчет очков: за каждое соседство 
#клеток с одинаковыми символами игроку, владельцу символа добавляется одно штрафное очко. Соседними считаются клетки, имеющие 
#общую сторону или расположенные наискосок друг от друга. Выигрывает тот, у кого в конце игры меньше всего штрафных очков.
#Взаимодействие с программой производится через консоль. Игровое поле изображается в виде 4 текстовых строк и перерисовывается 
#при каждом изменении состояния поля. При запросе данных от пользователя программа сообщает, что ожидает от пользователя 
#(например, координаты очередного хода) и проверяет корректность ввода. Программа должна уметь автоматически определять 
#количество штрафных очков и окончание партии и ее победителя.
#Сама программа НЕ ходит, т.е. не пытается заполнять клетки символами с целью выиграть игру.


#Игроки
print('Уважаемые игроки "Лоскутного Одеяла", пожалуйста, определитесь с очерёдностью своих ходов, а затем введите свои ники и выберите символ, которым вы будете играть (кроме минуса). Вводите это следующим образом по указанному образцу: Сергей-!; Андрей-*; Соня-№; ...')
P1 = str(input('Player1 = '))
if (len(P1) < 3) or (P1[-2] != '-') or (P1[-1] == '-'):
    while (len(P1) < 3) or (P1[-2] != '-') or (P1[-1] == '-'):
        print('Некорректный ввод! Введите ник ещё раз!')
        P1 = str(input('Player1 = '))
P2 = str(input('Player2 = '))
if (len(P2) < 3) or (P2[-2] != '-') or (P2[-1] == '-') or (P2[-1] == P1[-1]) or (P2[:-2] == P1[:-2]):
    while (len(P2) < 3) or (P2[-2] != '-') or (P2[-1] == '-') or (P2[-1] == P1[-1]) or (P2[:-2] == P1[:-2]):
        print('Некорректный ввод! Введите ник ещё раз!')
        P2 = str(input('Player2 = '))
P3 = str(input('Player3 = '))
if (len(P3) < 3) or (P3[-2] != '-') or (P3[-1] == '-') or (P3[-1] == P2[-1]) or (P3[-1] == P1[-1]) or (P3[:-2] == P2[:-2]) or (P3[:-2] == P1[:-2]):
    while (len(P3) < 3) or (P3[-2] != '-') or (P3[-1] == '-') or (P3[-1] == P2[-1]) or (P3[-1] == P1[-1]) or (P3[:-2] == P2[:-2]) or (P3[:-2] == P1[:-2]):
        print('Некорректный ввод! Введите ник ещё раз!')
        P3 = str(input('Player3 = '))

I1 = P1[:-2]
I2 = P2[:-2]
I3 = P3[:-2]

S1 = P1[-1]
S2 = P2[-1]
S3 = P3[-1]


#Поле
Pole = []
stroka = []
for m in range(4):
    for n in range(5):
        stroka.append('-')
        if n == 4:
            Pole.append(stroka)
            stroka = []
Str1 = Pole[0]
Str2 = Pole[1]
Str3 = Pole[2]
Str4 = Pole[3]
print('')
print(Str1)
print(Str2)
print(Str3)
print(Str4)
print('')


#Ход игрока, промежуточный подсчёт очков
Xod = 0
Ochki = {0:0, 1:0, 2:0} #Словарь очков игроков, где ключ "0" соответствует очкам 1 игрока, "1" - 2, "2" - 3
Im = {0:I1, 1:I2, 2:I3} #Словарь ников
Sim = {0:S1, 1:S2, 2:S3} #Словарь символов

def XodIgroka(Xod,x,y):
    if (x >= 0 and x <= 3) and (y >= 0 and y <= 4) and ((Pole[x])[y] == '-'):
        (Pole[x])[y] = Sim[Xod%3]
        print(Str1)
        print(Str2)
        print(Str3)
        print(Str4)
    else:
        while ((x < 0) or (x > 3) or (y < 0) or (y > 4) or ((Pole[x])[y] != '-')):
            print('Некорректный ввод! Введите координаты ещё раз!')
            try:
                x = int(input('x = (0,1,2,3) '))
                y = int(input('y = (0,1,2,3,4) '))
            except ValueError:
                x = y = 1000
            if (x >= 0 and x <= 3) and (y >= 0 and y <= 4) and ((Pole[x])[y] == '-'):
                (Pole[x])[y] = Sim[Xod%3]
                print(Str1)
                print(Str2)
                print(Str3)
                print(Str4)
                break
    if (x == 0 and y == 0):
        if (Pole[x])[y] == (Pole[x+1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y+1]:
            Ochki[Xod%3] -= 1
    elif (x == 3 and y == 0):
        if (Pole[x])[y] == (Pole[x-1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y+1]:
            Ochki[Xod%3] -= 1
    elif (x == 0 and y == 4):
        if (Pole[x])[y] == (Pole[x])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y-1]:
            Ochki[Xod%3] -= 1
    elif (x == 3 and y == 4):
        if (Pole[x])[y] == (Pole[x])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y-1]:
            Ochki[Xod%3] -= 1
    elif ((x > 0 and x < 3) and y == 0):
        if (Pole[x])[y] == (Pole[x-1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y+1]:
            Ochki[Xod%3] -= 1
    elif ((x > 0 and x < 3) and y == 4):
        if (Pole[x])[y] == (Pole[x+1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y-1]:
            Ochki[Xod%3] -= 1
    elif (x == 0 and (y > 0 and y < 4)):
        if (Pole[x])[y] == (Pole[x])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y-1]:
            Ochki[Xod%3] -= 1
    elif (x == 3 and (y > 0 and y < 4)):
        if (Pole[x])[y] == (Pole[x])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y-1]:
            Ochki[Xod%3] -= 1
    else:
        if (Pole[x])[y] == (Pole[x+1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y-1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x-1])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y+1]:
            Ochki[Xod%3] -= 1
        if (Pole[x])[y] == (Pole[x+1])[y-1]:
            Ochki[Xod%3] -= 1
    print('')
    print(I1,Ochki[0])
    print(I2,Ochki[1])
    print(I3,Ochki[2])
    print('')

while Xod < 20:
    print(Im[Xod%3] + ', ваш ход! Выбирайте строку(x) и столбец(y), где вы разместите свой символ!')
    try:
        x = int(input('x = (0,1,2,3) '))
        y = int(input('y = (0,1,2,3,4) '))
    except ValueError:
        x = y = 1000
    XodIgroka(Xod,x,y)
    Xod += 1


#Конец игры
if (Ochki[0] > Ochki[1]) and (Ochki[0] > Ochki[2]):
    print(I1 + ' победил!')
elif (Ochki[1] > Ochki[0]) and (Ochki[1] > Ochki[2]):
    print(I2 + ' победил!')
elif (Ochki[2] > Ochki[0]) and (Ochki[2] > Ochki[1]):
    print(I3 + ' победил!')
elif (Ochki[0] == Ochki[1]) and (Ochki[0] != Ochki[2]):
    print(I1 + ' и ' + I2 + ' победили!')
elif (Ochki[0] == Ochki[2]) and (Ochki[0] != Ochki[1]):
    print(I1 + ' и ' + I3 + ' победили!')
elif (Ochki[1] == Ochki[2]) and (Ochki[1] != Ochki[0]):
    print(I2 + ' и ' + I3 + ' победили!')
else:
    print('Победила дружба!')
