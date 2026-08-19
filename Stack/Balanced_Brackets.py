# Problem Statement

# Given a string containing brackets:

# ( )
# { }
# [ ]

# Determine whether the brackets are balanced.

# Balanced means:

# Every opening bracket has a matching closing bracket.
# Brackets close in the correct order.

def is_balanced(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return not stack


# Test Cases
print(is_balanced("{[()]}"))      # True
print(is_balanced("{[(])}"))      # False
print(is_balanced("((()))"))      # True
print(is_balanced("(()"))         # False
print(is_balanced("[]{}()"))      # True