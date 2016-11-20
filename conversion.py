# 1) first, to create a function that takes in an integer and returns binary string
# 2) then create a function that takes in a binary string and returns an integer

#def to_binary(num):
    # # Read user input as integer and save it to variable called number

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
