# 1.求列表的交集 并集 差集
li1 = [1, 2, 3, 4]
li2 = [2, 3, 5, 6]

res1 = list(set(li1).intersection(set(li2)))
print("交集: ", res1)

res2 = list(set(li1).difference(set(li2)))
print('差集: ', res2)

res3 = list(set(li1).union(set(li2)))
print('并集: ', res3)

# 2.反向输出
str1 = "Hello World"
li = [1, 2, 3, 4, 5]
# reversed
for s in reversed(str1):
    print(s, end='')
print()

# range
for i in range(len(str1)-1, -1, -1):
    print(str1[i], end='')
print()

# [::-1]扩展切片法
for s in str1[::-1]:
    print(s, end='')
print()
print(str1[::-1])

# list自带的reverse方法
li.reverse()
print(li)

# 3.列表嵌套列表排序
foo = [['zs', 19, 1], ['ll', 54, 2], ['wf', 23, -4], ['wf', 23, -3],
       ['xf', 23, 5]]
a = sorted(foo, key=lambda x: (x[1], x[0], x[2]))
print(a)


