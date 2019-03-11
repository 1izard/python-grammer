import subprocess


def main():
    proc = subprocess.Popen(['sleep', '0.3'])
    while proc.poll() is None:
        print('polling...')
    print(proc.poll())


if __name__ == '__main__':
    main()