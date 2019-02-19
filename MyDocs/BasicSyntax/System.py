# System


# File
text = "Hello World!"
with open("test.txt", "wt") as fout:
    fout.write(text)

# exists()
import os
os.path.exists("test.txt")
os.path.exists("./test.txt")    # . is working directory (project directory generally)


# isfile() and isdir()
os.path.isfile("test.txt")  # True
os.path.isdir("test.txt")   # False

# copy()
import shutil
shutil.copy("test.txt", "test_copy.txt")

# move()
# copy file and delete original.
shutil.move("test.txt", "test_moved.txt")

# rename()
import os
os.rename("test.txt", "test_renamed.txt")

# remove()
os.remove("test.txt")

# link()
os.link("test.txt", "test_linked.txt")  # return True or False

# symlink()
os.symlink("test.txt", "test_symlinked.txt")    # return True or False

# chmod()
import stat
os.chmod("test.txt", stat.S_IRUSR)

# chown()

# abspath()
os.path.abspath("test.txt")     # "text.txt" must be in current directory (project directory)

# realpath()
os.path.realpath("test_symlinked.txt")  # return absolute path of symbolic linked file



# Directory
# mkdir()
import os
os.mkdir("texts")
os.mddir("texts/maintexts")

# rmdir()
os.rmdir("texts")

# listdir()
os.listdir("texts")     #["maintexts"]

# chdir()
os.chdir("../")

# glob()



# getpid() & getcwd() & getuid() & getgid()
os.getpid()     # process id
os.getcwd()     # current working directory
os.getuid()     # user id
os.getgid()     # group id


# subprocess
import subprocess
ret = subprocess.getoutput("date")  # get output of date program from UNIX
ret


# multiprocessing
import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n,))
        p.start()


import multiprocessing
import time
import os

def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 100
    for num in range(start, stop):
        print("\tNumber %s of %s, Honk!" % (num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()


# Queue
import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print("Washing", dish, "dish")
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print("Drying", dish, "dish")
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dishes = ["salad", "bread", "entree", "dessert"]
washer(dishes, dish_queue)
dish_queue.join()

