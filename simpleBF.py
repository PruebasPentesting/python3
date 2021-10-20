import os

#testing brute force...


def create_txt():
    name = "passlst.txt"
    os.remove(name)
    txt = open(name, "a+")
    for i in range(0, 1000000):
        txt.write(str(i)+"\n")
        
    txt.close()
    txt = open(name, "r")

    key = "900000"

    brute_force(key, txt)




def brute_force(key, txt):
    content = txt.readlines()
    for line in content:
        if key in line:
            print("found " + key.strip())
            break

        else:
            print("not " + line.strip())

    txt.close()

create_txt()
