def selection_sort(a, N):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx] , a[i]
    return a
arr = [5, 1, 3, 2, 4]
n = len(arr)

result = selection_sort(arr, n)
print(result)