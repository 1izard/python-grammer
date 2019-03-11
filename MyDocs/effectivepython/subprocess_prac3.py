import subprocess
import time


def run_sleep(period):
    return subprocess.Popen(['sleep', str(period)])


def main():
    start = time.time()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()
    end = time.time()
    print('Finished in {0:.3f} seconds'.format(end - start))



if __name__ == '__main__':
    main()