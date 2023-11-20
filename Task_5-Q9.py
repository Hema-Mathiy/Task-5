def word_count(str_var):
    # Spliting the string into words using whitespace
    words = str_var.split()
    # Returning the count of words
    return len(words)

# Example usage:
str = "takes a string and returns the number of words"
# Counting the number of words in the input string
result = word_count(str)
# Printing the result
print(str)
print(f"Number of words is: {result}")
