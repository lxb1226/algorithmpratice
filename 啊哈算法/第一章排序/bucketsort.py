
def bucket_sort(N,M):
    # 桶排序 简易版
    # 其本质是将数字放到一个桶里面标记起来
    # 所以要对0~1000以内的数字排序，就需要1000+1个桶。
    # 参数N代表要排序数的最大值，M代表着要排序的数的个数
    # 时间复杂度: O(N+M)
    # 空间复杂度：N
    # 缺点：空间复杂度高，浪费空间，且无法知道排序后对应的序号

    a = [0 for _ in range(N+1)]
    for i in range(1,M):
        t = input('请输入一个数字：')
        a[int(t)] += 1
    
    # 从小到大输出
    for i in range(N):
        for _ in range(1,a[i]+1):
            print(i)

    # 从大到小输出
    # for i in range(N,-1,-1):
    #     for _ in range(1,a[i]+1):
    #         print(i)


if __name__ == "__main__":
    N = 1001
    M = 10
    bucket_sort(N,M)


