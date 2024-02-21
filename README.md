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
SI BEUG avec .GZ pour le décompresser commande suivante: 
tar xzvf nom_archive.tar.gz
'''
#Utilisation STAR

(Outil de mapping)
```
cd tools/STAR/bin/Linux_x86_64
Pour le lancer:
test=$(mktemp -d);
./STAR --runThreadN 6 --runMode genomeGenerate --genomeDir $test --genomeFastaFiles NOMFICHIERREFERENCE
Dans le répertoire SimINSANNE
snakemake -c1 -
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
conda activate snakemake
Dans le répertoire SimINSANNE
snakemake -c1 --use-conda all
```

#Utilisation JACUSA2
```
conda activate snakemake
Dans le répertoire SimINSANNE
snakemake -c1 --use-conda all
```
