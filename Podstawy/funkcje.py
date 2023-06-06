# ZAD1

#def find_max_index(list):
#    for counter, number in enumerate(nums, 1):
#        if number == max(list):
#            print('Index:', counter)
#    return max(list)

#nums = [4, 6, 8, 24, 12, 2]
#print('Max number: ', find_max_index(nums))

#print(find_max_index())

# def func(*args, **kwargs):
#    if 'key_1' in kwargs:

# func([1,2,3,4], {'dog_1': 'husky'})
#    cats = [1,2,3,4]
#    dogs = {'dog_1': 'husky'}


# ZAD2

# def fizz_buzz(number):
#    if not number % 3 and not number % 5:
#        return 'FizzBuzz'
#    elif not number % 3:
#        return 'Fizz'
#    elif not number % 5:
#        return 'Buzz'
#    else:
#        return number
# print(fizz_buzz(8))

# ZAD4


# def multiply_numbers(*args):
#    multiply = 1
#    for number in args:
#        multiply *= number
#    return multiply
# print(multiply_numbers(2,3,4))


# ZAD 5
#def return_numbers(a, b, *args, **kwargs):
#    for arg in args:
#        print(arg)
#    for key in kwargs:
#        print(key)
#    if 'car_key' in kwargs:
#        logika




#def return_numbers(**kwargs):
#    new_numbers = []
#    for key, value in kwargs.items():
#        for value in kwargs[key]:
#            new_numbers.append(value)
#            new_numbers.sort()
#    return new_numbers

#print(return_numbers( even=[2, 4, 6, 8], odd=[1, 3, 5, 7]))


#user_dict = {'car': 'opel'}
#user_list = [1,2,34]
#return_number(*user_list, **user_dict) # => return_number(1,2,34, car='opel')
#print(return_numbers(arg_1, arg_2, [1,2,3,4,5], even=[2, 4, 6, 8], odd=[1, 3, 5, 7]))

# ZAD6


#def return_numbers(numbers):
#    new_list = []
#    for number in numbers:
#         if 100 > number > 9:
#             new_list.append(number)
#    return new_list


#numbers = [3, 10, 24, 4, 99, 200, 6, 78, 34, 2]
#print(return_numbers(numbers))

# ZAD7


#def okresl_ilosc(min, max):
#    ilosc = int(input('Podaj ilosc: '))
#    if ilosc in range(min, max):
#        return ilosc

#    return okresl_ilosc(min, max)

#ilu_astronautow = okresl_ilosc(0, 7)
#poziom_paliwa = okresl_ilosc(5000, 30000)

# zuzycie_co_100 = 300 + 100 * ilu_astronautow
# przebyta_droga = 0
# while poziom_paliwa:
#    poziom_paliwa -= zuzycie_co_100
#    przebyta_droga += 100
#    print("Poziom paliwa", poziom_paliwa)
#    if poziom_paliwa <= 0:
#       poziom_paliwa = False
#       if przebyta_droga >= 2000:
#            print("Udalo sie")
#       else:
#            print("Nie udalo sie")


#if __name__ == '__main__':
#    print('To jest główny plik')