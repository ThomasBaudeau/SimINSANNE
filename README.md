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

#Utilisation

conda activate snakemake
Dans le répertoire SimINSANNE
snakemake -c1 --use-conda all
```
