class factorial:
    num=int(input('enter the number: '))
    def facto(self):
        fact=1
        for i in range(self.num,0,-1):
            fact=fact*i
        print(fact)
obj=factorial()
obj.facto()