import multiprocessing

def test():
    print("This is my multiprocessing program.")


def square(n):
    return n**2


def producer(q):
    for i in ["sudh", "pwskills", "krish", "kumar", "himraj"]:
        q.put(i)


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)


def square1(index, value):
    value[index] = value[index]**2

if __name__ == "__main__":

    # m = multiprocessing.Process(target=test)
    # print("This is my main program")
    # m.start()
    # m.join()

    # with multiprocessing.Pool(processes=4) as pool:
    #     out = pool.map(square, [2, 3, 4, 5, 6])
    #     print(out)


    # queue = multiprocessing.Queue()
    # m1 = multiprocessing.Process(target=producer, args=(queue,))
    # m2 = multiprocessing.Process(target=consume, args=(queue,))
    # m1.start()
    # m2.start()
    # queue.put("xyz")
    # m1.join()
    # m2.join()


    arr = multiprocessing.Array("i", [2, 3, 4, 5, 6, 7, 8])
    process = []
    for i in range(7):
        m = multiprocessing.Process(target=square1, args=(i, arr))
        process.append(m)
        m.start()
    for m in process:   
        m.join()
    print(list(arr))

