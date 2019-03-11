import subprocess


def main():
    proc = subprocess.Popen(
        ['echo', 'Hello from the child!'],
        stdout=subprocess.PIPE
    )

    print('proc.poll() =', proc.poll())

    proc2 = subprocess.Popen(
        ['echo', 'Goodnight from the child...'],
        stdout=subprocess.PIPE
    )

    print('proc.poll() =', proc.poll())
    print('proc2.poll() =', proc2.poll())

    # communicate() reads stdout from proc after proc terminated.
    # stdout of proc must be PIPE so that parent process (main process) can access it.
    out2, err2 = proc2.communicate()
    out, err = proc.communicate()

    print(out2.decode('utf-8'))
    print(out.decode('utf-8'))
    print()

    print('proc.poll() =', proc.poll())
    print('proc2.poll() =', proc2.poll())
    print()

    proc3 = subprocess.Popen(
        ['echo', 'Good evening from child'],
    )
    out3, err3 = proc3.communicate()

if __name__ == '__main__':
    main()