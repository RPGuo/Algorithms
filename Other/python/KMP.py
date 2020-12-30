def kmp(pat):
    dp = [[0 for _ in range(256)] for _ in range(len(pat))]
    dp[0][ord(pat[0])] = 1
    x = 0
    for j in range(1, len(pat)):
        for c in range(0, 256):
            dp[j][c] = dp[x][c]
        dp[j][ord(pat[j])] = j + 1
        x = dp[x][ord(pat[j])]
    return dp


def kmp_search(txt, pat):
    dp = kmp(pat)
    j = 0
    m = len(pat)
    n = len(txt)
    for i in range(n):
        j = dp[j][ord(txt[i])]
        if j == m:
            return i - m + 1
    return -1


if __name__ == '__main__':
    print(kmp_search('ababc', 'abc'))


