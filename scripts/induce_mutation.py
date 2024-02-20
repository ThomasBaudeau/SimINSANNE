import random
def make_reverse(seq):
    n_seq=''
    for i in seq:
        n_seq+=nuc_reverse(i)
    return n_seq



def nuc_reverse(x):
    if x=='A':
        return 'T'
    if x=='T':
        return 'A'
    if x=='C':
        return 'G'
    if x=='G':
        return 'C'

def deal_del(x):
    new=""
    for i in x:
        if i!='-':
            new+=i
    return new

def rnuc(x):
    a=random.choice('ACTG')
    while a==x:
        a=random.choice('ACTG')
    return a

def main_snakefile(inp,inp1,out,param):
    print(snakemake.params)
    l_gen=param['t_ref']
    l_read=param['r_len']
    mutation=param['mut']
    file_read=open(inp).readlines()
    file_head=open(inp1).readlines()
    lmutation=[198,242,7877,7883,8110,8079,8975,8989]
    nfsta=open(out,'w')
    for i in range(len(file_read)-3):
        if file_read[i][0]=='>':
            file_read=file_read[i:]
            break
    for i in range(len(file_head)):
        if file_head[i][0]=='@':
            file_head=file_head[i:]
            break
    for i in range(int(len(file_read)/3)-1):    
            nohead=False
            head=file_read[i*3].split('\t')
            pos=int(head[2])
            strand=head[3][0]

            seq=file_read[(i*3)+2][:-1]
            seq=deal_del(seq)
            if strand=='-':
                
                pos=l_gen-int(pos)-l_read
            
            tomut=[]
            for mut in lmutation:
                mut-=169
                if pos<mut and pos+150>=mut:
                    mut-=pos
                    amutation=random.randint(1,100)
                    if amutation<=mutation :
                        seq=seq[:mut-1]+rnuc(seq[mut-1])+seq[mut:]
                        if strand=='-':
                            seq=make_reverse(seq)[::-1]
            nfsta.write(file_head[i*4])
            nfsta.write(seq+'\n')
            nfsta.write(file_head[(i*4)+2])
            nfsta.write(file_head[(i*4)+3])
    
        



main_snakefile(snakemake.input[0],snakemake.input[1],snakemake.output[0],snakemake.params)
            
                    
                    

        
