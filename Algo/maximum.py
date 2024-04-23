import time

tab = [1,2,3,4,5,6,7,8,7,8,9,7,1,8,7,8,9,7,18,19,20,1,2,3,4,5,6,7,8,7,8,9,7,18,19,20,1,2,3,4,5,6,7,8,9,10,11,8,9,10,118,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,20]
print(len(tab))
maxi = tab[0]
start = time.time_ns()
i=1
while i<len(tab):
  if tab[i]>maxi:
    maxi=tab[i]
  i=i+1

print(time.time_ns() - start)