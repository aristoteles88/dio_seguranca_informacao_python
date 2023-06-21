import itertools

string = input("Digite a string a ser permutada: ")

result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))