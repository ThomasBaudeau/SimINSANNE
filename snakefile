configfile: 'data/config.yaml'
COV=config['couverture']
R_LEN=config['taille_read']
T_REF=config['longueur_ref']
MUT=config['mutation']

rule simulate_short:
    input:
        'data/ref.fasta'
    output:
        b='art_out.aln',
        c='art_out.fq'

    params:
        cov =COV,
        r_len=R_LEN
    conda:
        'envs/art.yaml'
    shell:
        "art_illumina -i {input} -l {params.r_len} -f {params.cov} -o art_out"


rule induce_mutation:
    input:
        'art_out.aln',
        'art_out.fq'
    output:
        'read_mut.fasta'
    params:
        mut = MUT,
        r_len=R_LEN,
        t_ref=T_REF
    conda:
        'envs/art.yaml'
    script:
        "scripts/induce_mutation.py"


rule samtool_index:
    input:
        'read_mutAligned.sortedByCoord.out.bam'
    output:
        'align_md.bam'
    shell:
        "samtools calmd -b read_mutAligned.sortedByCoord.out.bam data/ref.fasta > align_md.bam ; samtools index align_md.bam"


rule star_align:
    input:
        ref='data/ref.fasta',
        read='read_mut.fasta'
    output:
        'read_mutAligned.sortedByCoord.out.bam'
        
    conda:
        'envs/star.yaml'
    shell:
        "test=$(mktemp -d); STAR --runThreadN 6 --runMode genomeGenerate --genomeDir $test --genomeFastaFiles {input.ref};STAR --genomeDir $test --runThreadN 6 --readFilesIn {input.read} --outFileNamePrefix read_mut --outSAMtype BAM SortedByCoordinate --outSAMunmapped Within --outSAMattributes Standard"

rule jacusa:
    input:
        'align_md.bam'
    output:
        'results_call1.out'
    shell:
        'java -jar bin/JACUSA2/target/JACUSA2-2.0.2.jar call-1 -r results_call1.out {input}'


rule all:
    input:
       'results_call1.out'
