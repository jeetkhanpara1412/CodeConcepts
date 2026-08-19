# Prime Number is a number that has only two factors

# num = int(input("Enter a number: "))

# if num <= 1:
#     print(num, "is not a prime number.")
# else:
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, "is a prime number.")
#     else:
#         print(num, "is not a prime number.")


for i in range(1, 101):
    if i > 1:
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(i)


# Print Prime Numbers Between 1 and 100

# for num in range(1,101):
#     if num > 1:
#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print(num)





# Instead of checking all numbers up to num-1, check only up to √num.
# Time Complexity
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     is_prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not Prime")