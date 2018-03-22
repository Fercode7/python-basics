# Inputs from user
"""
datoA = int(input("Ingresa un numero"))
datoB = int(input("Ingresa otro numero"))
datoC = int(input("Ingresa otro numero mas"))"""

# Conditional if
'''if datoA > datoB and datoA > datoC:
    print("Number A is the hightes", datoA)
else:
    print("Hola")'''

# While
'''
x = 50
while x > 10:
    print(x)
    x = x - 1 '''

# for
'''for x in range(0, 50, 2):
    print(x) '''

''' datos = ["dato1"], [["dato2"]], ["dato3"]

for dato in datos:
    print(dato) '''


def greet():
    print("Hola mundo")


def square(number: int) -> int:
    return 5 * number


def square_op1():
    print("Realizar operacion")


valor = square(5)
print(valor)
greet()
