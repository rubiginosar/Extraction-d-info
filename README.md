# Extraction-d-info
un script qui permettant d’extraire (web scraping) les entités médicales et qui Génere en sortie un dictionnaire au format .dic et un fichier nommé « infos1.txt » contenant :
- le nombre d’entités médicales de type noms de médicaments par substance active du 
dictionnaire « subst.dic » généré préalablement, pour chaque lettre de l’alphabet ;
- et le nombre total d’entités médicales de type noms de médicaments par substance 
active de ce dictionnaire.
un deuxième script Python « enrichir.py », permettant d’alimenter et d’enrichir le dictionnaire « subst.dic » avec de nouvelles entités médicales de type noms de médicaments par nom commercial ou par substance active, à partir du fichier « corpus-medical.txt ». Le dictionnaire « subst.dic » après enrichissement ne doit pas contenir de doublons et doit être trié par ordre croissant (a-z).
Le script d’enrichissement garde une trace des noms de médicaments trouvés dans le fichier 
« corpus-medical.txt », en les stockant dans un autre fichier appelé « subst_corpus.dic »,il Génére aussi un fichier nommé « infos2.txt » sans doublons contenant :
- le nombre de médicaments issus du corpus pour chaque lettre de l’alphabet ;
- et le nombre total de médicaments issus du corpus.
et un fichier nommé « infos3.txt » sans doublons contenant :
- le nombre de médicaments conservés pour l’enrichissement pour chaque lettre de 
l’alphabet ;
- et le nombre total de médicaments conservés pour l’enrichissement.
Construction d'un graphe d’extraction (.grf) sous UNITEX, qui se base impérativement sur l’étiquette 
<N+subst> du dictionnaire « subst.dic », afin d’extraire les occurrences de « posologies » à partir 
du fichier « corpus-medical.txt ». Le graphe d’extraction s’appele « posologie.grf ». Le résultat 
de cette extraction sera placé par UNITEX dans le fichier « concord.html », qui se trouve dans le 
dossier « corpus-medical_snt » généré par UNITEX.
un troisième script permettant d’appeler UNITEX pour exploiter votre graphe, à partir de 
l’emplacement C:\................\Unitex-GramLab\App>

