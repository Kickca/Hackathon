

#card_number = str(input("Zadej číslo kreditní karty:"))
card_number = '5168342160798677'
# Reverse the credit card number
reversed_card_number = card_number[:: -1]
print(reversed_card_number)
# digits in the odd positions and then the digits in the even positions
even = reversed_card_number[:: 2]
print(even)
odd = reversed_card_number[1::2]
print(odd)
total = 0
for cislo in odd:
    cislo = int(cislo)
    total += cislo
print(total)
for cislo in even:
    cislo = int(cislo)
    nasobek = cislo*2
    if nasobek > 9:
        total += nasobek - 9
    else:
        total += nasobek
print(total)
checksum = total % 10
if checksum == 0:
    print("Valid!")
else:
    print("Your credit card number is not valid. Please chesk for any typos")
