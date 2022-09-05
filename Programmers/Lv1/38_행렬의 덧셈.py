def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = arr1[i][j] + arr2[i][j]
    return arr