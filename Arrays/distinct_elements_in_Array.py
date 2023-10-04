# def distinctElements(arr, n):
#     distinct_list = []  # Initialize a list to store distinct elements
#     for i in range(n):
#         d = 0
#         for j in range(0, i):
#             if arr[i] == arr[j]:
#                 d = 1
#                 break

#         if d == 0:
#             distinct_list.append(arr[i])  # Append the distinct element to the list
#     return distinct_list

# arr = [1, 2, 3, 4, 5, 6, 3]
# n = len(arr)
# distinct_elements = distinctElements(arr, n)

# print("Distinct elements:", distinct_elements)


###### simple approach

def Unique(arr):
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    
    return list

arr = [1, 2, 3, 4, 5, 6, 3, 4, 12, 10, 3, 67]
ans = Unique(arr)
print("Unique elements :",ans)
