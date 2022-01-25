import csv


with open("Hw.csv",newline="") as f:
    reader = csv.reader(f)
    data   = list(reader)

data.pop(0)

height = []

for i in data:
    num = i[1]
    height.append(float(num))

n = len(height)
mean = sum(height)/n
print(mean)    