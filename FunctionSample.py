tom_exp_list = [2100, 3400, 3500]

joe_exp_list = [200, 300, 300]

#
total = 0


#
# for item in tom_exp_list:
#     total += item
#
# print("Tom Total expanses : ", total)
# total = 0
# for item in joe_exp_list:
#     total += item
#
# print("Joe Total expanses : ", total)

# Global variable
addval = 0

def calculate_total(exp):
    sum_exp = 0
    for item1 in exp:
        sum_exp += item1
    return sum_exp


print("Joe Total expanses : ", calculate_total(joe_exp_list))

print("Tom Total expanses : ", calculate_total(tom_exp_list))


def add_val(a, b):
    '''
    This function takes two arguments which are integer numbers and
    it will return sum of them as an output
    '''
    addval = a + b
    print("total inside function :", addval)
    return addval

print("sum of 10+ 5 : ", add_val(10, 5))
# Named argument
print("sum of 6 + 5 : ", add_val(b=6, a=5))
print("total outside function", addval)

#default argument

def multiply(a, b = 1):
    return a * b

print("multiplication of two numbers ", multiply(10, 2))
print("multiplication of two numbers ", multiply(10))


'''
Exercise 1
'''

def calculate_area( base, height ):
    triangle_area = 1/2 *(base * height)
    return triangle_area
'''
Exercise 2
'''

def calculate_area( base, height,shape ):
    area=0
    if shape == "T":
            area = 1/2 * (base * height)

    elif shape == "R":
            area = base * height

    return area

print("Area of Triangle : " , calculate_area(10,5,"T"))
print("Area of Rectangle : " , calculate_area(10,5,"R"))

'''
Exercise 3
'''
def print_pattern(k):
    for i in range(1, k):
        for j in range(1, i + 1):
            print("*", end=" ")
        print("")

print("print_pattern : ", print_pattern(5))