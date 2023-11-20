# Assigning the vowels
vowels = 'aeiou'
# Get the input
string_count = input("Enter the string to count: ")
# convert string in case insensitive
string = string_count.casefold()

# create a dictionary with each vowel a key and value 0
count_vowels = {}.fromkeys(vowels, 0)

# count the number of each vowels
for x in string:
    if x in count_vowels:
        count_vowels[x] += 1

print("Total number of vowels - ", count_vowels)