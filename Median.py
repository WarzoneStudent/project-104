import csv
from statistics import median


with open("Hw.csv",newline="") as f:
    reader = csv.reader(f)
    data   = list(reader)

data.pop(0)

height = []

for i in data:
    num = i[1]
    height.append(float(num))

n = len(height)
height.sort()

if n%2 == 0:
    median1 = height[n//2]
    median2 = height[n//2-1]
    median = (median1+median2)/2
else:
    median = height[n//2]
    
print(median)    