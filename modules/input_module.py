from getwaketime import getwakehour

from getwaketime import getwakeminute

print("Hello, and welcone the your home-brewed automatic alarm suite! \n")

x=getwakehour()

y=getwakeminute()

# print(type(x))
# print(type(y))

# if x== int(now.hour):
#     print("cool")

# if y== int(now.minute):
#     print("goond")

# outfile_waketime = open("Wake_up!.runtime.csv", "w")

# outfile_waketime.write(str(x), str(y))

# outfile_waketime.close()

outlist = []

outlist.append([str(x) + ":" + str(y)])

# print(outlist)

with open("runtime.txt", "w") as outfile_waketime:
    for item in outlist:
        outfile_waketime.write("".join(item))

outfile_waketime.close()