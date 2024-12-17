def palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]


result = palindrome(123321)
print("The number is a palindrome", result)
