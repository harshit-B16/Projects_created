
def Frequency(arr):
    dict = {}
    for i in arr:
        print(i)
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict

arr = [2,3,4,2,8,7,8]
ans = Frequency(arr)
print(ans)



### ek dum simple approach

# a = [1,2,8,2,4,2,7]
# count = {}
# for i in a:
#     if i in count:
#         count[i]+= 1
#     else:
#         count[i]= 1
    
# print(count)





#### Using list variable
# def countFreq(arr, n):
     
#     # Mark all array elements as not visited
#     visited = [False for i in range(n)]
 
#     # Traverse through array elements
#     # and count frequencies
#     for i in range(n):
         
#         # Skip this element if already
#         # processed
    
#         if (visited[i] == True):
#             continue
 
#         # Count frequency
#         count = 1
#         for j in range(i + 1, n, 1):
#             if (arr[i] == arr[j]):
#                 visited[j] = True
#                 count += 1
         
#         print(arr[i], count)

# arr = [10, 20, 20, 10,20]
# n = len(arr)
# countFreq(arr, n)




















