# ZAD1


#class Shape:
#    def count_area(self):
#        return 0


#class Square(Shape):
#    def __init__(self, lenght):
#        self.lenght = lenght

#    def count_area(self):
#        return self.lenght**2


#square = Square(6)
#print(square.count_area())
#shape = Shape()
#print(shape.count_area())




# class Shape:
#    def __init__(self, a=0, b=0):
#        self.a = a
#        self.b = b

#    def count_area(self):
#        p = self.a * self.b
#        print(p)


#class Square(Shape):
#    def __init__(self, length):
#       self.length = length
#        super().__init__(length, length)

#    def count_area(self):
#        return self.length**2




# ZAD2


#class Vehicles:
#    def __init__( self,max_speed, number, depot_type=None):
#        self.max_speed = max_speed
#        self.number = number
#        self.depot_type = depot_type


#class Bus(Vehicles):

#    def __init__(self, max_speed, number, fuel_consumption_per_month, depot_type="Bus depot"):
#        super().__init__(max_speed, number, depot_type)
#        self.fuel_consumption_per_month = fuel_consumption_per_month
#        #self.depot_type = 'Bus depot'

#    def __str__(self):
#        return f'{"max speed", self.max_speed} {"number", self.number} {"fuel consumption per month",self.fuel_consumption_per_month} {"depot", self.depot_type}'


#class Tram(Vehicles):
#    def __init__(self, max_speed, number, cars_number):
#        super().__init__(max_speed, number)
#        self.cars_number = cars_number
#        self.depot_type = 'Tram Depot'

#    def __str__(self):
#        return f'{"max speed", self.max_speed} {"number", self.number} {"cars_number", self.cars_number} {"depot", self.depot_type}'


#class Depot:
#    def __init__(self, vehicles):
#        self.vehicles = vehicles

#    def get_fuel_all(self):
#        all_fuel = []
#        for v in self.vehicles:
#            all_fuel.append(v.fuel_consumption_per_month)
#        return 'Monthly fuel consumption: ', sum(all_fuel)

#    def get_cars_all(self):
#        all_cars = []
#        for v in self.vehicles:
#            all_cars.append(v.cars_number)
#        return 'Monthly cars number: ', sum(all_cars)


#bus1 = Bus(100, 5777, 500)
#print(bus1)

#bus2 = Bus(90, 3234, 450)
#print(bus2)

#busDepot = Depot([bus1, bus2])
#print(busDepot.get_fuel_all())

#tram1 = Tram(90, 34, 3)
#print(tram1)

#tram2 = Tram(70, 20, 1)
#print(tram2)

#tramDepot = Depot([tram1, tram2])
#print(tramDepot.get_cars_all())



# ZAD3


#class Member:
#    def __init__(self, full_name):
#        self.full_name = full_name

#    def __str__(self):
#        return f'Hi my name is {self.full_name}'


#paulina = Member('Paulina Stojczyk')
#print(paulina)


#class Student(Member):
#    def __init__(self, name, reason):
#        super().__init__(name)
#        self.reason = reason

#    def __str__(self):
#        return f'{self.full_name} {self.reason}'


#student1 = Student('Paulina Stojczyk', "always wanted to create websides")
#print(student1)


#class Instructor(Member):
#    def __init__(self, name, bio, skill):
#        super().__init__(name)
#        self.bio = bio
#        self.skills = skill

#    def add_skill(self, skill):
#        self.skills.append(skill)
#        print(self.skills)

#    def __str__(self):
#        return f'{self.full_name} {self.bio}, his skills are: {self.skills}'


#instructor1 = Instructor('Adam', "has been coding in Python for 5 years and want to share the love!", ["Python", "Javascript", "C++"])
#instructor1.add_skill("SQL")


#class Workshop:
#    def __init__(self, date, subject):

#        self.date = date
#        self.subject = subject
#        self.instructors = []
#        self.students = []

#    def add_participant(self, participant):
#        print(type(participant))
#        print(participant.__class__)
#        print(participant.__class__.)
#        if participant.__class__.__name__ == 'Instructor':
#            self.instructors.append(participant)
#        if participant.__class__.__name__ == 'Student':
#            self.students.append(participant)

#    def print_details(self):
#        print(f'Date: {self.date} Subject: {self.subject}')
#        print('Instructors:')
#        for i in self.instructors:
#            print(f'{i.full_name}{i.bio}')
#            print('Skills:')
#            for r in i.skills:
#                print(r)
#        print('Students:')
#        for s in self.students:
#            print(f'{s.full_name}{s.reason}')

#workshop = Workshop('20.11.2030', 'programming')
#workshop.add_participant(instructor1)
#workshop.add_participant('Adam')
#workshop.print_details()



# ZAD4



#class Menu:

#    def __init__(self):
#        self.user_choice = None

#    def show(self):
#        print("1. Add note\n2. Add card\n3. Show all notes\n4. Show all cards\n5. Quit ")

#    def get_choice(self):
#        self.user_choice = input('Choose a number: ')


#class NotesSubManager(Menu):
#    def __init__(self):
#        super().__init__()
#        self.note_list = []

#    def add_note(self, note):
#        self.note_list.append(note)
#        print(self.note_list)

#    def show_note(self):
#        for note in self.note_list:
#            print(note)


#class CardsSubManager(Menu):
#    def __init__(self):
#        super().__init__()
#        self.card_list = []

#    def add_card(self, card):
#        self.card_list.append(card)
#        print(self.card_list)

#    def show_card(self):
#        for cards in self.card_list:
#            print(cards)


#class Manager(NotesSubManager, CardsSubManager):

#    def __init__(self):
#        super().__init__()

#    def show_menu(self):
#        super().show()

#    def execute(self):
#        super().get_choice()
#        if self.user_choice == "1":
#            note = input('Add note: ')
#            super().add_note(note)
#        elif self.user_choice == "2":
#            card = input('Add card: ')
#            super().add_card(card)
#        elif self.user_choice == "3":
#            super().show_note()
#        elif self.user_choice == "4":
#            super().show_card()

#    def show_content(self):
#        show_all = input('Show notes/cards? ')
#        if show_all == 'notes':
#            super().show_note()
#        elif show_all == 'cards':
#            super().show_card()


#menu = Menu()
#item = Manager()
#item.show_menu()
#item.execute()
#item.show_content()



