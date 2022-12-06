# list22 = []
#
# for i in range(1, 21):
#     if(i%2 == 0):
#         list22.append(i)
#
# print(list22)
#
# list_1 = [i for i in range(1, 21)]
#
# print(list_1)
#
# list_2 = [i for i in range(1, 21) if i%2 == 0]
#
# print(list_2)
#
# list_3 = [(i, i) for i in range(1, 21) if i%2 == 0]
#
# print(list_3)
#
# def x_3(x):
#     return x**3
#
# list_4 = [x_3(i) for i in range(1, 21) if i%2 == 0]
#
# print(list_4)
#
# def x_3(x):
#     return x**3
#
# list_5 = [(i, x_3(i)) for i in range(1, 21) if i%2 == 0]
#
# print(list_5)
#
# list_6 = [1, 2, 3, 5, 8, 15, 23, 38]
# t = lambda x: x**2
# list_8 = [(i, t(i)) for i in list_6 if i % 2 == 0]
# print(list_8)
#
#
# path = 'file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
#
# numbers = []
#
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e, e**2))
#
# print(out)
#
#
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
#
# print(res)
# res_2 = where(lambda x: not x%2, res)
# print(res_2)
#
# res_3 = select(lambda x: (x, x**2), res_2)
# print(res_3)
#
data = '1 2 3 5 8 15 23 38'.split()
res = list(map(int, data))
print(res)
res = list(filter(lambda x: not x % 2, res))
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)


