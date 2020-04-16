def step(x, n):
    if n > 0:
         return x * step(x, n-1)
    elif n < 0:
         return 1.0 / step(x, -n)
    return 1
 
print(step(float(input()), int(input())))