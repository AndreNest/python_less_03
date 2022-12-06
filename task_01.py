def sum(x, y):
    return x+y
sum_2 = lambda x, y: x + y

def mylt(x, y):
    return x*y
mylt_2 = lambda x, y: x * y
def calc(op, a, b):
    print(op(a, b))

calc(sum, 10, 5)
calc(sum_2, 10, 5)
calc(lambda x, y: x + y, 10, 5)
calc(mylt, 10, 5)
calc(mylt_2, 10, 5)
calc(lambda x, y: x * y, 10, 5)

def x_3(x):
    return x**3

list_4 = [x_3(i) for i in range(1, 21) if i%2 == 0]

print(list_4)

def x_3(x):
    return x**3

list_5 = [(i, x_3(i)) for i in range(1, 21) if i%2 == 0]

print(list_5)