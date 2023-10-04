def _copy(arr, n):
    new_arr = []
    for i in range(n):
        new_arr.append(arr[i])
    
    return new_arr

arr = [1, 2, 3, 4, 5]
n = len(arr)
ans = _copy(arr, n)
print(ans)
