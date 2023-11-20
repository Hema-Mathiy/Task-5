print("New String with all VOWELS removed")
str = input("Enter a string: ")
vowels = "aeiouAEIOU"
for value in str:
    if value in vowels:
        str = str.replace(value,"")
    print("Output", str)




