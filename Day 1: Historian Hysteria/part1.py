alist=[]
blist=[]
while True:
  try:
    inputs=list(map(int,input().split()))
    alist.append(inputs[0])
    blist.append(inputs[1])
  except EOFError:
    break
alist.sort()
blist.sort()
result=0

for i in range(len(alist)):
  res=alist[i]-blist[i]
  if(res<0):
    res*=-1
  result+=res 
  res=0
print(result)
