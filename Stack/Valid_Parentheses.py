# Problem Statement

# Given a string containing only:

# ( )
# { }
# [ ]

# Determine if the parentheses are valid.

# A string is valid if:

# Every opening bracket has a matching closing bracket.
# Brackets close in the correct order.
# Every opening bracket is closed.



def isValid(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        if ch in "([{":
            stack.append(ch)

        else:

            if not stack:
                return False

            if stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0


print(isValid("()"))
print(isValid("([{}])"))
print(isValid("(]"))
print(isValid("([)]"))


# We use a stack because brackets follow the Last In, First Out (LIFO) principle. 
# We push every opening bracket onto the stack. 
# When we encounter a closing bracket, we check whether it matches the most recent opening bracket at the top of the stack. 
# If it doesn't match or the stack is empty, the string is invalid. 
# After processing all characters, the string is valid only if the stack is empty. 
# This algorithm runs in O(n) time and O(n) space.

