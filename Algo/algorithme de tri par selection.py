t=[9,7,2,3,6,1,5]

i=0
min=0
j=0

i=1
while i<len(t):
    j=i+1
    min=i
    while j<=len(t):
        if t[j]<t[min]:
            min=j
        else:
            j=j+1
    if min != i:
        t[i], t[min] = t[min], t[i]
    else:
        i=i+1

print(t)