def my_gen():
    a = 1
    yield a 

    a = 2
    yield a 

    a = 3
    yield a 

def pair():
    for i in range(0,201,2):
        yield i 

# my_first_gen = my_gen()
# print(next(my_first_gen))
# print(next(my_first_gen))
# print(next(my_first_gen))


if __name__ == "__main__":
    first_gen = pair()
    for j in range(100):
        print(next(first_gen))