def most_frequent_char(string):
    from collections import Counter
    count = Counter(string)
    most_common = count.most_common(1)
    return most_common[0][0]

string = "Guvi Geeks NetWork Private Limited"
result = most_frequent_char(string)
print("Most frequent character:", result)
