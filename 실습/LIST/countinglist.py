def counting_sort(arr):
    k = max(arr)
    counts = [0] * (k + 1)
    result = [0] * len(arr)
    for ele in arr:
        counts[ele] += 1
    for idx in range(len(counts) - 1):
        counts[idx + 1] += counts[idx]
    for idx in range(len(arr) - 1, -1, -1):
        counts[idx] -= 1
        result[counts[arr[idx]]] = arr[idx]