import time

def test():
    print("This is start of the function.")
    print(4 + 5)
    print("This is end of the function.")


# test()

def deco(func):
    def inner_deco():
        print("This is the start of my function.")
        func()
        print("This is the last of my function.")

    return inner_deco


@deco
def test1():
    print(4 + 5)


# test1()


def timer_test(func):
    def timer_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    
    return timer_test_inner


@timer_test
def test2():
    print(50 + 50)

# test2()


@timer_test
def test3():
    for i in range(10000000):
        # print(i, end="")
        pass

test3()