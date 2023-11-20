def pyramid_of_stars(num):
    for i in range(num):
        print(" " * (num - i - 1), end="")
        for j in range(i + 1):
            print(j + 1, end=" ")

        print("\n")
num = input("Enter number: ")
num = int(num)

pyramid_of_stars(num)