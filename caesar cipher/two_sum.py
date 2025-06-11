L = [2, 5, 3, 7, 4]
target = 10

res = []
for i in range(len(L) - 1):
    for j in range(i+1, len(L)):
        
        if L[i] + L[j] == target:
            res.append((L[i], L[j]))

print(res)