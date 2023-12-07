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
"""
LOGIC:
1.Set the variables count, factor, and i to their default values.
2.The while loop continues until i is less than or equal to n.
3.Calculate the divisor, which is i multiplied by 10, in each iteration.
4.Use the following formula to update the count:
   count += (n% divisor - i + 1, 0), i + min(max(n% divisor - i + 1, 0), i)
  (n // divisor) * i counts the number of occurrences of'1' contributed by i multiples up to n.
  min(max(n% divisor - i + 1, 0), i) counts the occurrences of '1' after the multiples of i in the remainder part of n.
5.To get to the next digit, multiply i by 10.

ALGORITM:
1.In each iteration, begin with the least significant digit (units place) and progress to higher digits.
2.The loop iterates through each digit position, counting the number of occurrences of '1' in that position.
3.The formula calculates the count quickly by taking into account both multiples of i and the remainder part of n.
4.By multiplying i by 10, you can advance to the next digit position.
5.Repeat until all digit places have been taken into account.
6.Return the total number of occurrences of the character '1'.
   The time complexity of this algorithm is O(log n), making it efficient for large values of n.
"""
