
def is_strictly_monotonic(lst):
    return (all(lst[i] < lst[i+1] for i in range(len(lst) - 1)) or \
           all(lst[i] > lst[i+1] for i in range(len(lst) - 1))) and \
           all(abs(lst[i]-lst[i+1])<=3 for i in range(len(lst)-1))
def find_removing_one(lst):
      for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if(is_strictly_monotonic(new_lst)):
          return True
      return False
  
res=0
while True:
  try:
    inputs=list(map(int,input().split()))
    if(is_strictly_monotonic(inputs)):
      res+=1
    else:
      if(find_removing_one(inputs)):
        res+=1 
  except EOFError:
    break
print(res)  
