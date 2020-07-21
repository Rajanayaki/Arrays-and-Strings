def transpose(mat,row,col):
  for i in range(row):
    for j in range(i,col):
      t=mat[i][j]
      mat[i][j]=mat[j][i]
      mat[j][i]=t

def reverse(mat,col):
  for i in range(col):
    j=0
    k=col-1
    while j<k:
      t=mat[j][i]
      mat[j][i]=mat[k][i]
      mat[k][i]=t
      j+=1
      k-=1

def printmatrix(mat,row,col):
  for i in range(row):
    for j in range(col):
      print(mat[i][j],end=" ")
    print(" ")

def rotate(mat,row,col):
  transpose(mat,row,col)
  reverse(mat,col)
  
row=int(input())
col=int(input())
mat=[]
for i in range(row):
  mat.append(list(map(int,input().split())))
rotate(mat,row,col)
printmatrix(mat,row,col)
