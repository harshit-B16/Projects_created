# arr = [1,2,3,4,5,6,7,8]
# # arr.reverse()
# # print(arr)
# print(arr[::-1])


def reverseArray(arr,n):
    for i in range(2,n):
        if i % 2 == 0:
            print(arr[i])

arr = [2,1,3,4,5,10,6,1,33,11,23]
n = len(arr)
ans = reverseArray(arr,n)
    
