def count_vowels(string):
    vowels = "aeiouAEIOU"
    total_vowels = 0
    vowel_counts = {vowel: 0 for vowel in vowels}

    for char in string:
        if char in vowels:
            total_vowels += 1
            vowel_counts[char] += 1

    return total_vowels, vowel_counts


string = "Guvi Geeks NetWork Private Limited"
total_vowels, vowel_counts = count_vowels(string)
print("Total vowels:", total_vowels)
print("Count of each vowel:", vowel_counts)
