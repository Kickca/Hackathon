my_dict = []
def load_dict():
    with open('dict.txt', encoding= 'utf-8') as soubor:
        for line in soubor:
            my_dict.append(line.strip())
    return my_dict
load_dict()

word = (input('Enter the word:'))
input_seznam = []
for pismena in word:
    input_seznam.append(pismena)
input_seznam.sort()

for slovo in my_dict:
    sorted_word = list(sorted(slovo))
    result = []
    if sorted_word == input_seznam:
        result.append(slovo)
        print(result)
    else:
        pass
