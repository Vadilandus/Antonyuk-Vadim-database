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
        print('Следущее за числом',n,'число:',n+1)
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
    if number == 15:
        n = int(input('Naselenie'))
        if n % 2 != 0:
            print(n//2+1)
        else:
            print(n//2)
    if number == 16:
        n = int(input('nomer'))
        print(n//4+1)
    if number == 17:
        n = int(input('minuts'))
        hours = n//60
        minut = n%60
        print(hours,'hours',minut,'minut')
    if number == 18:
        n = int(input('chislo'))
        f = n//100
        s = n//10%10
        l = n%10
        print(f+s+l,f*s*l)
    if number == 19:
        n = int(input('chislo'))
        f = n // 100
        s = n // 10 % 10
        l = n % 10
        f = str(f)
        s = str(s)
        l = str(l)
        print(f+s+l)
        print(f+l+s)
        print(s+f+l)
        print(s+l+f)
        print(l+f+s)
        print(l+s+f)
    if number == 20:
        n = int(input('chislo'))
        print(n//1000,n%1000//100,n%100//10,n%10)
    if number == 21:
        n = input('password')
        s = input('password2')
        if n == s:
            print('Password is true')
        else:
            print('Password is false')
    if number == 22:
        n = int(input('chislo'))
        if n % 2 !=0:
            print('Нечетное')
        else:
            print('Четное')
    if number == 23:
        n = int(input('chislo'))
        a = n // 1000
        b = n % 1000 // 100
        c = n % 100 // 10
        d = n % 10
        if a+d == b-c:
            print('DA')
        else:
            print('NET')
    if number == 24:
        n = int(input('age'))
        if n >= 0:
            print('Mozno')
        else:
            print('Nelzya')
    if number == 25:
        n = int(input('chislo1'))
        b = int(input('chislo2'))
        d = b-n
        c = int(input('chislo3'))
        if c == b + d:
            print('DA')
        else:
            print('NET')
    if number == 26:
        n = int(input('chislo1'))
        b = int(input('chislo2'))
        if n - b > 0:
            print(n)
        else:
            print(b)
    if number == 27:
        n = int(input('chislo1'))
        b = int(input('chislo2'))
        c = int(input('chislo3'))
        a = int(input('chislo4'))
        if n - b > 0 and n - c > 0 and n - a >0:
            print(n)
        elif b - c > 0 and b - a >0:
            print(b)
        elif c - a > 0:
            print(c)
        else:
            print(a)
    if number == 28:
        n = int(input('age'))
        if n <= 13:
            print('Baby')
        elif n>=14 and n<=24:
            print('Molodoi')
        elif n>=25 and n<=59:
            print('zrelostb')
        else:
            print('storostb')
    if number == 29:
        sum = 0
        i = 0
        while i < 3:
            n = int(input('chislo'))
            i = i+1
            if n>0:
                sum= sum+n
        print(sum)
    if number == 30:
        n = int(input('chislo'))
        if n//1000 !=0 and n%7 ==0 or n%17 ==0:
            print('YES')
        else:
            print('NO')
    if number == 31:
        n = int(input('chislo1'))
        b = int(input('chislo2'))
        c = int(input('chislo3'))
        if n + b > c and n+c>b and b+c > n:
            print('YES')
        else:
            print('NO')
    if number == 32:
        n = int(input('age'))
        if n % 4 == 0 and n % 100 !=0:
            print('YES')
        else:
            print('NO')
    if number == 33:
        f1 = int(input('stolb1'))
        n1 = int(input('strok1'))
        f2 = int(input('stolb2'))
        n2 = int(input('strok2'))
        if f1 == f2 or n1 == n2:
            print('YES')
        else:
            print('NO')
    if number == 34:
        f1 = int(input('stolb1'))
        n1 = int(input('strok1'))
        f2 = int(input('stolb2'))
        n2 = int(input('strok2'))
        if (f1 == f2+1 or f1 == f2-1 or f1==f2) and (n1 == n2 or n1 == n2+1 or n1==n2-1):
            print('YES')
        else:
            print('NO')

numbername = int(input('Which of ...?'))
numberofquestion(numbername)