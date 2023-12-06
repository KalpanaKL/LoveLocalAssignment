def length_of_last_word(s):
    # Remove trailing spaces and split the string into words
    words = s.rstrip().split()

    # Return the length of the last word
    return len(words[-1])

# Example usage:
s = "   fly me   to   the moon  "
result = length_of_last_word(s)
print(result)
