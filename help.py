# num = 1000
# for i in range(1,num):
#     print(i)
#     if len(str(i)) == 1 and str(i) == '5':
#         print("Vertical Major Interstate")
#         print("I-5")
#     elif len(str(i)) == 2 and str(i)[-1] in ('0', '5'):
#         if str(i)[-1] == '0' and 1 <= int(str(i)[0]) <= 9:
#             print("Horizontal Major Interstate")
#             print(f"I-{i}")
#         elif str(i)[-1] == '5' and 1 <= int(str(i)[0]) <= 9:
#             print("Vertical Major Interstate")
#             print(f"I-{i}")
#         else:
#             print("Others")
#     elif len(str(i)) == 3 and str(i)[0] != '0':
#         if not int(str(i)[0]) % 2:
#             print("Even Minor Interstate")
#         else:
#             print("Odd Minor Interstate")
#         if str(i)[1] == '0':
#             print(f'I-{str(i)[2]}')
#         else:
#             print(f"I-{str(i)[1:]}")
#     else:
#         print("Others")

help(str)