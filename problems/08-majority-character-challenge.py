# Given a string, write a function that returns the character that is the
# majority of the string. If there is no majority character, return None. A
# majority is considered as having more than `n / 2` instances where `n` is the
# length of the string.

# Write your code here.
def majority_char(s):
    count = {}
    n = len(s)

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char, count in count.items():
        if count > n / 2:
            return char

    return None

str = 'all'
str2 = 'welcome to the jungle'

print(majority_char(str))           # 'l'
print(majority_char(str2))          # None