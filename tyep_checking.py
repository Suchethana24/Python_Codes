length = len("suchi")
length_str = print("my name length is " + str(length) )

new_length = str(length)
print(type(new_length))

numbers = str(1234566789)
print(len(numbers))
print(type(numbers))

name = "suchi"
number = 10
print(number + len(name))

# print(number + int(name)) it gives error because we cant concatenate str and int
#  print(number + name) it also gives error

num_1 = input("enter first number : ")
num_2 = input("enter second number : ")
sum_num = int(num_1) + int(num_2)
print(sum_num)

num_1 = int(input("enter first number : "))
num_2 = int(input("enter second number : "))
sum_num = num_1 + num_2
print(sum_num)

# example

num = input("enter tow digit number : ")
first_num = num[0]
second_num = num[1]
sum_num = int(first_num) + int(second_num)
print(sum_num)