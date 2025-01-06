def palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]


print("The number is a palindrome", palindrome(123321))
