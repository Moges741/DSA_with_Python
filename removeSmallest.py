t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()  # sort the array

    possible = True
    for i in range(n - 1):
        if a[i+1] - a[i] > 1:
            possible = False
            break

    print("YES" if possible else "NO")
