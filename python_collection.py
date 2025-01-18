# Lista


my_list = [1,2,3,4, "hola", True, 1.2]
print(type(my_list))
my_list.append(1)
print(my_list)

print(my_list.pop())
print(my_list.pop())
print(my_list.pop())
print(my_list.pop(1))
print(my_list)


my_other_lit = list()

my_other_lit.append(1)

print(my_other_lit)

print(len(my_list))



# Accesos

my_list.append('hola')

print(my_list[0])

print(my_list[-1])

print(my_list.count('hola'))


my_list.insert(3,"adios")
print(my_list)


my_list.remove('hola')

del my_list[0]
print(my_list)
# del my_list
# print(my_list)




#Tuplas 

print("TUPLAS")

my_tuple = (1,2,3,4, "hola", True, 1.2)

# my_other_tuple = tuple()
print(type(my_tuple))


print(my_tuple[0])


# my_tuple[1] = 3 #error
# my_tuple.append(1) #error
# my_tuple.pop() #error

# my_tuple.remove(1) #error

# my_tuple.insert(1,2) #error


# para poder modificarla


my_list = list(my_tuple)

my_list[1] = 3 
my_list.append(1) 
my_list.pop() 

my_list.remove(1) 

my_list.insert(1,2) 


# Sets


my_set = {1,2,3,4,5, "hola", True, 1.2}

my_other_set= set()
print(type(my_set))

# print(my_set[1]) #error

my_set.add(6)

my_set.add(6)

my_set.add(6)
print(my_set)



# Dictionary
my_dict = { "name": "Borja", "age": 30, "is_student": False}

print(type(my_dict))
print(my_dict)
print(my_dict["name"])

# print(my_dict[0]) #error

my_dict["Apellidos"]="Guzmán"
my_dict["Nombre"] = "Pedro"
print("name" in my_dict)
print("Borja" in my_dict)
print(my_dict.items())
print(type(my_dict.items()))
print(my_dict.keys())
print(type(my_dict.keys()))
print(my_dict.values())

