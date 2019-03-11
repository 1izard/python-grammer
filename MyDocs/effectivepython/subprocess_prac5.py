import subprocess
import os

def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Q13S\x11'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


def main():
    procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = run_openssl(data)
        procs.append(proc)

    for proc in procs:
        out, err = proc.communicate()
        print(out[-10:])


if __name__ == '__main__':
    main()