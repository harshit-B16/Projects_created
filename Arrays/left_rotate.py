def leftRotate(arr,n):
    for i in range(n):
        first = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]
                
        arr[len(arr)-1] = first

    return arr

def rightRotate(arr,n):
    for i in range(n):
        last = arr[len(arr)-1]
        for j in range(len(arr)-1,-1,-1):
            arr [j] = arr[j-1]
        
        arr[0] = last

    return arr

arr = [1,2,3,4,5] #  [5,1,2,3,4]
n = 1
ans1 = leftRotate(arr,n)
ans2 = rightRotate(arr,n)
print("array elements after left rotation by 1 :", ans1)
print("array elements after right rotation by 1 :", ans2)
