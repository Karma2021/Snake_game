# def add():
#     print('function start')
#     a = int(input('enter the number:  '))
#     b = int(input('enter the number:  '))
#     c = a+b
#     print(f'the sum of {a} and {b} is {c}')
#     print('function end')
# print('program start')
# add()
# print('first calling of function completed')
# add()
#
# print('program end')


                  #day 3

#
# 1. Add Two Numbers With User Input.
# 2. write a program to find the sum of the first n positive numbers.
# sum = (n*(n+1))/2
# 3. Given the integer N - the number of minutes that is passed since midnight - how many
# hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23) and the
# number of minutes (between 0 and 59).
# For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30
# am. So, the program should print 2:30.
#
# 4. Write a Python Program to Check Prime Number.
# 5. Write a program to convert second into hour, minute & second.
# 6. Write a program that asks the user for a number in the range of 1 to 7. The program should display the corresponding day of the week, where
# 1=sunday, 2=monday,3=tuesday,4=wednesday,5=thursday,6=friday,7=saturday. The program should display an error message if the user enters a number
# that is outside the range of 1 to 7.
# 7. Write a Python Program to Find the Square Root of 100.
# 8. Write a Python Program to Swap Two Variables.
# 9. Write a Python Program to find the sum of all numbers stored in a list.
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# 10. Write a Python Program to display student's marks from record.
#
# a = int(input('enter the number:  '))
# b = int(input('enter the number:  '))
# sum = a + b
# print(f'the sum of {a} and {b} is {sum}')


#
#
# list = [1, 2, 3, 4, 5, 6]
# total = sum(list)
# print(f'the sum of given positive number is {total}')


#
# number = int(input('enter the minute passed since mid night:  '))
# hour = number//60
# minute = number%60
# print(f'now is {hour}:{minute}')


#
# number = int(input('enter any second:  '))
# hour = number//3600
# rhour = number%3600
# minute = rhour//60
# second = rhour%60
# print(f"{hour}:{minute}:{second}")


# numbers = [1,2,3,4,5,6,4,3,3,2,4]
# sum = 0
# for i in numbers:
#     sum = sum+i
#     print(f'The sum is {sum}')
# print(f'The total sum is {sum}')

#
# student_name = str(input('Enter the name of student:  '))
# marks = {'lama':70, 'hello':50, 'karma':100, 'sp':20}
#
# for student in marks:
#     if student == student_name:
#         print(marks[student])
#         break
# else:
#     print('Invalid name')


#
#                           ** day(4) **
#
#
#
# class_a = int(input('class a : '))
# class_b = int(input('class b : '))
# class_c = int(input('class c : '))
# d1 = class_a//3
# d2 = class_b//3
# d3 = class_c//3
# rm1 = class_a%3
# rm2 = class_b%3
# rm3 = class_c%3
# total = d1+d2+d3+rm1+rm2+rm3
# print(f'total desk needed is {total}')
#
# fruit = 'banana'
# FRUIT = 'BANANA'
# f = fruit>FRUIT
# print(f)
#
# students = int(input('enter the student number:  '))
# apples = int(input('enter the number of apples:  '))
# student_apple = apples//students
# rem_apples = apples%student_apple
# print(f'all student got {student_apple}')
# print(f'the remaining apples in the basket is {rem_apples}')
#
#
#
# list = [1,2,3,4,5]
# for i in list:
#     if i == 5:
#         print('True')
#
# number1 = int(input('enter the number:  '))
# number2 = int(input('enter the number:  '))
# number3 = int(input('enter the number:  '))
# list = [number1, number2, number3]
# print('the smallest number is', min(list))
#
# list = [1,2,3,4,5,6]
# print(list[5])
#
#
# number = [3,4,5]
# sum = sum(number)
# print(f'the sum of given numbers is {sum}')



                # *** Day (5) ***


# numbers = [445, 55.4, 332.3]
# max_num = max(numbers)
# print('The max number is',max_num)


# numbers = [333,222,4455]
# min_num = min(numbers)
# print('The minimum number is',min_num)


# def fizz_buzz(num):
#     if (num % 3 ==0) and (num % 5==0):
#         return "hello"
#     elif num % 3 == 0 :
#         return 'apple'
#     elif num % 5 == 0 :
#         return 'banana'
#     else:
#         print(num)
#
# a = int(input('Enter the number: '))
# b = fizz_buzz(a)
# print(b)
#








# def max():
#     first_num = int(input('Enter the number:  '))
#     second_num = int(input('Enter the number:  '))
#     third_num = int(input('Enter the number:  '))
#     if first_num > second_num and first_num > third_num:
#         print('The maximum number is', first_num)
#     elif second_num > first_num and second_num > third_num:
#         print('The maximum number is', second_num)
#     else:
#         print('The maximum number is', third_num)
#
# max()


def fizzbuzz(num) :
    if (num % 3 ==0) and (num% 5 ==0):
        return "Fizzbuzz"
    elif num % 5 == 0 :
        return "Buzz"
    elif num % 3 == 0 :
        return "Fizz"
    else :
        print(num)


# calling function
a = int(input("enter the number:"))
b = fizzbuzz(a)
print(b)
print("end of program")

#
# def age(name, age):
#     print(name, age)
#
#
# age('karma', 20)
#
# number = int(input('Enter the number:  '))
# for i in range(1,13):
#     if number == 1:
#         print('january')
#         break
#     elif number == 2:
#         print('february')
#         break
#     elif number == 3:
#         print('march')
#         break
#     elif number == 4:
#         print('april')
#         break
#     elif number == 5:
#         print('may')
#         break
#     elif number == 6:
#         print('june')
#         break
#     elif number == 7:
#         print('july')
#         break
#     elif number == 8:
#         print('august')
#         break
#     elif number == 9:
#         print('september')
#         break
#     elif number == 10:
#         print('october')
#         break
#     elif number == 11:
#         print('november')
#         break
#     elif number == 12:
#         print('december')
#         break
#     else:
#         print('invalid number!!')
#         break
