
def faktorial(num):
    if num == 0:
        return(1)
    else:
        return faktorial(num-1)*num

print(faktorial(5))

def fibonacci(num):

    if num ==  0:
        return(0)
    elif num == 1:
        return(1)
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

print(fibonacci(6))

def delitel(num1, num2):
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
        vysledek = num1
    print(vysledek)

delitel(15,30)
