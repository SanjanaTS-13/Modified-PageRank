import sys

# reading csv file
with open(sys.argv[1], "r") as myfile:
    data = myfile.readlines()

del data[0]

tMin = "0"
tMax = "16"
w = "1"
V = "11"
E = "12"

print(w + " " + V + " " + E + " " + tMin + " " + tMax)
for i, ele in enumerate(data):
    ele = ele.replace(",", " ")
    print(ele, end = "")