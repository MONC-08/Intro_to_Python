def calculate_mean(*args):
    if len(args) == 0:
        return "No values provided!"
    
    mean = sum(args) / len(args)
    return mean

print(calculate_mean(10, 20, 30))
print(calculate_mean(15, 20, 25, 30, 35, 40, 45, 50))
print(calculate_mean())
