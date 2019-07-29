import re

open_CDS = open('CDS.fasta')
seq = {}
for line in open_CDS:
    if line.startswith('Parent='):
        name = line.replace('\n','').split()[0]
        seq[name] = ''
    else:
        seq[name] += line.replace('\n','').strip()

translating_dict = {}        
key=''
for name in seq:
    key = name
    list_mRNA=[]
    translating = ''
    translating = str(seq[name])
    translating = translating.replace('A','{A}').replace('T','{T}').replace('C','{C}').replace('G','{G}')
    translating = translating.format(A='U',T='A',C='G',G='C')
    for W in range(0,len(translating),3):
        uncoden = ''
        uncoden += translating[W:W+3]
        list_mRNA.append(uncoden)
    translating_dict[key] = list_mRNA

Translated_seq = open('Translated.fasta','w')
code_dict = {'GUU':'G','GGC':'G','GGA':'G','GGG':'G','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GUU':'V','GUC':'V','GUA':'V','GUG':'V','CUU':'L','CUC':'L','CUA':'L','CUG':'L','UUA':'L','UUG':'L','AUU':'I','AUC':'I','AUA':'I','CCU':'P','CCA':'P','CCG':'P','CCC':'P','UUU':'F','UUC':'F','UAU':'Y','UAC':'Y','UGG':'W','UCU':'S','UCA':'S','UCC':'S','UCG':'S','AUG':'S','AGC':'S','ACU':'T','ACC':'T','ACG':'T','ACA':'T','UGU':'C','UGC':'C','AUG':'M','AAU':'N','AAC':'N','CAA':'Q','CAG':'Q','GAU':'D','GAC':'D','GAA':'E','GAG':'E','AAA':'K','AAG':'K','CGU':'R','CGC':'R','CGG':'R','CGA':'R','AGA':'R','AGG':'R','CAU':'H','CAC':'H','N\w\w':'X','\wN\w':'X','\w\wN':'X'}

for key in translating_dict:
    translated = []
    translated_str = ''
    for i in range(len(translating_dict[key])):
        for code in code_dict:
            if code == translating_dict[key][i]:
                translated.append(code_dict[code])
    translated_str = ''.join(translated)
    Translated_seq.write(key+'\n')
    Translated_seq.write(translated_str+'\n')

Translated_seq.close()
open_CDS.close()
        
        



