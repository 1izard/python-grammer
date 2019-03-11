import subprocess

def main():
    procs = []
    for i in range(5):
        proc = subprocess.Popen(
            ['echo', 'Hello from {}th child!'.format(i)],
            stdout=subprocess.PIPE
        )
        procs.append(proc)

    outs = []
    for proc in procs:
        out, err = proc.communicate()
        outs.append(out)

    print(outs)

if __name__ == '__main__':
    main()