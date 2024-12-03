import re
res=0
enable=True
while True:
  try:
    inputs=input().strip()
    for word in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",inputs):
      if(word=="do()"):
        enable=True
      elif(word=="don't()"):
        enable=False
      else:
        if(enable):
          x,y=map(int,word[4:-1].split(','))
          res+=x*y
  except EOFError:
    break
print(res)  
