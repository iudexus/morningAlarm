import datetime

import os

now = datetime.datetime.now()

filename = "\\runtime.txt"

path = os.getcwd()+"\modules"+filename

infile = open(path, "r")

datalist = []

for xline in infile:
    hour, minute = xline.split(":")

# print(hour)
# print(minute)

# print(type(hour))
# print(type(minute))

infile.close()