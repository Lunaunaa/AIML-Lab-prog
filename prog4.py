
# Hill Climbing Algorithm

def f(x):
    return -x*x + 6*x

x = float(input("Enter initial value of x: "))
step = 0.1

while True:
    current = f(x)

    left = f(x - step)
    right = f(x + step)

    if left > current:
        x = x - step
    elif right > current:
        x = x + step
    else:
        break

print("Maximum value of x:", x)
print("Maximum value of f(x):", f(x))
