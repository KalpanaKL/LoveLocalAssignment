def last_word_length(s):
    # Remove double quotes and split the string into words
    words = s.strip('"').split()

    # Return the length of the last word
    return len(words[-1])

# Read input from the user directly within the input function
result =last_word_length(input('s= '))

# Display the result
print(result)
"""
Logic:
1.Remove Double Quotes: The function strip('"') removes double quotes from the beginning and end of the input string s. This ensures that the double quotation marks are not regarded as part of the words.
2.Split Into Words: The string is split into words using split(), which is then applied without double quotes. This function converts a string to a list of words. It divides the string into substrings (words) by spaces.
3.Return the length of the last word in the list of words obtained after stripping double quotes and splitting. words[-1] refers to the list's final element, which is the last word.

Algorithm:
1.Remove all double quotation marks from the input string.
2.Make a list of the words from the string.
3.If there are multiple words in the list, go to the last one.
4.Return the length of the previous word.
"""
