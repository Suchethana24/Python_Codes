def max_of_three(a,b,c):
    if a>b and a>c:
        print(a)
    if b>c:
        print(b)
    else:
        print(c)
max_of_three(100,200,400)


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    print(total)

sum((1,2,3,4,5))


def mul_list(list_1):
    total = 1
    for x in list_1:
        total *= x
    print(total)
mul_list([8, 2, 3, -1, 7])


def reverse_string(string):
    r_str = " "
    for i in string:
        r_str = string[::-1]
    print(r_str)
reverse_string("1234abcd")

def fac(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f)
fac(3)

def number(n):
    if n in range(1,9):
        print("the number is in the range ")
    else:
        print("the number is not in the range")
number(9)


def str_test(str):
    upper_case = 0
    lower_case = 0
    for i in str:
        if i.isupper():
            upper_case += 1
        if i.islower():
            lower_case += 1
    print(f"upper case letters in given string are {upper_case}")
    print(f"lower case letter in given string are {lower_case}")

str_test('The quick Brow Fox')




def area_of_triangle(height,base):
    area = (1/2)*base*height
    print(area)

area_of_triangle(2,3)




i = 0


def pattren(n):

    for i in range(n+1):
        s = " "

        for j in range(i+1):
            i += 1
            s = s + "*"
        print(s)


pattren(4)


def calculating_area(dimension1,dimension2,shape):

    if shape == "triangle":
        area_triangle = (1/2)*dimension1*dimension2
        print(area_triangle)

    elif shape == "rectangle":
        area_rectangle= dimension1*dimension2
        print(area_rectangle)

    else:
        print("sorry wrong angle you have taken")


calculating_area(4, 5, "triangle")
calculating_area(6, 7, "suchi")










