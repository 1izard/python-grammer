import subprocess

def main():
    proc = subprocess.Popen(['sleep', '1.0'])
    try:
        proc.communicate(timeout=0.1)
    except subprocess.TimeoutExpired:
        proc.terminate()
        proc.wait()
    print('Exit status', proc.poll())

if __name__ == '__main__':
    main()