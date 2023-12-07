def count_digit_one(n):
    count = 0
    factor = 1
    i = 1

    while i <= n:
        divisor = i * 10
        count += (n // divisor) * i + min(max(n % divisor - i + 1, 0), i)
        i *= 10

    return count

# Take input from the user
n = int(input("n= "))

# Check if the input is within the specified constraints
if 0 <= n <= 109:
    # Call the function with user input
    result = count_digit_one(n)
    print(result)
else:
    print("Invalid input. Please enter a value within the specified constraints.")
