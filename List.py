"""List Python"""

number = [1,2,3,4,5,6]
names = ['James', 'John', 'Rose', 'Meldar', 'Ohalon']
my_list = [['melon', 'orange'], 'cherry', 'mango', 'pineapple']

#how to print info in list (Sequence)
print(number[0])
print(names[3])
print(my_list[0][1])

#Slice
print(names[1:4])

"""List Method"""

'''ADD'''
my_list1 = ['cherry', 'mango', 'pineapple']
#append
my_list1.append('orange')
print(my_list1)
#insert
my_list1.insert(1, 'melon')
print(my_list1)
#extend
list_extend = [1,2]
my_list1.extend(list_extend)
print(my_list1)
# +
my_list2 = [1,2,3,4]
my_list3 = [5,6,7,8]
mylist4 = my_list2 + my_list3
mylist5 = my_list3 + my_list2
print(mylist4)
print(mylist5)

'''REMOVE'''
my_list1 = ['cherry', 'mango', 'pineapple', 'melon', 'orange']
#remove
my_list1.remove('cherry')
print(my_list1)
#pop
my_list2 = ['cherry', 'mango', 'pineapple', 'melon', 'orange']
my_list2.pop() #last order
pop1 = my_list2.pop(0)
print(pop1)
print(my_list2)
#clear
my_list2.clear()
print(my_list2)
# #del
# del my_list1
# print(my_list1)

'''change to list'''
one = {'one' : 1, 'two' : 2}
two = ('0n3', 'tw0')
print(list(one))
print(list(two))

'''copy len count index'''
list1 = [1,2,3,4,5,3,4,6,8,3]
list2 = list1.copy()
print(list2)
print(len(list1))
print(list1.count(3))
print(list1.index(2))


'''sort sorted'''
number = [3,4,6,9,2,1,4,0,5,3,7,8,1,0,3,2,5,6]
num1 = number.copy()
num1.sort()
print(num1)
print(num1[::-1])
num1.sort(reverse=True)
print(num1)
num2 = sorted(num1)
print(num2)

#use key
name = ['aaa', 'bbbbbb', 'c', 'dd']
print(f"name default : {name}")
name.sort(key=len)
print(f"sorted list : {name}")


#list to string
list1 = ['aa', 'bbb', 'c', 'dd', 'eee', 'f']
print(' '.join(list1))
print(*list1)
print(*list1, sep='\n')
#string to list - use json and not use json
#use json
import json
txt = '["aa", "bbb", "c", "dd"]'
print(json.loads(txt))
#don't use json
text = 'hello world and banana i love u'
print(text.split())