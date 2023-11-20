def longest_common_substring(str1, str2):
    # Getting the lengths of the input strings
    m, n = len(str1), len(str2)
    # Creating an array to store the lengths of common substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len, end_index = 0, 0

    # Loop through each character in both strings.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Checking if the characters match
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Checking if the current length is greater than the max_len
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    return str1[end_index - max_len + 1: end_index + 1]

# Example usage:
str1 = "Potato"
str2 = "Tomato"
result = longest_common_substring(str1, str2)
print(f"The longest common substring between '{str1}' and '{str2}' is: {result}")
