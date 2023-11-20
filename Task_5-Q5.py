def isPalindrome(input_str):
    return input_str == input_str[::-1]
# Storing a value in one variable
input_str = "malayalam"
result = isPalindrome(input_str)
# Using if loop to check the input_str is palidrome or not
if result:
    print(f"Is '{input_str}' a palindrome? {result}")
else:
    print(f"Is '{input_str}' a palindrome? {result}")