# Variable scope as the life of the variable

# Local Scope - Defined inside function
# Enclosing Scope - nested function
# Global Scope - Defined outside
# Built in Scope

# Global Scope --- Defined outside
global_var = "I'm a global variable"

def outer_func():
    # Enclosing_Scope
    enclosing_var = "I'm a enclosing variable"

    def inner_func():
        # Local Variable
        local_var = "I'm a local variable"

        print(local_var)
    print(enclosing_var)
    inner_func()

    print(global_var)