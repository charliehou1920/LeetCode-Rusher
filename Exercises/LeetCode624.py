'''
给定m个数组,每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数(每个数组选一个)并且计算它们的距离。两个整数a和b之间的距离定义为它们差的绝对值|a-b|。你的任务就是去找到最大距离
'''
def maxDistance(arrays):
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    max_distance = 0

    for i in range(1, len(arrays)):
        current_min = arrays[i][0]
        current_max = arrays[i][-1]
        max_distance = max(max_distance, abs(current_min - max_val), abs(current_max - min_val))
        min_val = min(min_val, current_min)
        max_val = max(max_val, current_max)

    return max_distance

def main():
    arr = [[0,1],[1,2,3],[4,5,6],[1,2,3]]
    distance = maxDistance(arr)
    print("The Maximum Distance is: ", distance)

if __name__ == "__main__":
    main()


