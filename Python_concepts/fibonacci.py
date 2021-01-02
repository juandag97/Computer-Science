
def fibonacci(n, initial = 0, final = 1):
    if n == 0 or n == 1:
        print(1)
    else:
        print(initial+final)
        return fibonacci(n-1, final, initial+final) 
    # if n == 0 or n == 1:
    #     return 1
    # return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("How many numbers of fibonacci series you want to print? "))
    fibonacci(n)

if __name__ == "__main__":
    main()