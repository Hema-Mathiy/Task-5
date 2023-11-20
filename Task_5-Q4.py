def count_ofunique_characters(input_string):

    unique_characters = set()
    for char in input_string:
        unique_characters.add(char)
    return len(unique_characters)

str = input("Enter value: ")
result = count_ofunique_characters(str)
print(f"The number of unique characters in '{str}' is: {result}")