def largestNo(arr,n):
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max


def SmallestNo(arr,n):
    min = arr[0]
    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    return min


arr = [12,34,23,-16,10]
n = len(arr)
print("largest element in an Array is : " , largestNo(arr,n))
print("Smallest element in an Array is : " , SmallestNo(arr,n))