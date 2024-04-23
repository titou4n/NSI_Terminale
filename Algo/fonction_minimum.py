L=[6,5,9,3,2,7,1]
d = 0
f=len(L)-1

def minimum(L, d, f):
    if d == f:
        return L[d]
    else:
        m=(d+f)//2
        x = minimum(L, d, m)
        y = minimum(L, m+1, f)
        if x < y:
            return x
        else:
            return y

print(minimum(L, d, f))