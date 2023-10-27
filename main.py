def numberofquestion (number):
    if number == 1:
        s = 0
        k = 15
        d = k - 10
        k = 4 * d
        s = k - 50
        print (s)
    if number == 2:
        x = 3
        y = 4
        z = x + y
        z = z + 1
        x = y
        y = 5
        x = z + y + 7
        print(x)
    if number == 3:
        n = int(input('Random number'))
        print(' Первое число:',n,'\n','Второе число:',n+1,'\n','Третье число:',n+2,'\n')

    if number == 4:
        n = int(input('Число дайте'))
        x = int(input('Число дайте'))
        t = int(input('Число дайте'))
        print(n+x+t)
    if number == 5:
        n = int(input('длина ребра'))
        print('Площадь полной поверхности:',6*n**2,'\n','Объем:',n**3)
    if number == 6:
        a = int(input('First number a'))
        b = int(input('Second number b'))
        print('3*(a+b)^3 + 275*b^2 - 127*a - 41 =', 3*(a+b)**3 + 275*b**2 - 127*a -41)
    if number == 7:
        n = int(input('Your number:'))
        print('Следущее за число',n,'число:',n+1)
        print('Для числа',n,'предыдущее число:',n-1)
    if number == 8:
        n = int(input('Цена1'))
        b = int(input('Цена2'))
        c = int(input('Цена3'))
        e = int(input('Цена4'))
        print((n+b+c+e)*3)
    if number == 9:
        x = int(input('number 1'))
        y = int(input('number 2'))
        print(x+y,'suma \n', x*y,'proizvedenie \n',x-y, 'raznostb \n')
    if number == 10:
        y = int(input('Pervoe chislo'))
        x = int(input('vtoroe chislo'))
        n = int(input('tretbe chislo'))
        print(((2*n+(x-1)*y)*x/2))
    if number == 11:
        n = int(input('Chislo'))
        if n > 0:
            print(n,'---',2*n,'---',3*n,'---',4*n,'---',5*n,)
        else:
            print('прикол')
    if number == 12:
        y = int(input('Pervoe chislo'))
        x = int(input('vtoroe chislo'))
        n = int(input('tretbe chislo'))
        print(y*x**(n-1))
    if number == 13:
        n = int(input('Number'))
        if n > 0:
            print(n//100)
        else:
            print('прикол')

    if number == 14:
        n = int(input('Wkolota'))
        k = int(input('Mandariniiii'))
        print(k//n,'Celoe chislo mandarinov wolnikam\n',k%n,'v korzine')
    # if number == 15:
    #     n = int(input('Naselenie'))
    #     if n % 2 != 0:
    #


numbername = int(input('Which of ...?'))
numberofquestion(numbername)