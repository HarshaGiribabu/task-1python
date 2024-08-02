def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])

string = "Guvi Geeks NetWork Private Limited"
new_string = remove_vowels(string)
print("String without vowels:", new_string)
