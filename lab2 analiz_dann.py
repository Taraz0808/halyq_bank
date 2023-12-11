# a=1
# b=2
# if a>b:
#     print(a)
# else:
#     print(b)
#
#
#
#
# year = int(input())
#
# if year < 30000 and year > 0:
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")
#
#
#
#
#
# a = int(input())
# b = int(input())
#
# for i in range(a, b+1):
#     if i % 2 == 0:
#         print(i, end=" ")
#
#
#
# N = int(input())
#
# for i in range(1, N):
#     if i**2 <= N:
#         print(i**2, end=" ")
#
#
#
#
#
# N = int(input())
#
# sum = 0
# while N > 0:
#     sum += N % 10
#     N //= 10
#
# print(sum)
#
#
#
#
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# if N < 100 and N > 0:
#     for i in range(0, N, 2):
#         print(arr[i], end=" ")
# else:
#     print("Error")
#
#
#
#
#
# arr = list(map(int, input().split()))
#
# for i in range(0, len(arr), 2):
#     print(arr[i], end=" ")
#
#
#
#
#
# N = int(input())
#
# fact = 1
# for i in range(1, N+1):
#     fact *= i
#
# print(fact)