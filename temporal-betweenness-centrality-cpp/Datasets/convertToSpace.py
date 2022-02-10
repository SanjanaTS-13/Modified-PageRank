# reading csv file
with open(argv[1], "r") as myfile:
    data = myfile.readlines()

del data[0]

tMin = 0
tMax
w = 1
