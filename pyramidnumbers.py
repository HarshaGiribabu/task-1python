def number_pyramid(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            if num > n:
                break
            print(num, end=" ")
            num += 1
        print()

number_pyramid(20)
