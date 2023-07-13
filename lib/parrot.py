""" Instructions
This is a test-driven lab. Run pipenv install to create your virtual environment and pipenv shell to enter the virtual environment. Then run pytest -x to run your tests. Use these instructions and pytest's error messages to complete your work in the lib/ folder.

In this lab, you'll be defining a function called parrot().

The parrot() function should accept an argument of a string and both print() and return the string at the end of the function.

The parrot() function should have a default argument of "Squawk!"

NOTE: This lab is explicitly testing your ability to control the return value of a function: not just what it does, but what it returns. Remember, return values are important. What's the return value of print()?
 """

def parrot(default ="Squawk!"):
    print (default)
    return default
    
    
    
"""     def parrot(default ="Squawk!"):
            return default
            print (default) """
            
""" The given code is not equivalent to the original code.

In the modified code, the return statement comes before the print statement. In Python, when a return statement is executed, it immediately exits the function and returns the specified value. Therefore, any code after the return statement will not be executed.

In this case, since the return default statement is placed before the print(default) statement, the print statement will never be reached. The function will immediately exit after returning the value of the default parameter.

To clarify, the modified code will only return the value of default and will not print anything.   """        
    
     


