def SumofArray(arr,n):
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
    return sum

arr = [20,30,20,10,10,5,5]
n = len(arr)
print("Summ of array elements ", SumofArray(arr,n))