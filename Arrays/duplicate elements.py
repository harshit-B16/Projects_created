# def find_first_duplicate(arr, n):
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] == arr[j]:
#                 return arr[i]

# arr = [1, 2, 3, 3, 2, 4, 1, 5, 5, 5, 6, 3]
# n = len(arr)
# ans = find_first_duplicate(arr, n)
# print("The first duplicate element is:", ans)


def find_duplicates_method1(arr):
    duplicates = []
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
                count += 1
    #print(count)
    return duplicates


my_array = [1, 2, 3, 4, 2, 5, 6, 4, 2, 4, 7]
print("Method 1 - Duplicate elements:", find_duplicates_method1(my_array))
