x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Imprime "local"
    
    inner()
    print(x)  # Imprime "enclosing"

outer()
print(x)  # Imprime "global"