
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for m in range(60):
            if "3" in str(i) + str(j) + str(m):
                count += 1
print(count)
