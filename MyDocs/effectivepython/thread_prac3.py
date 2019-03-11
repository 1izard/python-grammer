import select, socket
import time
from threading import Thread

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)


def main():
    start = time.time()
    for _ in range(5):
        slow_systemcall()
    end = time.time()
    print('Took {0:.3f} seconds'.format(end - start))
    print()

    start = time.time()
    threads = []
    for _ in range(5):
        thread = Thread(target=slow_systemcall)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end = time.time()
    print('Took {0:.3f} seconds'.format(end - start))
    '''
    Took 0.508 seconds

    Took 0.107 seconds
    '''

if __name__ == '__main__':
    main()