# A Perfect Number is a positive integer that is equal to the sum of all its proper divisors (excluding the number itself).

# 6 → Divisors: 1, 2, 3
# Sum = 1 + 2 + 3 = 6 ✅ Perfect Number

# 12 → Divisors: 1, 2, 3, 4, 6
# Sum = 1 + 2 + 3 + 4 + 6 = 16
# 16 ≠ 12 ❌ Not a Perfect Number

# Algorithm
# Input a number n.
# Initialize sum = 0.
# Loop from 1 to n-1.
# If i divides n exactly (n % i == 0):
# Add i to sum.
# Compare:
# If sum == n → Perfect Number.
# Otherwise → Not a Perfect Number.

# 1 using for loop 
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is Not a Perfect Number")