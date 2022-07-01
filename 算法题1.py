def solve(s1, s2):
    # 初始化dp数组为全 0 ,共len(s1)+1行, len(s2)+1列.
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    maxlen = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > maxlen:
                    maxlen = dp[i + 1][j + 1]
                    p = i + 1
    #
    # for i in range(len(s1) + 1):
    #     for j in range(len(s2) + 1):
    #         print(dp[i][j], end=' ')
    #     print()

    return s1[p - maxlen:p], maxlen  # 返回最长子串及其长度


if __name__ == "__main__":
    print(solve('baabcdadabc', 'abcdkkk'))
