l=[[1,3,5], [77,5.4,9,0], [2,11,22]]
for i in l:
    for j in i:
        print(j)

#another way
l=[[1,3,5], [77,5.4,9,0], [2,11,22]]
a=[]
for i in l:
    for j in i:
        a.append(j)
print(a)

