IF={}
SIF={}
Name=''

f=open('plum_0630.scafSeq.FG')

seq={}
for line in f:
    if line.startswith('>'):
         name=line.replace('\n','').split()[0]
         seq[name]=''
    else:
        seq[name]+=line.replace('\n','').strip()
                         

exc = open('result.txt',"w")
exc.write("name"+"\t"+"total length"+"\t"+"efective length"+"\t"+"N length"+"\t"+"GC length"+"\t"+"GC rate"+"\n")
for i in seq:
    Name=i
    TL=0
    EL=0
    NL=0
    GCL=0
    GCR=0
    dna_dic = {'A':0,'G':0,'C':0,'T':0,'N':0}
    for j in seq[i]:
        dna_dic[j] += 1
        
    TL += dna_dic[j]
        EL = TL-dna_dic['N']
        NL = dna_dic['N']        
        GCL = dna_dic['G']+dna_dic['C']
        GCR = GCL/TL
        IF[Name] = TL
    exc.write(i+"\t"+str(TL)+"\t"+str(EL)+"\t"+str(NL)+"\t"+str(GCL)+"\t"+str(GCR)+"\n")

exc.close()

import operator
sorted_IF=sorted(IF.items(),key=operator.itemgetter(1),reverse=True)
SIF=dict(sorted_IF)
print(SIF)

X=0
Y=0
Q=0
W=0
E=0
R=0

for n in SIF:
    X += SIF[n]
print(X)

Q=int(X*(0.48))
W=int(X*(0.50))
E=int(X*(0.89))
R=int(X*(0.91))
for n in SIF:
    Y += SIF[n]
    if Y in range(Q,W):
        print('N50 is'+"\t"+n+"\t"+str(SIF[n]))
    elif Y in range(E,R):
         print('N90 is'+"\t"+n+"\t"+str(SIF[n]))


          
        



