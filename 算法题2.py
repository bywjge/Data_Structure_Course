def solve():  # 求解算法
    ans = []
    for i in range(1, n + 1):
        if visited[i] == 0:
            cnt = dfs(G, i)
            if cnt > 1:
                ans.append(cnt)  # 人数多于1的计一个朋友圈
    ans.sort()
    return ans


def dfs(G, v):  # 邻接表G中从顶点v出发的深度优先遍历
    cnt = 1  # 访问顶点v
    visited[v] = 1  # 置已访问标记
    if G[v] is None:
        return cnt  # v没有朋友时返回
    for j in range(len(G[v])):  # 处理顶点v的所有出边顶点j
        w = G[v][j]  # 取顶点v的一个相邻点w
        if visited[w] == 0:
            cnt += dfs(G, w)  # 若w顶点未访问,递归访问它
    return cnt


if __name__ == "__main__":

    n, m = map(int, input().split())  # 转换为整数序列
    G = [None] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        if G[a] is None:
            G[a] = []
        if G[b] is None:
            G[b] = []
        G[a].append(b)  # 互为朋友，所以要互相加
        G[b].append(a)  # 同上
    visited = [0] * (n + 1)  # 记录是否已访问
    ans = solve()
    print(f"共有{len(ans)}个朋友圈")
    print(f"各朋友圈人数:{ans}")
