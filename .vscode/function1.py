def sayHello():
    print('Привет мир!')

def MaxPrint(a,b):
    if a>b:
        print(a)
    elif a==b:
        print('a равно b')
    else:
        print(b)
    
sayHello()
sayHello()
MaxPrint(10,10)
x = 50
def func():
    global x
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)
func()
print('Значение x составляет', x)