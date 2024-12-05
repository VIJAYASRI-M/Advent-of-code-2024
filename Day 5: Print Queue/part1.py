from sys import stdin
import functools

def day5(s):
  p1, p2 = s.split('\n\n') # p1['47|53\n97|13']  p2[75,47,61,53\n97,61]
  rules = [tuple(line.split('|')) for line in p1.splitlines()] # [('47,'53),('97','13')]
  updates = (line.split(',') for line in p2.splitlines()) #(['75', '47', '61', '53', '29'])


  def compare(a, b):
    return -1 if (a, b) in rules else 1 if (b, a) in rules else 0

  total = 0
  for update in updates:
    new = sorted(update, key=functools.cmp_to_key(compare))
    if (new == update): 
      total += int(new[len(new) // 2])

  return total
  
arr=stdin
print(day5(arr.read()))
