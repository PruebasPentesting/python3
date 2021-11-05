import os
import subprocess


dir1 = os.listdir()
print("1. resize")
print("2. rotate")
print("3. flop")

start = int(input("option: "))

if start == 1:
    size = input("how many % of reduction: ")
    for i in dir1:
        subprocess.run(["convert", "-resize", (size * 50) / 100, i, i])

if start == 2:
    for i in dir1:
        subprocess.run(["convert", i,  "-rotate", "180", i])

if start == 3:
    for i in dir1:
        subprocess.run(["convert", "-flop", i, i])


