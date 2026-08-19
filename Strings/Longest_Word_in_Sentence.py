# Given a sentence, find the longest word present in it.

# Input:
# "Python is a powerful programming language"
# Output:
# programming


# 1: Using split() and max() (Best Method)
sentence = input("Enter a sentence: ")
longest = max(sentence.split(), key=len)
print("Longest word:", longest)



# 2: Using a for Loop

sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
