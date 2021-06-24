# for i in range(1,21):
#     if i%2 == 0:
#         print(f'{i}:even')
#     else:
#         print(f'{i}:odd')
#
# number = int(input('Enter the number for multiplication table  : '))
# for i in range(1,11):
#     table = number*i
#     print(f'{number}*{i}={table}')
#     if table > 30:
#         break
#
# number = int(input('enter the number for your multiplication table :  '))
# for i in range(1,11):
#     table = number*i
#     print(f'{number}*{i}={table}')
# print('program end')
#
# for i in range(3):
#     for j in range(4):
#         print('%', end=' ')
#     print()

# fruit = (1,2,3,4,5,)
# for i in fruit:
#     print(i)
#     if i >=3:
#         break
#         print(i)

# number_list = (1,2,3,4)
# alpha_list = ['a','b','c']
# for number in number_list:
#     print(number)
#     for alpha in alpha_list:
#         print(alpha  )
#     print()

# i = 0
# while i < 10 :
#     print(i)
#     i = i + 1
#
# i = 1
# while i <=8:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
#

# def hello(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# print(hello(1,5,8,7,9))

#
# def add(**hi):
#     sum = 0
#     for i in hi.values():
#         sum += i
#     return sum
#
#
# print(add(a=112, b=322, c=44))


#

# def add():
#     global a
#     a = a * 3
#     print('inside function a:', a)
#
#
# a = 33
# add()




# def add():
#     a= 3
#     print('add function (non-local) a is',a)
#     def sub():
#         nonlocal a
#         a= a*2
#         print('sub function a is',a)
#     sub()
# a = 33
# print('Global number is',a)
# add()
#
