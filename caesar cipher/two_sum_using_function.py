##find the pair of indices

def two_sum(L, target):
    d = {}

    for i in range(len(L)):
        if target - L[i] in d:
            print(d)
            return [d[target - L[i]], i]
        
        d[L[i]] = i

    return -1

L = [2, 5, 3, 7, 4]
print(two_sum(L, 10))