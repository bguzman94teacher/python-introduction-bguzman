# ○ SintaxError

# print hola

# ○ NameError

name= "Borja"
# print(nmae)

# ○ IndexError

my_list = [1, 2, 3]
# print(my_list[4])

# ○ ModuleError
# import math3
# math.sqrt(-1)

# ○ AttributeError
import math
# math.sq3rt(-1)

# ○ KeyError
my_dict = {"name": "Borja"}
# print(my_dict["age"])

# ○ TypeError
# ○ ImportError
# ○ ValueError
# ○ ZeroDivisionError



my_dict = {"name": "Borja"}
try:
    print(my_dict["age"])
except KeyError as e:
    print("Error:", e)
else:
    print("No error")
finally:
    print("Finally")
