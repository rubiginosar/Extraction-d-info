import os 
os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt Dela_fr.bin subst.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courier new\" -s 12")

#Alphabet.txt est un fichier texte decrivant tous les caracteres d'une langue, ainsi que les correspondances entre les lettres minuscules et majuscules
#il est obligaatoire pour qu'Unitex puisse fonctionner, chaque ligne du ce fichier doit avoir une une des formes suivantes suivi par un routeur a la ligne:
#1- Un diese suivi de caracteres X et Y indique que tous les caracteres compris entre les caracteres X et Y sont des lettres. 
#Tous ces caracteres sont consideres comme etant a la fois minuscules et majuscules. Ce mode est utile pour definir les alphabets des langues asiatiques 
#comme le coreen, le chinois
#2- 2 caracteres X et Y indiquent que X et Y sont des lettres et que X est l'equivalent en majuscule de la lettre Y
#3- un unique caractere X definit X comme une lettre a la fois minuscule et majuscule. Ce mode est utile pour definir un caractere asiatique de maniere ponctuelle.
#Pour certaines langues comme le francais,il arrive qu'a une lettre minuscule correspondent a plusieurs majuscules, comme c'estle cas pour le è, qui peut avoir comme majuscule soit E, È
#Pour exprimer cela, il suffit d'utiliser plusieurs lignes. Le contraire est egalement vrai, le E peut etre la majuscule de é, è, ё, ê ou e