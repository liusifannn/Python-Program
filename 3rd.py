list1=[]
list2=[]
f=open('plum_0630.scafSeq.FG')
ls=[]
for line in f:
    if not line.startswith('>'):
        ls.append(line.replace('\n',''))
Q=str(ls)

for i in range(0,len(Q),250):
    q=''
    q=Q[i:i+250]
    U=0
    for j in range(len(q)):
        if q[j]=='G' or q[j]=='C':
             U += 1
    list1.append(U)
print(list1)

P=[]
for i in range(len(list1)):
    P.append(int((list1[i]/250)*100))
    
    
   
list2.append(P.count(0))
list2.append(P.count(1)) 
list2.append(P.count(2))
list2.append(P.count(3))
list2.append(P.count(4))
list2.append(P.count(5))
list2.append(P.count(6))
list2.append(P.count(7))
list2.append(P.count(8))
list2.append(P.count(9))
list2.append(P.count(10))
list2.append(P.count(11))
list2.append(P.count(12))
list2.append(P.count(13))
list2.append(P.count(14))
list2.append(P.count(15))             
list2.append(P.count(16))
list2.append(P.count(17))
list2.append(P.count(18))
list2.append(P.count(19))
list2.append(P.count(20))
list2.append(P.count(21))
list2.append(P.count(22))
list2.append(P.count(23))
list2.append(P.count(24))
list2.append(P.count(25))
list2.append(P.count(26))
list2.append(P.count(27))
list2.append(P.count(28))
list2.append(P.count(29))
list2.append(P.count(30))
list2.append(P.count(31))
list2.append(P.count(32))
list2.append(P.count(33))
list2.append(P.count(34))
list2.append(P.count(35))
list2.append(P.count(36))
list2.append(P.count(37))
list2.append(P.count(38))
list2.append(P.count(39))
list2.append(P.count(40))
list2.append(P.count(41))
list2.append(P.count(42))
list2.append(P.count(43))
list2.append(P.count(44))
list2.append(P.count(45))
list2.append(P.count(46))
list2.append(P.count(47))
list2.append(P.count(48))
list2.append(P.count(49))
list2.append(P.count(50))
list2.append(P.count(51))
list2.append(P.count(52))
list2.append(P.count(53))
list2.append(P.count(54))
list2.append(P.count(55))
list2.append(P.count(56))
list2.append(P.count(57))
list2.append(P.count(58))
list2.append(P.count(59))
list2.append(P.count(60))
list2.append(P.count(61))
list2.append(P.count(62))
list2.append(P.count(63))
list2.append(P.count(64))
list2.append(P.count(65))
list2.append(P.count(66))
list2.append(P.count(67))
list2.append(P.count(68))
list2.append(P.count(69))
list2.append(P.count(70))
list2.append(P.count(71))
list2.append(P.count(72))
list2.append(P.count(73))
list2.append(P.count(74))
list2.append(P.count(75))
list2.append(P.count(76))
list2.append(P.count(77))
list2.append(P.count(78))
list2.append(P.count(79))
list2.append(P.count(80))
list2.append(P.count(81))
list2.append(P.count(82))
list2.append(P.count(83))
list2.append(P.count(84))
list2.append(P.count(85))
list2.append(P.count(86))
list2.append(P.count(87))
list2.append(P.count(88))
list2.append(P.count(89))
list2.append(P.count(90))
list2.append(P.count(91))
list2.append(P.count(92))
list2.append(P.count(93))
list2.append(P.count(94))
list2.append(P.count(95))
list2.append(P.count(96))
list2.append(P.count(97))
list2.append(P.count(98))
list2.append(P.count(99))
list2.append(P.count(100))
print(list2)



import numpy as np
import matplotlib.pyplot as plt


plt.title('GC含量分布曲线')
plt.plot(list(range(101)),list2,color='blue')


plt.show()



 






            
