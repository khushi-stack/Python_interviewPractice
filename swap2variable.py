# First Approach
# a = 10
# b = 6
# temp = a  # temp = 10
# a = b  # a = 6
# b = temp # b = 10


# print(a)
# print(b)

# second approach

# a , b = b , a

# print(a)
# print(b)

temp = 0
def swap(a,b):
    temp = a 
    a = b   
    b = temp
    return a , b

a = int(input("Enter the  a  number"))
b = int(input("Enter the b  number"))

a, b = swap(a,b)

print(f"After swapping value of a is {a} and value of b is {b}" )






