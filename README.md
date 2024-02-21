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

#Utilisation STAR

(Outil de mapping)
```
cd tools/STAR
Pour le lancer:
./STAR 
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
