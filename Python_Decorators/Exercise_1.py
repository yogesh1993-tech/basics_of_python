"""
Create a decorator function to check that the argument passed
to the function factorial is a non-negative integer:
"""

def check(f):
    def helper(x):
        if type(x)==int and x>0:
            return f(x)
        else:
            raise Exception("Argument is not a non-negative integer")
        return  helper


    
