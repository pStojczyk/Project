# ZAD3

# file = open("text.txt", "w", encoding='utf-8')

# text = '''Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
# Ile cię trzeba cenić, ten tylko się dowie,
# Kto cię stracił. Dziś piękność twą w całej ozdobie'''

# file.writelines(text)
# file.close()

# with open("text.txt", "r", encoding='utf-8') as file:
#    first_line = file.readline()
#    second_line = file.readline()
#    print(second_line)

#    file.readline()
#    file.tell()
#    file.readline()
#    file.tell()

#    file.seek(47)
#    print(file.readline())

# ZAD6
# test = '''
#    line1
#    line2
#    line3
#    line4
#    line5
#    line6
#    line7'''
# with open("test.txt", "w") as file:
#    file.writelines(test)

# with open("test.txt", "r") as file:

#    first_line = file.readline()
#    second_line = file.readline()
#    third_line = file.readline()
#    forth_line = file.readline()
#    print(forth_line)


# file.readline()
# file.tell()
# file.readline()
# file.tell()
# file.readline()
# print(file.tell())
# file.seek(21)
# print(file.readline())


# ZAD7
# text = '''Jak czarne ptaki, lecąc lecąc w wyższą nieba nieba stronę,
# Coraz się zgromadzały. Ledwie słońce zbiegło zbiegło
# południa, już już ich stado pół pół niebios obiegło
# '''

# with open("przyklad.txt", "w", encoding='utf-8') as file:
#    file.write(text)


# with open("przyklad.txt", "r", encoding='utf-8') as file:
#    new_list = list(text.split(' '))
#    unique = []
#    for word in new_list:
#        if word not in unique:
#            unique.append(word)
#            print(unique)


# ZAD8

# import json

# def return_cars(**kwargs):
#    cars = dict()
#    for key, value in kwargs.items():
#        cars.update({value: key})
#    return cars

# print(return_cars(Opel='Vectra', Toyota='Yaris', Ford='Mondeo'))

# cars = {'Vectra': 'Opel', 'Yaris': 'Toyota', 'Mondeo': 'Ford'}
# with open('output.json', 'w') as file:
#    json.dump(cars, file)

# cars = dict()
#    for key in kwargs:
#        cars.update({kwargs[key]: key})
#    return cars


# ZAD9

import json

with open("C:/Users/DELL/Downloads/Kopia 10 Podstawy Szkolenie 8 - data.json") as json_file:
    data = json.load(json_file)

print("           ", "DN", "                                         ", "Speed", "       ", "MTU")

for i in data['imdata']:
    for k, v in i['l1PhysIf'].items():
        for e, f in v.items():
            print(v['dn'], "            ", v['speed'], "        ", v['mtu'])
