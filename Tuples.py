# Tuples in python
my_tuple = (1, 2, 3, 5, 4)
my_second_tuple = ('a', 'aa', 'aaa')
my_third_tuple = (1, 'aaaa', True, 1.33)
user = ("Luis", "Santiago", 20, "Veracruz")

'''for item in user:
    print(item)'''

print(my_tuple[0])
print(my_second_tuple[1])
print(my_third_tuple[2])


def generate_data():
    name = "Luis"
    ages = 24
    city = "Veracruz"
    return name, ages, city


def recieve_data(data):
    print(data[0])
    print(data[1])

recieve_data(generate_data())