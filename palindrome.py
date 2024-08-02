def is_palindrome(string):
    return string == string[::-1]

string = "malayalam"
result = is_palindrome(string)
print("Is palindrome:", result)
