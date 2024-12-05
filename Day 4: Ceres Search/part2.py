from sys import stdin

arr=[]
for line in stdin
  arr.append(line.strip())

total=0
for i in range(len(arr)):
  for j in range(len(arr)):
    if arr[x][y]=='M':
      if(i+2 <len(arr)  and j+2<len(arr)):
        if(arr[x+1][y+1]=='A' and arr[x+2][y+2]=='S'):
          if((arr[x+2][y]=='S' or arr[x+2][y]=='M') and (arr[x][y+2]=='S' or arr[x][y+2]=='M'):
            total+=1

    if arr[x][y]=='S':
      if(i+2 <len(arr)  and j+2<len(arr)):
        if(arr[x+1][y+1]=='A' and arr[x+2][y+2]=='M'):
          if((arr[x+2][y]=='S' or arr[x+2][y]=='M') and (arr[x][y+2]=='S' or arr[x][y+2]=='M'):
            total+=1
print(total)
