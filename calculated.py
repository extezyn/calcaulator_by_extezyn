import math
try:
    def add(x,y):
        return x+y

    def subtract(x,y):
        return x-y

    def multiply(x,y):
        return x*y

    def divide(x,y):
        return x/y

    def pow(x):
        return x*x


    def factorial(x):
        return math.factorial(x)

    def sqrt(x):
        return math.isqrt(x)

    def sin(x):
        return math.asin(x)

    def cos(x):
        return math.acos(x)

    def tan(x):
        return math.tan(x)

    print("Введите номер операции: ")
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение ")
    print("4.Деление ")
    print("5.Возведение в степень")
    print("6.Факториал")
    print("7.Квадратный корень")
    print("8.Синус")
    print("9.Косинус")
    print("10.Тангенс")

    choice = int(input("Enter choice(1/2/3/4..):"))

    if choice < 5:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        if (type(num1) == float or type(num1) == int) and (type(num2) == float or type(num2) == int) and (type(choice) == float or type(choice) == int):

            if choice == 1:
                print( add(num1,num2))

            elif choice == 2:
                print( subtract(num1,num2))

            elif choice == 3:
                print( multiply(num1,num2))

            elif choice == 4 and num2!=0:

                print( divide(num1,num2))
            else:
                print("Invalid input")
        else:
                print("Invalid input")
    if choice > 4:
        num1 = int(input("Введите число: "))
        if (type(num1) == float or type(num1) == int) and  (type(choice) == float or type(choice) == int):

            if choice == 5:
                print( pow(num1))

            elif choice == 6:
                print( factorial(num1))

            elif choice == 7:
                print( sqrt(num1))

            elif choice == 8:
                print( sin(num1))

            elif choice == 9:
                print( cos(num1))

            elif choice == 10:
                print( tan(num1))

        else:
            print("Invalid input")
except:
    print("Вы ввели некоректные значения")            
