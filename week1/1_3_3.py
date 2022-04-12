def cnk(n, k):
    if k == 0 or k == n:
        return 1
    elif k > n:
        return 0
    else:
        return cnk(n - 1, k) + cnk(n - 1, k - 1)


n, k = map(int, input().split())
print(cnk(n, k))
