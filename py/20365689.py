b=[]
for a in range(1,10):
    for s in str(a):
        print(s)
    a+=1
    #b=[]
    if a<11:
        b.append(a)
print(b)