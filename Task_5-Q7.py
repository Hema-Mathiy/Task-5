# Assigning a string variable
str1 = "mississippis"
print(f"The entered value is ",{str1})

# Creating a empty dict
most_frequent_char = {}

# Counting the frequency of each character in the string
for char in str1:
    if char in most_frequent_char:
        most_frequent_char[char] += 1
    else:
        most_frequent_char[char] = 1

# Finds the character with the maximum frequency
result = max(most_frequent_char, key=most_frequent_char.get)

# Printing the result
print("Most frequent character:", result)
