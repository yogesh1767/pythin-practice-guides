l=[1,5,3,4,2,4,7,55,67,3,34,3,4]
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)
    
#another way..

a='asdfvdfhy'
for i in a :
    if not a.count(i)>1:
        print(i,end='')
