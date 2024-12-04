from sys import stdin

arr=[]
for line in stdin
  arr.append(line.strip())

total=0
directions=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

for i in range(len(arr)):
  for j in range(len(arr)):
    for dx,dy in dirs:
      if( 0<= [i+ 3*dx] <len(arr) and 0<= [j+ 3*dy] <len(arr)):
        if arr[i][j]=="X" and arr[i+dx][j+dy]=="M" and arr[i+ 2*dx][j+ 2*dy]=="A" and arr[i+ 3*dx][j+ 3*dy]=="S":
          total+=1
print(total)
        
