
num = int(input("enter a number: "))
 
fac = 1
i = 1
 
while (i <= num):
    fac = fac * i
    #print (fac)
    i = i + 1
    #print(i)
 
print("factorial of ", num, " is ", fac)


#factorial program using opps
class factorial:
    num=int(input('enter the number: '))
    def facto(self):
        fact=1
        for i in range(self.num,0,-1):
            fact=fact*i
        print(fact)
obj=factorial()
obj.facto()

#number passing arguments
class factorial:

    def facto(self,a):
        self.num=a
        fact=1
        for i in range(1,self.num+1):
            fact=fact*i
        print(fact)
obj=factorial()
obj.facto(5)

