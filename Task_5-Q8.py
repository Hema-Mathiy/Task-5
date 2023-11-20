def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    anagram_str1 = str1.replace(" ", "").lower()
    anagram_str2 = str2.replace(" ", "").lower()

    # Checking if the sorted characters of both strings are the same
    return sorted(anagram_str1) == sorted(anagram_str2)

# The string variables
str1 = "Potato"
str2 = "Tomato"
# Checking if the strings are anagrams
result = is_anagram(str1, str2)
print(f"Are '{str1}' and '{str2}' anagrams? {result}")