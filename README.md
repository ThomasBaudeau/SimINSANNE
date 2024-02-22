# SimINSANNE



#Installation
```
git clone https://github.com/ThomasBaudeau/SimINSANNE/tree/main
cd SimINSANNE
mkdir bin
cd bin
git clone https://github.com/dieterich-lab/JACUSA2
cd JACUSA2
mvn clean install
cd ../..
sudo apt install samtools
```

#Utilisation SimINSSANE
```
conda activate snakemake
Dans le répertoire SimINSANNE
snakemake -c1 --use-conda all
```


#A la reception:
'''
FASTA ou FASTQ
Besoin du FASTQ

regarder l'extension :

Si .GZ cela veut dire que le fichier est compréssé.
si fichier rouge:
sudo chmod 777 NOMDUFICHIER
SI BEUG avec TAR.GZ pour le décompresser commande suivante: 
tar xzvf nom_archive.tar.gz

ou 
si que .gz
gunzip NOMDUFICHIER


Pour télécgarger:
wget URL 
'''
#Utilisation STAR

(Outil de mapping)
```
cd tools/STAR/bin/Linux_x86_64   #pour aller à l'endroit pour lancer STAR
Pour le lancer:
test=$(mktemp -d);
./STAR --runThreadN 6 --runMode genomeGenerate --genomeDir $test --genomeSAindexNbases 11 --genomeFastaFiles NOMFICHIERREFERENCE
./STAR --genomeDir $test --runThreadN 6 --readFilesIn NOMDUFICHIERDEREAD --outFileNamePrefix LENOMDELASORTI --outSAMtype BAM SortedByCoordinate --outSAMunmapped Within --outSAMattributes Standard"

```


#Utilisation BWA-MEM

(Outil de mapping)
```
conda activate snakemake
Dans le répertoire SimINSANNE
snakemake -c1 --use-conda all
```

#Utilisation Samtool
```
   "samtools calmd -b NOMDUFICHIERDALIGNEMENT NOMDELAREFERENCE > NOMDUFICHIERDESORTI.bam ; samtools index NOMDUFICHIERDESORTI.bam
```

#Utilisation JACUSA2
```
Il faut aller dans le repertoire de JACUSA2
puis dans: bin/
Ensuite:
```
- Si tu veux faire xp pour trouver les points d'arrets:
```
java -jar JACUSA2-2.0.2.jar call-1 -r NOMDUFICHIERRESULTAT NOMDUFICHIERMDTAG.bam
```
-Si tu veux faire xp pour trouver les mutations:
```
```
```

#Utilisatation de Nanocompore:

- activer l'environement conda de Nanocompore avec:
```
conda activate nanocompore
```
- 1er étape pré-traitement des base non caller (fichier FAST5):
  
```
TODO
```
-2ieme étape:
```
TODO
```

