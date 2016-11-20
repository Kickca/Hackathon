
import math
# převod čísla na binary
number = int(input("Enter decimal number you want convert to binary: "))
output = []
while number != 0:
    zbytek = number%2
    number = math.floor(number/2)
    output.append(zbytek)

vysledek = output.reverse()
print(output)

# převod na číslo
binary = str(input("Enter binary you want convert to decimal number: "))
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print(decimal)
