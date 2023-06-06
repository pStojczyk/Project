# ZAD1

#add = lambda x: x + 15

#print(add(2))

#mul = lambda x, y: x * y

#print(mul(3, 2))

# ZAD2

#to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

#to_sort.sort(key=lambda x: x[1])
#print(to_sort)

#list(map(lambda x: x[1], to_sort))
#result = to_sort
#print(result)
#print(result.sort())
#print(result)
#
#print(sorted(to_sort, key=lambda x: x[1]))

# ZAD3

#nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#square = list(map(lambda x: x**2, nums_list))
#print(square)

#cube = list(map(lambda x: x**3, nums_list))
#print(cube)

# ZAD4

#lines = ['10000101011', '111111', '0101010101010', '011001100001', '001010101011']

#result = len(list(filter(lambda x: x.count('11') == 0, lines)))
#print(result)


# ZAD5

#nums1 = [1, 2, 3]
#nums2 = [4, 5, 6]
#nums3 = [7, 8, 9]
#
#sum_lists = sum(list(map(sum, (nums1, nums2, nums3))))
#print(sum_lists)
#
# ZAD6

#colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

#str_list = list(map(lambda x: ' '.join(x), colors))
#print(str_list)

# ZAD7

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#square = list(map(lambda x: x**2, nums))
#print(square)

#add = list(filter(lambda x: x % 2 == 0, square))
#print(add)

# ZAD8

orders = [
    ["34587", "Learning Python, Mark Lutz", 4, 40.95], ["98762", "Programming Python, Mark Lutz", 5, 56.80],
    ["77226", "Head First Python, Paul Barry", 3, 32.95], ["88112", "Einfuhrung Python3, Bernd Klein", 3, 24.99]
]
invoice = list(map(lambda x: (x[0], x[2] * x[3] if x[2]*x[3] >= 100 else x[2]*x[3] + 10 ), orders))
print(invoice)


#below_100 = list(map(lambda x: x[1] < 100, orders))
#print(below_100)

#add_10 = list(map(lambda x: x + 10, below_100))
#print(add_10)


#class Product:
#    def __init__(self, price, quantity):
#        self.price = price
#        self.quantity = quantity

#    def __str__(self):

#        return f'{self.price} {self.quantity}'

#    def sell(self):
#        for self.price in orders:

#        order = self.price * self.quantity
#        return order



#order1 = Product(orders[0][3], 4)
#print(order1.sell())

#order2 = Product(orders[1][3], 5)
#print(order2.sell())

#order3 = Product(orders[2][3], 3)
#print(order3.sell())

#order4 = Product(orders[3][3], 3)
#print(order4.sell())