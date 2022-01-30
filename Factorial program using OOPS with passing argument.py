class factorial:

    def facto(self,a):
        self.num=a
        fact=1
        for i in range(1,self.num+1):
            fact=fact*i
        print(fact)
obj=factorial()
obj.facto(5)