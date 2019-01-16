
def quick_sort(left,right):
    # 快速排序
    # 从初始序列两端开始探测，先从右往左找比基准数小的数，再从左往右找比基准数大的数，然后交换它们，当i=j时，第一轮探测结束，交换基准数和位置i的数
    # 此时基准数的左边都比基准数小，基准数的右边都比基准数大
    # 接下来递归基准数的左边和右边
    # 时间复杂度： O(Nlog(N))

    if left > right:
        return
    
    temp = a[left]
    i = left
    j = right
    while i != j:
        while a[j] >= temp and i < j:
            j -= 1
        while a[i] <= temp and i < j:
            i += 1
        if i < j:
            a[i], a[j] = a[j], a[i]
        
    a[left] = a[i]
    a[i] = temp

    quick_sort(left,i-1)
    quick_sort(i+1,right)

if __name__ == "__main__":
    n = int(input("请输入你要排序序列的个数："))
    a = [int(x) for x in input("").split(' ')]
    quick_sort(0,n-1)
    for x in a:
        print(x, end=' ')


