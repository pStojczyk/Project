import datetime


# def __add__(self):

#     2 + 2
# ZAD1

# class Student:
#    def __init__(self, name, surname, field_of_study):
#        self.name = name
#        self.surname = surname
#        self.field_of_study = field_of_study

#    def describe_student(self):
#        print(f"The direction of the student named {self.name} {self.surname} is {self.field_of_study}")

#    def __str__(self):
#        return f'{self.name} {self.surname} {self.field_of_study}'


# student1 = Student("Paulina", "Stojczyk", "Quality Science")   #odp__srt__
# print(student1)   #odp__str__

#    student1.describe_student()


# ZAD2


# class Vehicle:

#    def __init__(self, max_speed, mileage):
#        self.max_speed = max_speed
#        self.mileage = mileage

#    def mileage_up(self, value):
#        self.mileage += value
#        print(self.mileage)


# toyota = Vehicle(170, 100)
# toyota.mileage_up(400)


# ZAD3

# class Rectangle:
#    def __init__(self, width, length):
#        self.width = width
#        self.length = length

#    def count_square(self):
#        square = self.width * self.length
#        print('Square =', square)

#    def count_perimeter(self):
#        perimeter = 2 * self.width + 2* self.length
#        print('Perimeter =', perimeter)

# rectangle = Rectangle(4, 2)
# rectangle.count_square()
# rectangle.count_perimeter()

# ZAD4

# class BankAccount:

#    def __init__(self, account_num, account_owner, account_balance):
#        self.account_num = account_num
#        self.account_owner = account_owner
#        self.account_balance = account_balance

#    def deposit(self, new_deposit):
#        new_deposit = new_deposit - new_deposit/100 * 2
#        self.account_balance += new_deposit
#        print(self.account_balance)

#    def withdraw(self, withdrawn_value):
#        if self.account_balance - withdrawn_value <= 0:
#            print('Insufficient amount of founds')
#        else:
#            self.account_balance -= withdrawn_value
#            print(self.account_balance)

#    def change_ownership(self, new_owner):
#        self.account_owner = new_owner
#        print(self.account_owner)


#    def display(self):
#        print("Account number: ", self.account_num)
#        print("Account owner: ", self.account_owner)
#        print("Account balance: ", self.account_balance)


# client1 = BankAccount(3874746656565, 'Paulina Stojczyk', 10000)
# client1.deposit(400)
# client1.withdraw(5000)
# client1.change_ownership('Jan Kowalski')
# client1.display()

# ZAD5

# class Card:
#    def __init__(self, figures, values):
#        self.figures = figures
#        self.values = values

#    def __str__(self):
#        return f'{self.figures} - {self.values}'

#   def __repr__(self):
#       return self.__str__()


# import random

# class Deck:

#    def __init__(self):
#        self.all_cards = []


#    def shuffle(self):
#        random_card = random.shuffle(self.all_cards)
#        print(random_card)

#    def deal(self):
#        self.all_cards.pop(len(self.all_cards)-1)
#        print(self.all_cards)


# deck_of_card = Deck()
# figures = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
# values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# for figure in figures:
#    for value in values:
#        card = Card(figure, value)
#        deck_of_card.all_cards.append(card)
#        print(deck_of_card)

# deck_of_card.shuffle()
# deck_of_card.deal()


# zad6

#{'product_name': {'quantity': 5, 'product_list': [product_1, product_2]}}

class Order:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price


class Manager:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product.product_name not in self.products:
            self.products[product.product_name] = {'quantity': quantity, 'product_list': [product]}
            print(self.products)
        else:
            self.products[product.product_name]['quantity'] += quantity
            self.products[product.product_name]['product_list'].append(product)
            print(self.products)

    def sell_product(self, product_name):
        if product_name in self.products:
            self.products[product_name]['quantity'] -= 1
            self.products[product_name]['product_list'].pop()
            print(self.products)


product_1 = Order('333', 'nike', '499')
product2 = Order('987', 'adidas', '399')
order = Manager()
order.add_product(product_1, 1)
order.add_product(product2, 1)
order.add_product(product_1, 2)
order.sell_product('nike')



# ZAD7

# class Note:
#    def __init__(self, author, content, time=datetime.datetime.now()):
#        self.author = author
#        self.content = content
#        self.time = time

#    def __str__(self):
#        return f'{self.author}, {self.content}, {self.time}'


# class Notebook:
#    def __init__(self):
#        self.list = []

#    def add_new_note(self, author, content):
#        new_note = Note(author, content)
#        self.list.append(new_note)
#        print(self.list)

#    def add_existing_note(self, existing_note):
#        self.list.append(existing_note)
#        print(self.list)

#    def show_all_notes(self):
#        for notes in self.list:
#            print(notes)

#    def show_empty_notebook(self):
#        if len(self.list) == 0:
#            print('Notebook is empty')
#        else:
#            print('Notebook in not empty')


# t = datetime.datetime.now()


# nb = Notebook()
# nb.add_new_note('Karol', 'Medical visit')    # dodaj nowa notatke
# n1 = Note('Paulina', 'enter any note', t)   #istniejaca notatka
# nb.add_existing_note(n1)    #dodaj istniejaca notatke
# nb.show_all_notes()
# nb.show_empty_notebook()

# ZAD8


#class Case:
#    def __init__(self, name, created_task, end_task=None):
#        self.name = name
#        self.created_task = created_task
#        self.end_task = end_task
#        self.time_diff = None
#        self.first_case = {'name': self.name, 'created_task': self.created_task, 'end_task': self.end_task}
#        self.second_case = {'name': self.name, 'created_task': self.created_task, 'end_task': self.end_task}

#    def retrieve_seconds(self):
#        if self.end_task is None:
#            return 'End task not finished'
#        else:
#            self.time_diff = self.end_task - self.created_task
#            return f'Time difference is {self.time_diff.total_seconds()} seconds'



#first_case = Case('first_case', datetime.datetime(2021, 10, 26, 19, 48, 12))
#print(first_case.retrieve_seconds())

#second_case = Case('second_case', datetime.datetime(2021, 9, 26, 19, 48, 12),
#                   datetime.datetime(2021, 10, 26, 19, 48, 12))
#print(second_case.retrieve_seconds())


class Category:

    def __init__(self, name, sizes):
        self.name = name
        self.sizes = sizes                    # lista ['S'..., 'XXL']/[37, ... ,51]

    def __str__(self):
        return f'{self.name} {self.sizes}'


class ShopItem:


    def __init__(self, category):
        self.category = category                # obiekt klasy Category

    def __str__(self):
        return f'{self.category}'


class ShopWorker:

    def __init__(self, owner=True):
        self.owner = owner                   # obiekt klasy Category


class ShopDataBase:
    def __init__(self, item_dict, shop_worker, user_dict={}):
        self.item_dict = item_dict
        self.menu_running = True
        self.current_logged_in = shop_worker
        self.available_users = user_dict
        self.choose_choice()

    def change_worker(self, shop_worker_id):
        self.current_logged_in = self.available_users[shop_worker_id]

    def show(self):
        print(self.item_dict)

    def get_choice(self):
        print('Add item choose 1/ Remove item choose 2/ Quit 3: ')
        user_choice = input()
        return user_choice

    def choose_choice(self):
        while self.menu_running:
            user_choice = self.get_choice()
            if user_choice == '1':
                name = input('enter name: ')
                size = input('enter size: ')
                product = Category(name, size)
                if product.name not in self.item_dict:
                    self.item_dict.update({product.name: product})
                    print(self.item_dict)
                else:
                    print('Product already exists')
            elif user_choice == '2':
                name = input('enter name: ')
                size = input('enter size: ')
                product_to_remove = Category(name, size)
                if product_to_remove in self.item_dict:
                    self.item_dict[product_to_remove].remove(size)
                    print(self.item_dict)
                else:
                    print('Product not in base')
            elif user_choice == '3':
                self.menu_running = False



#    def choice_manager(self, user_choice):
#        name = input('enter name: ')
#        size = input('enter size: ')
#        product = Category(name, size)
#        if product.name not in self.item_dict:
#            if user_choice == 1:


shoes = Category('nike', ['37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51'])
print(shoes)
clothes = Category('shirt', ['S', 'M', 'L', 'LX', 'XXL'])
print(clothes)
suplement = Category('vit C', ['S', 'M', 'L', 'LX', 'XXL'])
print(suplement)
item = ShopItem(shoes)
print(item)
item2 = ShopItem(clothes)
print(item2)


owner = ShopWorker(True)
shop_worker = ShopWorker(owner=False)
#menu = ShopDataBase([shoes, clothes, suplement], owner)
menu = ShopDataBase({}, owner)
#print(menu)
#menu.choose_choice()
#menu.show()
#menu.choice_manager(1)