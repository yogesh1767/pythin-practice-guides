s='United States'

x={i:s.count(i) for i in s}
print(x)

#another program
a={i:('even' if i%2==0 else 'odd')  for i in range(1,11)}
print(a)
