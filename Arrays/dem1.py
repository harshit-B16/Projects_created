
# def splitArr(arr, n, k):
#     for i in range(0, k):
#         x = arr[0]
#         print(x,"",end='')
#         for j in range(0, n-1):
#             arr[j] = arr[j + 1]
 
#         arr[n-1] = x
 
 
# # main
# arr = [12, 10, 5, 6, 52, 36]
# n = len(arr)
# position = 2
 
# splitArr(arr, n, position)


def Odd_numbers(n):
    count = 0
    while count < 10:
        if n %2!= 0:
            print(n)
            count += 1
        n += 1

n = 32
ans = Odd_numbers(n)
    