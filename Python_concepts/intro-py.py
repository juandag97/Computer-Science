"""
    Author: @juandag97
    Date: Dec 28 2020, Monday, 10:40
    Algorithms for calculate a square root
"""

#Exhaustive numbering algorithm
def num_exh(target):
    answer = 0
    while answer**2 < target:
        answer += 1
    if answer**2 == target:
        return answer
    else:
        return -1

#Solutions approximation algorithm
def aprox(target, epsilon = 0.01):
    step = epsilon**2
    answer = 0.0
    while abs(answer**2 - target) > epsilon and answer <= target:
        answer += step 
    return answer


def binary_search(target, epsilon = 0.01):
    low = 0
    high = target 
    middle = (low + high)/2
    while abs(middle**2 - target) >= epsilon:
        if middle**2 > target:
            high = middle
        else:
            low = middle
        middle = (low + high)/2
    return middle   


def main():
    text = """
            Hello there, this is a program for calculate a square root for every
            positive number, please read the next steps:
            1. Type the number you want to calculate square root.
            2. Choose the method you want to choose for calculate square root.
            Possible methods:
                Type 1 for Exhaustive numbering algorithm
                Type 2 for Solutions approximation
                Type 3 for Binary Search
           """
    print(text)
    target = int(input("Type the number for calculate square root: "))
    solution = int(input("Choose the method: "))
    root = 1
    if solution == 1:
        root = num_exh(target) 
    elif solution == 2:
        root = aprox(target)
    elif solution == 3:
        root = binary_search(target)
    else:
        print("You type wrong values, please try again.")
        target = int(input("Type the number for calculate square root: "))
        solution = int(input("Choose the method: "))
    print("The square root of {0} is {1}".format(target, root))

if __name__ == "__main__":
    main()
