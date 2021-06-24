# #The secret name is palsang
# secret_name = 'palsang'
# guess_count = 0
# guess_limit = 2
# while not guess_count > guess_limit:
#     guess = str(input('guess a name ?  '))
#     guess_count += 1
#     if guess == secret_name:
#         print('You won!')
#         break
# else:
#     print('You lose')



                        # question

#
# 1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# 2. Print "Hello" if a is equal to b, and c is equal to d.
# 3. Print "Hello" if a is equal to b, or if c is equal to d.
# 4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
# 5. Check whether the user input number is even or odd and display it to user.
# 6.  WAP which accepts marks of four subjects and display total marks, percentage and
# grade.
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass,
# less than 40% –> fail
# 7. What is the output of ‘APPLE’ > ‘apple’?
#
# 8. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# 9. Write a Python program to display your details like name, age, address in three different lines.
# 10. Write a python program which accepts the radius of circle from user and compute the area.
#
# 11. Solve each of the following problems using Python Scripts. Make sure you use appropriate
# variable names and comments. When there is a final answer have Python print it to the
# screen.
# A person’s body mass index (BMI) is defined as:
# BMI=mass in kg / (height in m)2
#
# 12. A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks
# that can be purchased.
# The program should read three integers: the number of students in each of the three
# classes, a, b and c respectively.
# Hint. In the first test there are three groups. The first group has 20 students and thus needs 10
# desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
#


                       # answers

#
# a = int(input('a number : '))
# b = int(input('b number : '))
# if a==b:
#     print(1)
#
# a = int(input('a number : '))
# b = int(input('b number : '))
# if a > b:
#     print(2)
# else:
#     print(3)

#
#
#
# a = int(input('a number : '))
# b = int(input('b number : '))
# c = int(input('c number : '))
# d = int(input('d number : '))
# if a == b or c == d:
#     print('hello')
# else:
#     print('invalid')


#
# number = int(input('enter the number:  '))
# i = 0
# if i < number:
#     print('True')
#     if i > number:
#         print('False')
# else:
#     print('Zero')



#
# number = int(input('enter the number: '))
# if number % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd')
#


# first_name = str(input('first name?  '))
# last_name = str(input('last name ? '))
# for i in last_name,first_name:
#     print(i,end=' ')



# name = str(input('what is your name?'))
# age = int(input('how old are you? '))
# address = str(input('where do you live? '))
# print(f'''Name: {name}
# Age: {age}
# Address : {address}''')



# result = int(input('Enter your number? '))
# if result >= 70:
#     print('Distinction')
#     if result >= 60:
#         print('First')
#     elif result >= 40:
#         print('Pass')
# else:
#     print('Fail')

#
#
# mass_in_kg = int(input('enter the mass in kg:  '))
# height = int(input('enter the height :  '))
# BMI = mass_in_kg/(height^2)
# print(BMI)

# p = int(input('enter the marks for physics:  '))
# b = int(input('enter the marks for biology:  '))
# c = int(input('enter the marks for chemistry:  '))
# m = int(input('enter the marks for math:  '))
# total = p+b+c+m
# print(f'the total score is {total}')
# percentage = (total/400)*100
# print("total percentage is ",percentage,'%')
# if percentage > 70:
#     print('he got distincion')
# elif percentage > 60:
#     print('he got first division')
# elif percentage > 40:
#     print('he passed the exam')
# elif percentage < 40:
#     print('he failed')

# first_name = str(input('enter the first name;  '))
# last_name = str(input('enter the last name;  '))
# print(f'{last_name} {first_name}')

# name = str(input('What is your name? '))
# age = int(input('How old are you? '))
# address = str(input('Where do you live? '))
# print(f'''name : {name}
# age : {age}
# address : {address}''')

# radius = int(input('enter the radius of circle: '))
# area = 3.14*(radius*radius)
# print(area)


# class_1 = 20
# class_2 = 21
# class_3 = 22
# desk1 = class_1//2
# print(f'required desk for class1 is {desk1}')
# desk2 = class_2//2
# print(f'required desk for class2 is {desk2}')
# desk3 = class_3//2
# print(f'required desk for class3 is {desk3}')
# remaining1 = class_1%2
# print(f'remaining desk for class is {remaining1}')
# remaining2 = class_2%2
# print(f'remaining desk for class2 is {remaining2}')
# remaining3 = class_3%2
# print(f'remaining desk for class3 is {remaining3}')
# Total = desk1+desk2+desk3+remaining3+remaining2+remaining1
# print(f'total number of desks that can be purchased is {Total}')

