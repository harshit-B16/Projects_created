def rightRotate(arr,n):
    for i in range(n):
        last = arr[len(arr)-1]
        for j in range(len(arr)-1,-1,-1):
            arr [j] = arr[j-1]
        
        arr[0] = last

    return arr

arr = [1,2,3,4,5]
n= 2
ans = rightRotate(arr,n)
print("array elements after right rotation by 1 :", ans)




