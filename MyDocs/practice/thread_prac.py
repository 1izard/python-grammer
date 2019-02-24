import time

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield

def main():
    numbers = [2139079, 1214759, 1516637, 1852285]
    start = time.time()
    for number in numbers:
        list(factorize(number))
    end = time.time()
    print('Took {0:.3f} seconds'.format(end - start))


if __name__ == '__main__':
    main()