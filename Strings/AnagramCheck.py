# An Anagram is a word or phrase formed by rearranging the letters of another word or phrase.\
# "heart" → "earth" ✅ (Anagram)
# "hello" → "world" ❌ (Not an Anagram)

# 1: Using sorted() (Most Common)

str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")



# 2: Using Character Count (Without sorted())

# str1 = input("Enter first string: ").lower()
# str2 = input("Enter second string: ").lower()

# if len(str1) != len(str2):
#     print("Not Anagram")
# else:
#     count1 = {}
#     count2 = {}

#     for ch in str1:
#         count1[ch] = count1.get(ch, 0) + 1

#     for ch in str2:
#         count2[ch] = count2.get(ch, 0) + 1

#     if count1 == count2:
#         print("Anagram")
#     else:
#         print("Not Anagram")

