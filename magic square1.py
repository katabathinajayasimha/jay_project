
"""
created on monday , 17 aug 2026
@author: katabathina jayasimha
"""


def zeroes(n):
    matrix0=[]
    for m in range(n):
        l=[]
        for w in range(n):
            l.append(0)
        matrix0.append(l)
    # printing(matrix0)
    count=1
    length=n*n
    i,j=n//2,n-1
    # print(i,j)

    while count<=length:
        if i==-1 and j==n:
            i,j= 0,n-2
        else:
            if j==n:
                j = 0
            if i<0:
                i = n-1

        if (matrix0[i][j] != 0):
            i = i+1
            j = j-2
            continue
        else:
            matrix0[i][j] = count
            count+=1
        i=i-1
        j=j+1
    printing(matrix0)
def printing(matrix1):

    for p in range(n):
        j=0
        for j in range(n):
            print(matrix1[p][j],end=" ")
        print()

        

n= int(input("enter the odd number only:"))
if n%2==0:
    raise ValueError("give only odd numbers")
zeroes(n)