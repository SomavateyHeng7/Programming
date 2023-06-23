# # # for i in range(7,-2,-9):
# # #     for j in range(-2):
# # #         print(j)

# # for i in range(4,7):
# #     i = i+ 3
# #     print('Hello')

# x = 1234
# while x % 10:
#     x = x//10
#     print(x)

# n = 11
# for i in range(2,n//2):
#     if n%i!=0:
#         print("P")
#         break
#     else:
#     	print("bye")

# n = 10   
# for i in range(n):
#     if n == 5:
#         break
#         print("P")
# print(n)

# for i in range(5):
#     for j in range(i):
#         i = i+j
#         print(i , end = '@')
# print(j)

# s = 0
# for i in range(-5,5):
#     s = s+i
# print(s)

# L = [13,12,21,16,35,7,4]
# s = 5
# s1 = 3
# for i in L:
#     if (i%4==0):
#         s = s+i
#         continue
#     if(i%7==0):
#         s1 = s1+i
# print(s,end=' ')
# print(s1)

# def Display(str):
#     m=""
#     for i in range(0,len(str)):
#         if(str[i].isupper()):
#             m=m+str[i].lower()
#         elif str[i].islower():
#             m=m+str[i].upper()
#         else:
#             if i%2==0:
#                 m=m+str[i-1]
#             else:
#                 m=m+"#"
#     print(m)
# Display('Fun@Python3.0')

strList = ['Toyota', 'Onepiece', 'Ebola']
for i in strList:
    vCount = 0
    aCount = 0
    for j in range(len(strList)):
        if str(j) in 'aieou':
            vCount += 1
        else:
            aCount += 1
print(f'vCount = {vCount}')
print(f'aCount = {aCount}')