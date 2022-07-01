print("请输入m,n(用空格隔开)：")
m, n = map(int, input().split())
print("接下来请输入n组数据，每行分别为a[i]和b[i](用空格隔开)：")
set = [[0, 0] for _ in range(m)]
a_i = []
b_i = []
for i in range(n):
    a, b = map(int, input().split())
    a_i.append(a)
    b_i.append(b)

# 假设每个人都不需要等待，那么每个人呆在银行的时间区间应该是[ai,(ai+bi)]
c_i = [[a_i[i], a_i[i] + b_i[i]] for i in range(len(a_i))]

total_wait_time = 0  # 所有客户一共要等待的时长

for i in range(n):

    if 1 == 1:  # 调试模式
        print(f"第{i+1}个顾客在第{a_i[i]}分钟进入银行")
        print(f"当前柜台情况：{set}")


    temp = []  # 创建一个临时数组，用来寻找当前最快完成业务的柜台

    for j in set:  # 遍历每个柜台, 找出最快完成的柜台
        temp.append(j[1])  # 把当前每一个柜台的完成时间存入

    finish_clock = min(temp)  # 最快完成的柜台
    min_index = temp.index(finish_clock)  # 找出一个离现在最快完成的柜台的索引（就是柜台编号）

    if 1 == 1:
        print(f"当前{min_index}号柜台最快")

    if a_i[i] >= finish_clock:  # 如果这个人是刚好在上一个人完成的时候到达（对应=号）和迟于上一个人完成的时候到达，也就是柜台空闲的时候到达（对应于>号）
        set[min_index][0], set[min_index][1] = c_i[i][0], c_i[i][1]  # 那么就更新柜台的占用时间为ci
        print("无需等待")
    else:  # 如果是到达银行，还没有空闲的柜台，则等待最快完成的柜台，并将等待时间记录到total_wait_time
        wait_time = finish_clock - a_i[i]  # 计算你到达银行后 还要等多久 上一个人才办完业务
        print(f"需等待{wait_time}")
        total_wait_time += wait_time  # 加入等待总时长
        set[min_index][0], set[min_index][1] = c_i[i][0]+wait_time, c_i[i][1]+wait_time

    print(f"总计等待时长{total_wait_time}")
    print("-----------------------------------------------")


print(f"平均等待时长为:{total_wait_time/n}分钟")

# 测试样例：
# 2 4
# 1 2
# 2 4
# 2 5
# 3 4