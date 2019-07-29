import re

seq={}
IFM={}
q=[]
f = open('plum_0630.scafSeq.FG')
g = open('Prunus_mume_scaffold.gff')

for line in f:
    if line.startswith('>'):
         name = line.replace('\n','').split()[0]
         seq[name] = ''
    else:
        seq[name] += line.replace('\n','').strip()

G={}
F={}
for line in g:
    list1 = line.strip('\n').split()
    type1 = list1[2]
    if type1 == 'mRNA':
        P=''
        O=''
    elif type1 == 'CDS':
        chr=str('>'+list1[0])
        startpoint=int(list1[3])
        endpoint=int(list1[4])
        direction=list1[6]
        key =str(list1[8])
        if direction == '+':
            P += seq[chr][startpoint-1:endpoint]
            G[key] = P
        else:
            O += seq[chr][startpoint-1:endpoint]
            F[key] = O

list2=[]
str2=''
s=''
for line in F:
    line.rstrip('\n')
    list2=list(reversed(F[line]))
    s = ''.join(list2)
    s = s.replace('A','{A}').replace('T','{T}').replace('C','{C}').replace('G','{G}')
    s = s.format(A='T',T='A',C='G',G='C')

    G[line] = s
    
CDS = open('CDS.fasta','w')
for key in sorted(G.keys()):
    R = ''
    CDS.write(key+'\n')
    for j in range(0,len(G[key]),50):
        R=G[key][j:j+50]
        CDS.write(R+'\n')

g.close()
f.close()
CDS.close()





    

            
            


    

    
            
