alist=[]
blist=[]
while True:
  try:
    inputs=list(map(int,input().split()))
    alist.append(inputs[0])
    blist.append(inputs[1])
  except EOFError:
    break
result=0
for i in range(len(alist)):
  result+=alist[i]*blist.count(alist[i])
print(result)  
