def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return middle
        elif a[middle] > key: # 찾는 값보다 크면
            end = middle - 1 # 왼쪽 구간 선택
        else: # 찾는 값보다 작으면
            start = middle + 1 # 오른쪽 구간 선택
    return -1 # 검색 실패

arr = [1, 2, 3, 4, 5]
n = len(arr)
print("key:", binarySearch(arr, n, 4))