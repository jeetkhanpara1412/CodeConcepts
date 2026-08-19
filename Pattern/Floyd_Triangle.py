# Floyd Triangle is a pattern where natural numbers are printed continuously in a triangular shape.

# For example, if n = 5, the output is:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

    