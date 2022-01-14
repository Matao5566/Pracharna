import math

cd = [2, 5, 4, 9, 8, 4, 5, 7, 3]
# print(sorted(cd))
x = 1
for i in range(0, len(cd)):
    for j in range(0, len(cd)-x):
        if cd[j] > cd[j+1]:
            cd[j+1], cd[j] = cd[j], cd[j+1]
    x+=1
print(cd)