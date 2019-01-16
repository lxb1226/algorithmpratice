
def bubble_sort():
    # 冒泡排序
    # 基本原理：每次比较两个相邻的元素，如果它们的顺序错误就把它们交换过来
    # 时间复杂度： O(N**2)
    # 空间复杂度： O(M)
    # 缺点： 时间复杂度高，目前无法优化


    # 创建一个列表用来存放数字，列表的容量应该大于要排序的数字的个数

    a = [0 for _ in range(100)]
    n = int(input('请输入要排序的数的个数： '))
    # 将数字存放到列表a中
    for i in range(1,n+1):
        a[i] = int(input('请输入数字: '))

    # 冒泡排序
    # 对n个数进行排序，只用进行n-1趟
    for i in range(1,n):
        # 从第1位开始比较直到最后一个尚未归位的数
        for j in range(1,n-i+1):
            # 比较大小，并交换
            # 从大到小排序
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            # # 从小到大排序
            # if a[j] > a[j+1]:
            #     a[j],a[j+1] = a[j+1],a[j]
    # 输出排序后的数字序列
    for i in range(1,n+1):
        print(a[i])



if __name__ == "__main__":
    bubble_sort()


