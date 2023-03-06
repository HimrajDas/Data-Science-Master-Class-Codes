import multiprocessing

def sender(conn, msg):
    for i in msg:
        conn.send(i)
    conn.close()


def recieve(conn):
    while True:
        try:
            msg = conn.recv()
        except Exception as e:
            print(e)
            break
        print(msg)


if __name__ == "__main__":
    msg = ["my name is himraj", "I am learning Data Science", "Tech is great"]
    parent_conn, child_conn = multiprocessing.Pipe()
    m1 = multiprocessing.Process(target=sender, args=(child_conn, msg))
    m2 = multiprocessing.Process(target=recieve, args=(parent_conn,))
    m1.start()
    m2.start()
    m1.join()
    child_conn.close()
    m2.join()
    parent_conn.close()