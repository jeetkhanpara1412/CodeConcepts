# A Number Pyramid is a pattern where numbers are printed in the shape of a pyramid. It is a very common interview and programming practice question because it helps you understand:


# n = 5

#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

n = 5

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print numbers
    for j in range(i):
        print(i, end=" ")

    print()



# 3: Palindrome Number Pyramid
#     1
#    212
#   32123
#  4321234
# 543212345

n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Descending numbers
    for j in range(i, 0, -1):
        print(j, end="")

    # Ascending numbers
    for j in range(2, i + 1):
        print(j, end="")

    print()