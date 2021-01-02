"""
    Notes about recursion in python
    Python has a limit in recursion. We could see it executing:
    import sys
    print(sys.getrecursionlimit()) #Normally the threshold is 1000
    
    And we could modify it with this piece of code:
    sys.setrecursionlimit(n) #Where is n is the new threshold
"""

def factorial(n):
    """
        Estimates the n factorial.
        n is positive greater than 0
        return n!

        Using recursion
    """
    if n == 1:
        return n 
    return n * factorial(n-1)

n = int(input("Type the number you want to calculate: "))
print("The result is:",factorial(n))