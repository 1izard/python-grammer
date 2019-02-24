from threading import Thread
import time

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


def main():
    numbers = [2139079, 1214759, 1516637, 1852285]
    start = time.time()
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end = time.time()
    print('Took {0:.3f} seconds'.format(end - start))


if __name__ == '__main__':
    main()