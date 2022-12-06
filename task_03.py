# li = [x for x in range(1,21)]
# print(li)
#
# li1 = map(lambda x: x + 10, li)
# print(li1)
#
# li2 = list(map(lambda x: x + 10, li))
# print(li2)
#
# data = map(int, input().split())
#
# print(data)
#
# data1 = list(map(int, input().split()))
# print('---')
# print(data1)

# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
#
# print(res)
# res_2 = where(lambda x: not x%2, res)
# print(res_2)
#
# res_3 = list(map(lambda x: (x, x**2), res_2))
# print(res_3)

data = [x for x in range(1,11)]
res = filter(lambda x : x % 2 == 0, data)
print(res)
res1 = list(filter(lambda x: x % 2 == 0, data))
print(res1)

res2 = list(filter(lambda x: not x % 2, data))
print(res2)