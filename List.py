# List in python

my_list = [0, 1, 2]


my_list = ['a', 'b', 'c']

my_list[0] = 1000

print(my_list)

lista = [1, 2, 3, 5, 6, 7, 6]

for list_item in lista:
    print(list_item)

lista.append(45)
lista[6] = 'Hola'
print(lista)
lista.pop()
print(lista)

# Ways of deleting in a list
lista.pop()
lista.remove(4)

del lista[4]
# Merging list
list_one = ["A , B , C , D"]
list_two = ["E , F , G , H"]

list_one.extend(list_two)
print(list_one)
# The length of an array
print(list_one.count())

# Sort a list

