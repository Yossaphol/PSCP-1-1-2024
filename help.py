# print(True and -2)
# print(-2 and True)
# print(1 or 0)
# print(0 or -1)

# i = -1
# while i > -8:
#     print(i)
#     i -= 3

# print((10, 'hello') > (9, 'moon'))
# print(('moon', 10) > ('world', 20))
# print(('10', 'world') > ('2', 'world'))
# print((10, 11, 12, 1) > (10, 11, 12, 2))

# ts = 'abcdefg'
# print(ts[::-1])

# muy = []
# for i in range(5):
#     n = input()
#     muy.append(n)

# muy.sort(key=len, reverse=True)
# for i in range(len(muy)):
#     print(muy[i])
# print(muy)

# dictt = {'car':'honda', 'serie':'cmd', 'year':2014,'color':'white'}
# for i in dictt:
#     print(i)

# for j in dictt:
#     print(dictt[j])


fruit = ('apple', 'banana', 'grape')
color = ('red', 'yellow', 'green', 'purple')

mix = zip(fruit, color)
print(mix)
print(tuple(mix))