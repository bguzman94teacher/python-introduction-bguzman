


print("Hello World!")

'''
esto es un comentario
'''

"""
esto es otro comantario
"""

# comentario sencillo


'''tipos de datos'''
print("tipos de datos")
print(type(print))
print(type(1))
print(type(1.2))
print(type("hola"))
print(type("hola"[0]))
print(type(True))


'''variables'''
print("Variables")
name = "Borja"
print(type(name))
name= 30
print(type(name))

age : int =9
print(type(age))
age = "borja"

print(type(age))

# id = input("¿que id quiere añadir?")
# print(id)

'''string'''

print("String")

product_name = "manzanas"
quantity = 10


print('Ha comprado' + " " + str(quantity) + " " +  product_name)
print("Ha comprado {} {}".format(quantity,product_name))
print("Ha comprado %d %s" % (quantity,product_name))
print(f"Ha comprado {quantity} {product_name}")

address = "calle de la fantasia n13 4ºD"

print(address)

print(address[0])
print(address[2:6])
print(address[2:])
print(address[:6])
print(address[-2])

#reverse
print(address[::-1])


print(address.capitalize())
print(address.upper())
print(address.count("t"))
print(address.isnumeric())
print("1".isnumeric())
print(address.lower())
print(address.lower().isupper())
print(address.startswith("ca"))
print("Py" == "py")  
print("holb" >"hola")
print("hola"*2)








# mirar varibales ambito en funcion


