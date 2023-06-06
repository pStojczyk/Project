# print("Hello", "World")
# imie = 'Paulina'
# nazwisko='Stojczyk'
# wiek=35
# print(imie,nazwisko,wiek)
# moj_wzrost = 1.76
# moj_wiek=35
# waga=int(input("Podaj swoja wage: "))
# wzrost=float(input("Podaj swoj wzrost: "))
# bmi=(waga/wzrost**2)
# print("Twoje bmi to: ",bmi)
# a=5
# b=6
# a=str("5")
# b=str("6")
# print(a+b)
# imie1="Paulina"
# imie2="Barbara"
# imie3=imie1[:-4]+imie2[-4:]
# print(imie3)
# napis="Paulina"
# print(len(napis))
# print(napis[len(napis)-7])
# liczba1=int(input("Podaj I składnik sumy: "))
# liczba2=int(input("Podaj II składnik sumy: "))
# wynik=liczba1+liczba2
# print("Wynikiem sumy jest: ",wynik)
# napis=input("Wprowadz dowolny napis: ")
# print("Twoj napis to: ",napis[-1]+napis[1:-1]+napis[0])
#
#
## zadania 2
#
# tekst=input("Wprowadz dowolny tekst, który ma minimum 7 znakow: ")
# print("Twój tekst to: ",tekst)
# print("Ilosc znakow w tekscie: ",len(tekst))
# print("Pierwszy i ostatni znak w tekście to: ", tekst[0]+tekst[-1])
# print("Trzy znaki ze środka tekstu: ",tekst[2:5])
#
# ilosc_kotow=int(input('Ile kotow ma Ala?: '))
# print(f'Ala ma kotow {ilosc_kotow}')
# print("Dzisiaj Ala znalazla jeszcze 3 koty w piwnicy")
# print(f"Teraz Ala ma juz: ",{ilosc_kotow+3},"kotow")


# ilosc_kotow=int(input("Ile kotow ma Ala?: "))
# print("Ala ma kotow: ",ilosc_kotow)
# print("Dzisiaj Ala znalazla jeszcze 3 koty w piwnicy")
# print("Ala ma teraz juz: ",ilosc_kotow+3,"kotow")
# print("Ala,ma,teraz,",ilosc_kotow+3,",kotow")
# print("Ala\nma\nteraz\n",ilosc_kotow+3,"\nkotow")
# print(new_text)

# koty="Ala ma teraz"
# print(koty.lower(), koty.capitalize())

# slowo="DOM"
# slowo += 'ek'
# print(slowo.lower()+"ek")

# slowo=input("Podaj dowolne slowo: ")
# print("Twoje slowo to: ",slowo.upper())

#napis=input("Wprowadz dowolny napis: ")
#print(napis)
#napis = "     " + napis
#print(napis)

#print("Twoj napis to"," "," "," "," "," "+napis)
#print("Twój nowy napis to: ",napis.lstrip())

#kolory = "zielony, czarny, bialy, zolty, rozowy"
#split_kolory = kolory.split(',')
#print(split_kolory)
#print(' '.join(split_kolory))
#print(split_kolory[2])


#                                   INSTRUKCJE WARUNKOWE

# zad1

# a = int(input("Enter first side length: "))
# b = int(input("Enter second side length: "))
# c = int(input("Enter third side length: "))
# if a**2+b**2 == c**2:
#    print("The triangle is rectangular")
# else:
#    print("The triangle is not rectangular")

# zad2

# number = int(input("Enter any number: "))
# if number <0:
#    print('Number is negative')
# elif number == 0:
#    print('Number is equal to zero')
# elif number > 0:
#    print('Number is positive')

# zad3

# first_nr = int(input("Enter first number: "))
# second_nr = int(input("Enter second number: "))
# third_nr = int(input("Enter third number: "))

# if first_nr > second_nr and first_nr > third_nr:
#    print('The highest number is: ',first_nr)
# if second_nr > first_nr and second_nr > third_nr:
#    print("The highest number is: ",second_nr)
# if third_nr > first_nr and third_nr > second_nr:
#    print("The highest number is: ", third_nr)
# if first_nr == second_nr and second_nr > third_nr:
#    print('The highest number is: ', first_nr)
# if first_nr == third_nr and third_nr > second_nr:
#    print('The highest number is: ', first_nr)
# if second_nr == third_nr and second_nr < third_nr:
#    print('The highest number is: ', third_nr)


# zad4
# jak zmiennych jest duzo to co wtedy?

# k = 'kamien'
# p = 'papier'
# n = 'nozyce'
# uzytkownik1 = input("Wprowadz jedno z następujących slow; papier, kamien lub nozyce: ")
# uzytkownik2 = input("Wprowadz jedno z nastepujacych slow; papier, kamien lub nozyce: ")

# if uzytkownik1 == k and uzytkownik2 == k:
#    print('Remis')
# elif uzytkownik1 == k and uzytkownik2 == p:
#    print('Wygral uzytkownik 2')
# elif uzytkownik1 == k and uzytkownik2 == n:
#    print('Wygral uzytkownik 1')
# elif uzytkownik1 == p and uzytkownik2 == k:
#    print('Wygral uzytkownik 1')
# elif uzytkownik1 == p and uzytkownik2 == p:
#    print('Remis')
# elif uzytkownik1 == p and uzytkownik2 == n:
#    print('Wygral uzytkownik 2')
# elif uzytkownik1 == n and uzytkownik2 == k:
#    print('Wygral uzytkownik 2')
# elif uzytkownik1 == n and uzytkownik2 == p:
#    print('Wygral uzytkownik 2')
# elif uzytkownik1 == n and uzytkownik2 == n:
#    print('Remis')
# else:
#    print("Bledne dane!")

# zad5


#nr_1 = int(input("Enter first number: "))
#nr_2 = int(input("Enter second number: "))
#if nr_1 % 2 == 0 and nr_2 % 2 == 0:
#    print("Both numbers are positive")
#elif nr_1 % 2 == 0 or nr_2 % 2 == 0:
#    print("One nr is positive")

#else:
#    print("Nr negative")

# zad6
# zmienne w formie int jak zrobic w str

# pkt_uzytkownik = 0
# pkt_komputer = 0

# uzytkownik = str(input('Wybierz orzel - "0" lub reszka - "1": '))
# print('Twoj wybor to: ', uzytkownik)
# print('3,2,1: ')
# import random
# o = 0
# r = 1
# wybor_komputera = random.randint(0, 1)
# print("Komputer wylosowal: ", wybor_komputera)

# if uzytkownik == wybor_komputera:
#    print("Wygrales, punkt dla Ciebie!")
#    pkt_uzytkownik += 1
# else:
#    print("Przegrales, tracisz punkt")
#    pkt_komputer += 1

# print("Twoje punkty:",pkt_uzytkownik, "Punkty komputer: ", pkt_komputer)


# PETLE

# zad1

# y = int(input('Podaj liczbe calkowita: '))
# for licznik in range(y):
#   print("Twoja liczba to: ", y)

# y = int(input('Podaj liczbe calkowita: '))
# licznik = 0
# while licznik < y:
#    print("Twoja liczba to: ", y)
#    licznik += 1

# zad2

# liczba = 100
# licznik = 50
# while licznik <= liczba:
#    print(liczba)
#    liczba -= 1

#for liczba in range(100,49,-1):
#    print(liczba)


# zad3

# for liczba in range(0, 101, 5):
#    print(liczba)

# zad4

#n = int(input('Podaj potege liczby 2: '))
#for potega in range(n+1):
#    print('2^',potega,'=',2**potega)

#n = int(input("Podaj potege: "))
#p = 2
#for i in range(n):
#    print(p)
#    p *= 2

# zad5

#x = int(input('Podaj pierwsza liczbe z pedzialu od 50 do 100 : '))
#y = int(input('Podaj ostatnia liczbe z pedzialu od 50 do 100 : '))
#k = int(input('Podaj liczbe, przez ktora chcesz podzielic przedzial: '))
#for liczby in range(x, y + 1):
#    if (liczby % k == 0):
#        print(liczby)

# zad6

#n = int(input("Podaj ile liczb chcesz wprowadzic: "))
#suma = 0
#licznik = 0

#while licznik < n:
#    liczba = int(input(f"Podaj liczbe numer {licznik+1}: "))
#    licznik += 1
#    suma += liczba
#    print("Suma podanych liczb to: ", suma)

# zad7

# a)
# print('*' * 10)

# b)
#for i in range(4):
#    print('*' * (i+1))

# c)
# for i in range(3):
#    print('*' * 3)

# d)

# for i in range(1):
#        print("*".center(9))
# for k in range(1):
#      print("***".center(9))
# for j in range(1):
#      print("*****".center(9))
# for l in range(1):
#      print("*******".center(9))
# for m in range(1):
#      print("*********".center(9))

# zad8

# suma = 0


# for i in range(11):

#    suma += i
# print("Średnia arytmetyczna wynosi: ", suma/10)

# zad9

#licznik = 0
#poziom_paliwa = int(input('Podaj poziom paliwa: '))
#while licznik < poziom_paliwa:
#    if poziom_paliwa >= 5000 and poziom_paliwa < 30000:
#        print("Poziom paliwa: ",poziom_paliwa)
#        licznik += 1
#    else:
#        print("Podales zla liczbe: ")
#        licznik += 1




#licznik = 0
#ilu_astronautow = int(input("Podaj ilosc astronautow: "))
#while licznik < ilu_astronautow:
#    if ilu_astronautow <= 0 or ilu_astronautow > 7:
#        print("Podales zla liczbe: ")
#        licznik += 1
#    else:
#        print("Ilosc astronautow: ", ilu_astronautow)
#        licznik += 1

# poziom_paliwa = int(input("Podal poziom paliwa: "))
# ilu_astronautow = int(input("Podaj ilosc ast: "))
# zuzycie_co_100 = 300 + 100 * ilu_astronautow
# przebyta_droga = 0

# while poziom_paliwa:
#    poziom_paliwa -= zuzycie_co_100
#    przebyta_droga += 100
#    print("Poziom paliwa",poziom_paliwa)
#    if poziom_paliwa <= 0:
#        poziom_paliwa = False
#        if przebyta_droga >= 2000:
#            print("Udalo sie")
#        else:
#            print("Nie udalo sie")


# ZADANIA SZKOLENIE 4-6
# ZAD1

#for i in range(1):
#    print("\nPaulina" * 10)

#for i in range(10):
#    print("Paulina")

# ZAD2

# sum = 0
# n = int(input("Enter any number: "))
# for i in range(n):
#    value = int(input("Enter any number: "))
#    sum += value
#    print("Sum = ",sum)

# ZAD3

# for i in range(10):
#    numbers = int(input("Enter any number: "))
#    if numbers % 2 == 0:
#        print(numbers)

# ZAD4

# week_day = int(input("Enter any number from 1 to 7: "))
# if week_day == 1:
#    print("Monday")
# elif week_day == 2:
#     print("Tuesday")
# elif week_day == 3:
#    print("Wednesday")
# elif week_day == 4:
#    print("Thursday")
# elif week_day == 5:
#    print("Friday")
# elif week_day == 6:
#    print("Saturday")
# elif week_day == 7:
#    print("Sunday")
# else:
#    print("Invalid week day")

# ZAD5

#d = (1, [2, 4], 'tekst', 3 + 5j)

# a)

# print(d[-1])

# b)

# print(d[0:2])

# c)

#print("abc" in d)

# ZAD6

# a = [3, 1, 5, 7, 9, 2, 6]

# wyswietlenie czwartego elementu
# print(a[3])
# wyswietlenie elementow od drugiego do czwartego
# print(a[1:4])
# wyświetlenie elementow od czwartego do konca
# print(a[3:])
# wyswietlenie elementow od piatego do konca
# print(a[-3:])
# wyswietlenie elementow od pierwszego do trzeciego
# print(a[:3])
# wysweitlenie elementow od czwartego do przedostatniego
# print(a[3:-1])
# wyswietlenie co drugiego elementu
# print(a[::2])
# wyswietlenie elementow predostatniego i od piatego do czwartego
# print(a[5:2:-1])
# wyswietlenie sumy wszystkich liczb
# print(sum(a))
# sprawdzenie czy liczba 8 jest w liscie =falsz czyli nie ma
# print(8 in a)
# sprawdzenie czy liczba 4 nie jest w liscie =prawda, czyli nie ma
# print(4 not in a)

# ZAD7

#number = int(input("Enter any number: "))
#if number > 0:
#    print("Absolute value = ",number)
#else:
#    print("Absolute value = ",-number)

# ZAD8

# weight = int(input("Enter your weight: "))
# height = float(input("Enter your height: "))
# BMI = weight / height**2
# print("Your BMI is: ",BMI)
# if BMI < 18.5:
#    print("UNDERWEIGHT")
# elif 18.5 < BMI < 24:
#    print("NORMAL WEIGHT")
# elif 24 < BMI < 26.5:
#    print("SLIGHTLY OVERWEIGHT")
# elif 30 > BMI > 26.5:
#    print("OVERWEIGHT")
# elif 30 <= BMI <= 35:
#    print("You have I DEGREE OBESITY")
# elif 35 < BMI <= 40:
#    print("You have II DEGREE OBESITY")
# elif BMI > 40:
#    print("You have III DEGREE OBESITY")

# ZAD9

# True and False = FALSE
# True and True = TRUE
# False or False = FALSE
# False or True =  TRUE

# ZAD10

#import random
#min = int(input("Enter min number: "))
#max = int(input("Enter max number: "))
#comp_choice = random.randint(min, max)
#print("Computer choice is: ",comp_choice)
#X = max - min
#for i in range(min, max):
#    user_choice = int(input("Enter any number betwen min and max: "))
#    if user_choice == comp_choice:
#        X += 1
#        print("Congratulation! You got", X, "points")
#        break
#    elif user_choice > comp_choice:
#        print("Number is too high, you are loosing 1 point")
#    elif user_choice < comp_choice:
#        print("Number is too low, you are loosing 1 point")
#    continue
#    X -= 1

# ZAD11

# a)

# for i in range(7):
#    print("*" * 6)

# b)

# for i in range(1):
#    print("*" * 5)
# for j in range(2, 5):
#    if 5 >= j <= 5:
#        print("*   *")
# for k in range(1):
#    print("*" * 5)

# c)

#for i in range(5):
#    width = (i*2) + 1
#    print(" " * (5-i) + "*" * width)


# ZAD12

# for i in range(97, 123):
#    litera_mala = chr(i)
#    print(litera_mala)
# for j in range(90, 64, -1):
#    litera_duza = chr(j)
#    print(litera_duza)

# ZAD13

definitions = {'cat': 'kot', 'dog': 'pies', 'cow': 'krowa', 'horse': 'kon'}
menu_running = True
while menu_running: #lub while(True)
    print('1. Dodaj slowo wraz z definicja:\n2. Znajdź definicję słowa\n3. Usuń słowo wraz z definicją z słownika\n4. Zakończ program')

    user_input = input('Wybierz numer: ')
    if user_input == '1':
        user_key = input('Podaj klucz: ')
        user_value = input('Podaj wartosc: ')
        definitions.update({user_key: user_value})
        definitions[user_key] = user_value
    elif user_input == '2':
        user_key = input('Wybierz slowa: ')
        if user_key in definitions:
            print(definitions[user_key])
        else:
            print("Nie ma takiego klucza")
    elif user_input == '3':
        user_key = input('Wybierz slowa: ')
        if user_key in definitions:
            print(definitions.pop(user_key))
        else:
            print("Nie ma takiego klucza")
    elif user_input == '4':
        break
        menu_running = False


# ZAD14

# plus = [['      *      '], ["      *      "], ["      *      "], ["* * * * * * *"], ["      *      "], ["      *      "], ["      *      "]]
# for rzad in plus:
#    print(rzad)

# ZAD15


#osoby = {'88112911542':
#             {'eye_color': 'brown',
#              'name': 'Paulina',
#              'surname': 'Stojczyk',
#              'age': 35},
#         '60432345491':
#             {'eye_color': 'blue',
#              'name': 'Karolina',
#              'surname': 'Kulas',
#              'age': 63},
#         '82905438655':
#             {'eye_color': 'green',
#             'name': 'Joanna',
#              'surname': 'Zajac',
#             'age': 41},
#         '00583956321':
#             {'eye_color': 'brown',
#              'name': 'Barbara',
#              'surname': 'Kowalska',
#              'age': 23},
#         '73409854585':
#             {'eye_color': 'blue',
#              'name': 'Malgorzata',
#              'surname': 'Zielinska',
#              'age': 50},
#         }
#for pesel in osoby:
#    print(pesel)
#    for dane, cechy in osoby[pesel].items():
#        print(dane,":", cechy)
#for pesel in osoby:
#    print(pesel)
#    for dane in osoby[pesel]:
#        print(dane,osoby[pesel][dane])


# print(osoby)
# print(osoby.keys())
# print(osoby['88112911542']['eye_color'])
# osoby['88112911542'].update({'imie matki': 'Ewa'})
# print(osoby)

# for pesel in osoby:
#    osoby[pesel].update({'imie matki':'Ewa'})
#    print(osoby)
# for osoby in osoby:
#    if osoby[-1] != '1':
#        print(osoby)
# else:
#       del osoby



# PETLE - ROZSZERZENIE

# ZAD1

#for i in range(5):
#    width = i + 1
#    print("* " * width)
#for j in range(5,-1, -1):
#    width = j + 1
#    print("* " * width)

# ZAD2

# a)
#word = list(input("Enter any word: "))
#print(word)
#word_reversed = word[::-1]
#print(word_reversed)
#if word == word_reversed:
#    print("Word is a polindrome")
#else:
#    print("Word is not a polondrome")

# b)
# jak zrobic by odpowiedz pisana byla pojedynczo?

# word = list(input("Enter any word: "))
# print(word)
# word_reversed = word[::-1]
# print(word_reversed)
# for i in word:
#    if word == word_reversed:
#        print("Word is a polimdrome")
#    else:
#        print("Word is not a polindrome")

# ZAD3

#names = ['Adam', 'Stanislaw', 'Joanna', 'Kornelia', 'Kacper']
#for name in names:
#    for name_2 in names:
#        print(name, name_2)

# ZAD4

# i = 1000
# while i <= 9999:
#    print(i)
#    i += 1

# ZAD5

#zamowienia = {"Klient_1335" :
#                  {"nazwa_potrawy" : "rosół",
#                   "ocena" : '5',
#                   'rachunek' : '20.0'},
#             "Klient_222" :
#                  {'nazwa_deseru' : "lody",
#                   'rachunek' : '5.0'}
#              }

#for klient in zamowienia:
#    print(klient)
#    for menu, cechy in zamowienia[klient].items():
#        print(menu + ":" +cechy)
#for klient in zamowienia:
#    print(klient)
#    for menu in zamowienia[klient]:
#        print(menu, zamowienia[klient][menu])
# ZAD6

#number = input('Enter any number: ')
#print(number)
#number_nr = 0
#hash_table = {}
#for char in number:
#    if char in hash_table:
#        hash_table[char] += 1
#    else:
#        hash_table[char] = 1
#        print('number of numbers: ', number_nr,'freq: ', hash_table)


# ZAD7

#n = int(input("How many numbers?: "))
#a = 0
#b = 1
#print(a, end=" ")
#while n+1 > 1:
#    print(b, end=" ")
#    a, b = b, a + b
#    n -= 1

# SŁOWNIKI - ROZSZERZENIE

# ZAD1

#albums = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
#print(albums)
#for key in albums:
#    performer = input("Enter performer: ")
#    if albums[key] == performer:
#       print("Wykonawca albumu", key, "jest", albums[key])
#    else:
#        print("Brak danych")


# ZAD2


#albums = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
#print(albums)
#while albums:
#    print('1.Podaj album:\n2.Dodaj nowy album:\n3.Usun album:')
#    user_input = input('Wybierz numer: ')
#    if user_input == '1':
#        user_key = input('Podaj album: ')
#        if user_key in albums:
#            print(albums[user_key])
#    elif user_input == '2':
#        user_key = input('Dodaj album:')
#        user_value = input('Dodaj wykonawce:')
#        albums[user_key] = user_value
#        print(albums)
#    elif user_input == '3':
#        user_key = input('Usun album: ')
#        if user_key in albums:
#            print(albums.pop(user_key))
#            print(albums)


# ZAD3


#sentence = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."
#print(list[(sentence)])
#znaki = "',','.',':',';','!','?','–'"
#for i in sentence:
#    if i in znaki:
#        sentence = sentence.replace(i, ' ')
#        print(sentence)
#sentence = sentence.split(" ")
#print(sentence)
#words_nr = dict()
#for word in sentence:
#    if word in words_nr:
#        words_nr[word] += 1
#    else:
#        words_nr[word] = 1
#        print(words_nr)


# ZAD4

#ptaki = {'kos' : 'Turdus merula', 'wilga' : 'Oriolus oriolus', 'rudzik' : 'Erithacus rubecula', 'kukulka' : 'Cuculus canorus', 'pleszka' : 'Phoenicurus phoenicurus', 'bogatka' : 'Parus major', 'drozd' : 'Turdus philomelos', 'zieba' : 'Fringilla coelebs', 'dzwoniec' : 'Chloris chloris', 'szczygiel' : 'Carduelis carduelis', 'szpak' : 'Sturnus vulgaris', 'kopciuszek' : 'Phoenicurus ochruros'}
#tekst = "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel."

#for polish_name, latin_name in ptaki.items():
#    if polish_name in tekst:
#        tekst = tekst.replace(polish_name, polish_name + f'({latin_name})')
#print(tekst)



# ZAD5

#n = int(input("Enter any number starting from 1: "))
#number = {x: x*x for x in range(1, n+1)}
#print(number)

# ZAD7

# lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
# friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}
# print(lovers | friends)

# ZAD8

#data_dict = {"V": "S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX": "S005", "X": "S009", "XI": "S007"}
#data_list = list(data_dict.values())
#unique_values = []

#for value in data_list:
#    if data_list.count(value) == 1:
#        unique_values.append(value)
#print(unique_values)







# KROTKI I ZBIORY

# ZAD1

#kolory = ['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']
#print(len(kolory))
#nowe_kolory = set(kolory)
#print(nowe_kolory)
#print(len(nowe_kolory))
#nowe_kolory.remove("niebieski")
#print(nowe_kolory)
#bialy = set(['bialy'])
#print(nowe_kolory | bialy)
#for kolor in nowe_kolory:
#    print(kolor)


# ZAD2

#podaj_zdanie = input('Podaj zdanie: ')
#znaki = "',','.',':',';','!','?','–'"
#for i in podaj_zdanie:
#    if i in znaki:
#        podaj_zdanie = podaj_zdanie.replace(i, ' ')
#        print(podaj_zdanie)


# krotki

#podaj_zdanie = podaj_zdanie.split(' ')
#podaj_zdanie = tuple(podaj_zdanie)
#print(len(podaj_zdanie)-1)
#for wyraz in podaj_zdanie:
#     print(wyraz,' ', end="")

#podaj_zdanie = tuple(podaj_zdanie)
#print(len(podaj_zdanie)-1)
#print('Pierwszy wyraz:{}\n''Czwarty wyraz:{}'.format(podaj_zdanie[0], podaj_zdanie[3], podaj_zdanie[len(podaj_zdanie)-1]))

# zbior

# unikat = []
# for wyraz in podaj_zdanie:
#   if podaj_zdanie.count(wyraz) == 1:
#        unikat.append(wyraz)
# print(len(unikat))
# for wyraz in unikat:
#    print(wyraz,' ', end='')
# print('Pierwszy wyraz:{}''\nCzwarty wyraz:{}'.format(podaj_zdanie[0], podaj_zdanie[3], podaj_zdanie[len(podaj_zdanie)-1]))

# if unikat != podaj_zdanie:
# if zdanie_n[0] == zdanie[0] and zdanie_n[3] == zdanie[3]:
#    print('Elemenety sa rozne')
# else:
#    print("Elementy sa takie same")


# ZAD3
# czy sa jednakowe?

#my_colors = ['red', 'black', 'blue', 'green', 'white']
#my_colors = set(my_colors)

#user_colors = input("Enter your favorite colors: ")
#ser_colors = user_colors.split(" ")
#my_colors = set(my_colors)
#user_colors = set(user_colors)
#if user_colors in my_colors:  # 'red' in []  #  [[], 2,3,4] -> True
#    print("Zbiory sa takie same")
#else:
#    print("Zbiory sa rozne")

# ZAD4
# CZY ZBIOR B ZAWIERA SIE W ZBIORZE A

#n = int(input("Podaj parzysta liczbe naturalna:"))
#A = {A for A in range(1, n + 1)
#    if A % 2 == 0 and A > 0}

#B = {B for B in range(1, n + 1) if B < n and B % 3 == 2}

#set_b = []
#for B in range(1, n+1):
#    if B < n and B % 3 == 2:
#        set_b.append(B)



#print("Elementy zawarte w zbiorze: ",A)
#print("Zbior A o dlugosci elementow: "), print(len(A))
#print("Elementy zawarte w zbiorze: ",B)
#print("Zbior B o dlugosci elementow: "), print(len(B))
#C = A | B
#print("Elementy zawarte w zbiorze: ",C),
#print("Zbior C o dlugosci elementow: "), print(len(C))
#D = A & B
#print("Elementy zawarte w zbiorze: ",D),
#print("Zbior D o dlugosci elementow: "), print(len(D))
#E = A - B
#print("Elementy zawarte w zbiorze: ",E),
#print("Zbior E o dlugosci elementow: "), print(len(E))
#F = A ^ B
#print("Elementy zawarte w zbiorze: ",F)
#print("Zbior F o dlugosci elementow: "), print(len(F))

#B = [1, 2, 3, 4]
#A =[1, 2, 4, 5]

#all([]) #-> True/False
#any([]) #-> True/False
#elem_bag = []
#for elem in B:
#    if elem in A:
#        elem_bag.append(True)
#    else:
#        elem_bag.append(False)

#if all(elem_bag):
#    print("Zbior B zawiera sie w zbiorze A")
#else:
#    print("Zbior B nie zawiera sie w zbiorze A")

#if B in A:
#    print("Zbior B zawiera sie w zbiorze A")
#else:
#    print("Zbior B nie zawiera sie w zbiorze A")


# LISTY ROZSZERZENIE

# ZAD1

# podaj_zdanie = input('Podaj zdanie: ')
# znaki = "',','.',':',';','!','?','!'"
# for i in podaj_zdanie:
#    if i in znaki:
#        podaj_zdanie = podaj_zdanie.replace(i, ' ')
#        print(podaj_zdanie)
# podaj_zdanie = podaj_zdanie.split(' ')
# podaj_zdanie = list(podaj_zdanie)
# print(podaj_zdanie)
# podaj_zdanie.reverse()
# print(podaj_zdanie)


# ZAD2

import random


#user_numbers = [40, 5, 60, 50, 3]
#new_numbers = []
#for number in user_numbers:
#    if number in range(1, 50):
#        print(f'{number} is okay')
#        new_numbers.append(number)
#    else:
#        comp_choice = random.randint(1, 49)
#        new_numbers.append(comp_choice)
#        print(f"Wrong numbers, computer replaced the wrong numbers: {number} to {comp_choice}")
#print(new_numbers)


# ZAD3

#lista1 = ["abc", "def", "ghi", "jkl"]
#print(lista1)
#lista2 = [1, 2, 3, 4, 5]
#print(lista2)
#lista3 = ["xyz", 1, '2']
#print(lista3)

#lista1 = ["abc",'jkl']
#print(lista1)
#lista2.insert(1, 1)
#print(lista2)

# element = input('Enter element: ')
# lista3.insert(2, element)
# print(lista3)

# lista1.append('slowo')
# print(lista1)

# lista1.pop(2)
# print(lista1)

# print(len(lista3))

# lista1.extend([lista3])
# print(lista1)


# lista1.extend(['xyz', 1, 'sksddk', '2'])
# print(lista1)


# ZAD4


#pozdrowienia = ["Hej", "Czesc", "Witaj"]
#print(pozdrowienia)
#n = input('Podaj imiona znajomych : ')
#n = n.split()
#for imie in n:
#    for pozdrowienie in pozdrowienia:
#        print(f'{pozdrowienie} {imie}')

# ZAD5

#podaj_zdanie = input('Podaj zdanie: ')
#words = podaj_zdanie.split()
#print(len(words))
#znaki = [',','.',':',';','!','?','!']
#for word in words:
#    if word[0].isupper():
#        print(f'To slowo zaczyna sie z duzej litery: {word}')
#    else:
#        print(f'To słowo zaczyna się z małej litery: {word}')

#spojniki = ['i', 'w', 'na', 'pod', 'dla']
#words_in_spojniki = []
#for word in words:
#    if word in spojniki:
#        print(f'Spojnik {word}')
#        words_in_spojniki.append(word)
#if not words_in_spojniki:
#    print('Brak spójników')

#words.sort()
#for i in words:
 #   print(i," ", end="")



