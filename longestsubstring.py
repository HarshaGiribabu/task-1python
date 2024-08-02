def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    longest = 0
    end = 0
    length_table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                length_table[i][j] = length_table[i - 1][j - 1] + 1
                if length_table[i][j] > longest:
                    longest = length_table[i][j]
                    end = i

    return s1[end - longest: end]

s1 = "abcde"
s2 = "abfde"
result = longest_common_substring(s1, s2)
print("Longest common substring:", result)
