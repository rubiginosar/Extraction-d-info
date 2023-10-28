from string import ascii_uppercase
import sys,re
#les expression reguliaires
regex1 = r"([a-zA-ZÉé]{5,}?)(?=\s*(K|LP|IVD)?\s*(\d+((,|\.)?\d+)?|½)\s*(MG|ML|G|mL|GR|µg|mg|mcg|UI|mG|mL|ml|g|gr|l|L|unités|cuillère à soupe|sachet|sachets|cps|flacon|sachet|cp|cps|sachet|sachets|injection|seringue|amp|IVL)?\W*:\s*(\d|½))"
regex2 = r"([a-zA-ZÉé]{5,}?)(?=\s*(K|LP|IVD)?\s*(\d+((,|\.)?\d+)?|½)\s*(MG|ML|G|mL|GR|µg|mg|mcg|UI|mG|mL|ml|g|gr|l|L|unités|cuillère à soupe|sachet|sachets|cps|flacon|sachet|cp|cps|sachet|sachets|injection|seringue|amp|IVL),\s*)"
regex3 = r"^-? ?([a-zA-ZÉé]{5,}) :? ?(\d+|,)+ (MG|ML|G|mL|GR|µg|mg|mcg|UI|mG|mL|ml|g|gr|l|L|unités|cuillère à soupe|sachet|sachets|cps|flacon|sachet|cp|cps|sachet|sachets|injection|seringue|amp|IVL).+"
regex4 = r"^Ø? ?([a-zA-ZÉé]{5,}) :? ?(\d+|,)+ (MG|ML|G|mL|GR|µg|mg|mcg|UI|mG|mL|ml|g|gr|l|L|unités|cuillère à soupe|sachet|sachets|cps|flacon|sachet|cp|cps|sachet|sachets|injection|seringue|amp|IVL).+"
medoc =[]
t=[]
j=0
a=open('subst-corpus.dic','w',encoding='utf-16-le')
a.write("\ufeff")

with open(sys.argv[1],'r',encoding='utf-8') as f :
    for i in f.readlines() :
        r =  re.search(regex1,i)
        if r :
            j+=1
            resp = str(r.group(1)).upper()
            a.write(str(r.group(1)).lower()+",.N+subst\n")
            t.append(resp)
            if resp not in medoc :
                medoc.append(resp)
        r =  re.search(regex2,i)
        if r :
            j+=1
            resp = str(r.group(1)).upper()
            a.write(str(r.group(1)).lower()+",.N+subst\n")
            t.append(resp)
            if resp not in medoc :
                medoc.append(resp) 
        r =  re.search(regex3,i)
        if r :
            j+=1
            resp = str(r.group(1)).upper()
            a.write(str(r.group(1)).lower()+",.N+subst\n")
            t.append(resp)
            if resp not in medoc :
                medoc.append(resp)
        r =  re.search(regex4,i)
        if r :
            j+=1
            resp = str(r.group(1)).upper()
            a.write(str(r.group(1)).lower()+",.N+subst\n")
            t.append(resp)
            if resp not in medoc :
                medoc.append(resp)
medoc.sort()
t=sorted(set(t))
#on ecris le fichier infos2
with open('infos2.txt','w',encoding="utf-8") as file :
        lettersDico = {}
        k=0
        for i in t:
            lettersDico.setdefault(i[0],[])
            lettersDico[i[0]].append(i)
        for i in lettersDico:
            k+=len(lettersDico[i])
            file.write('le nombre de mdicaments issus pour corpus pour la lettre {}:{}\n'.format(i.upper(),len(lettersDico[i])))
        file.write("Total:{}".format(len(t)))
# on supprime les mots non medicament qui sont passer dans la regex
medoc.pop(medoc.index('JANVIER'))
medoc.pop(medoc.index('DIFFU'))
medoc.pop(medoc.index('PROBABILISTE'))
medoc.pop(medoc.index('FAIBLE'))
medoc.pop(medoc.index('FIBRES'))
medoc.pop(medoc.index('SPECIAL'))
medoc.pop(medoc.index('POSOLOGIE'))
medoc.pop(medoc.index('RETARD'))
medoc.pop(medoc.index('INTRAVEINEUSE'))
medoc.pop(medoc.index('POTASSIUM'))

data_cleaned = []

with open('subst.dic','r',encoding="utf-16-le") as f :
    for i in f.readlines():
        data_cleaned.append(i.split(',')[0])

# on ecris le infos3.txt
with open('infos3.txt','w',encoding="utf-8") as file :
        lettersDico = {}
        k=0
        for i in medoc:
            lettersDico.setdefault(i[0],[])
            lettersDico[i[0]].append(i)
        for i in lettersDico:
            k+=len(lettersDico[i])
            file.write('le nombre de mdicaments conservs pour l\'enrichissement pour la lettre {}:{}\n'.format(i.upper(),len(lettersDico[i])))
        file.write("Total:{}".format(len(medoc)))

for i in data_cleaned : 
    if i not in medoc :
        medoc.append(i)
medoc.sort()
# on réecris dans subst.dic pour avoir la totalité des medicament 
with open('subst.dic','w',encoding="utf-16-le") as f :
    for i in medoc:
        f.write("{},.N+subst\n".format(i))
 