def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = "listen"
s2 = "silent"
result = is_anagram(s1, s2)
print("Is anagram:", result)
