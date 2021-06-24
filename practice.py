# list = ['karma','lama','palsang','dorje']
# list[3] = 'hello'
# print(list[2:])
# print(list)
#
#
#
#
# matrix =[
#     [2,4,5],
#     [4,3,2],
#     [2,3,4]
# ]
# for row in matrix:
#     for matrix in row:
#         print('6')
#
#
# #
# numbers = [1,2,3,4,5,6,7,8]
# numbers.sort()
# numbers.reverse()
# print(numbers)


# LIST
# numbers = [3,2,4,5,6,7,7,8]
# numbers.append(1999)
# print(numbers)

# numbers = [1,2,3,4*5,5,3.5,6,7]
# numbers.sort()
# print(numbers)

# numbers = [3,3,4,5,6,4,5,7]
# number = []
# for n in numbers:
#     if n not in number:
#         number.append(n)
# print(number)
#


# TUPLE

# numbers = (1,2,3)
# a,b,c = numbers
# print(a+b-c)



# DICTIONARIES
#
# phone_number = input('Phone:  ')
# digit = {
#     '1': 'one',
#     '2': 'Two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine'
# }
# output = ''
# for i in phone_number:
#     output += digit.get(i)+' '
# print(output)


# message = input('>')
# words = message.split(' ')
# emoji = {
#     ':)': '😀',
#     ':(': '😞'
# }
# output = ''
# for i in words:
#     output += emoji.get(i, i) +' '
# print(output)