import random
import random
lower='abcdefghijklmnopqrstuvwxyz'
UPPER='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number='1234567890'
symbol='!@#$%^&*()<>?{}'

all=lower+UPPER+number+symbol
length=9

password=''.join(random.sample(all, length))
print("The generator password is:", password)
