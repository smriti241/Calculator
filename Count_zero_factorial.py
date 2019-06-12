T = int(input())
for i in range(T):
    N = int(input())
    m = 1
    count = 0
    while N >= 1:
        m = int(m * N)
        N -= 1
    print(m)
    while m != 0:
        if m % 10 == 0:
            count += 1
        m = m/10
    print(count)
