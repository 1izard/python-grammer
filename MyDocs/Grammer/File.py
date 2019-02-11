# File

# Text file
# write()
    # fileobj = open(filename, mode)
        # mode
            # 1st Character : r(read), w(write), x(write just when the file does not exist), a(append)
            # 2nd Character : t(text), b(binary)
    poem = '''There was a youg lady named Bright,
    Whose speed was far faster than light;'''

        # write()
        fout = open("relativity", "wt")
        print(fout.write(poem))     # 74
        fout.close()

        # print()
        # adding space after every argument and new line
        fout = open("relativity", "wt")
        print(poem, file=fout)
        fout.close()

        # not adding
        print(poem, file=fout, sep="", end="")
        fout.close()

    # chunk
    fout = open("relativity", "wt")
    size = len(poem)
    offset = 0
    chunk = 20
    while True:
        if offset > size:
            break
        fout.write(poem[offset:offset+chunk])
        offset += chunk
    fout.close()

    # x
    try:
        fout = open("relativity", "xt")
        fout.write("stomp stomp stomp")
    except FileExistsError:
        print("relativity already exists.")


# read() & readline() & readlines()
    # read()
    fin = open("relativity", "rt")
    poem = fin.read()
    fin.close()

        # chunk
        poem = ""
        fin = open("relativity", "rt")
        chunk = 20
        while True:
            fragment = fin.read(chunk)
            if not fragment:
                break
            poem += fragment
        fin.close()

    # readline()
    poem = ""
    fin = open("relativity", "rt")
    while True:
        line = fin.readline()
        if not line:
            break
        poem += line
    fin.close()

    # iterator
    poem = ""
    fin = open("relativity", "rt")
    for line in fin:
        poem += line
    fin.close()

    # readlines()
    # return list of lines
    fin = open("relativity", "rt")
    lines = fin.readlines()
    fin.close()


# Binary file
bdata = bytes(range(0, 255))

    # write()
    fout = open("bfile", "wb")
    fout.write(bdata)
    fout.close()

        # chunk
        fout = open("bfile", "wb")
        offset = 0
        chunk = 20
        while True:
            if offset > len(bdata)
                break
            fout.write(bdata)
            offset += chunk
        fout.close()

    # read()
    fin = open("bfile", "rb")
    bdata = fin.read()
    fin.close()

        # seek(offset[,origin])
        # origin=0 : move from 0 to offset
        # origin=1 : move from current position to offset
        # origin=2 : move from end to offset
        fin = open("bfile", "rb")
        fin.seek(254, 0)
        fin.read()
        fin.close()

# with
# with expression as variable
    with open("relativity", "wt") as fout:
        fout.write(poem)



# CSV
    # wirte
        # list of list
        import csv
        philosophers = [
            ["Spinoza", "Netherlands"],
            ["Descartes", "France"],
            ["Kant", "German"]
        ]
        with open("philosopehrs", "wt") as fout:
            csvout = csv.writer(fout)
            csvout.writerows(philosophers)

        # list of dictionary
        philosophers = [
            {"Name": "Spinoza", "Country": "Netherlands"},
            {"Name": "Descartes", "Country": "France"},
            {"Name": "Kant", "Country": "German"}
        ]
        with open("philosophers", "wt") as fout:
            csvout = csv.DictWriter(fout)
            csvout.writeheader()    # adding header as column name
            csvout.writerows(philosophers)

    # read
        # list of list
        with open("philosophers", "rt") as fin:
            csvin = csv.reader(fin)
            philosophers = [row for row in csvin]
            # [["Spinoza", "Netherlands"], ...]

        # list of dictionary
        with open("philosophers", "rt") as fin:
            # if there is header, call csv.DictReader() without argument "fieldnames"
            csvin = csv.DictReader(fin, fieldnames=["Name", "Country"])
            philosphes = [row for row in csvin]
            # [{"Name": "Spinoza", "Country": "Netherlands"}, ...]


# JSON
    menu = {
        "breakfirst": {
            "hours": "7-11",
            "items": {
                "breakfirst burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

    # encode
    import json
    menu_json = json.dump(menu)

    # decode
    menu2 = json.loads(menu_json)


