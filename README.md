# Conlp: Colorado Natural Language Processing Repository 
## Table of Contents

[What is NLP?](#intro)    
[Why is this important?](#importance)    
[What Language?](#workflow)       
[Installing NLP Tools](#install)    
[NLP Tutorials](#tutorial)        
[Additional Functionality](#additional)    

## <a name="intro"></a>What is NLP?

Natural Language Process or NLP is blah

## <a name="importance"></a>Why is this important?

NLP is used in x, y, and z. 

## <a name="workflow"></a>Languages Supporting NLP Packages

Python 

R 

JAVA 

Demo Image Below
<img src="https://github.com/NCBI-Hackathons/VirusCore/blob/master/input.png" height="400" width="550">

### Useful References

#### Magic-BLAST

[BLAST Command Line Manual](https://www.ncbi.nlm.nih.gov/books/NBK279690/)    
[Magic-BLAST GitHub repo](https://github.com/boratyng/magicblast)    
[Magic-BLAST NCBI Insights](https://ncbiinsights.ncbi.nlm.nih.gov/2016/10/13/introducing-magic-blast/)    

#### MEGAHIT

[MEGAHIT GitHub repo](https://github.com/voutcn/megahit)    
[MEGAHIT Paper](https://www.ncbi.nlm.nih.gov/pubmed/25609793)    

#### Protein Domain Identification

[BLAST Command Line Manual](https://www.ncbi.nlm.nih.gov/books/NBK279690/)    
[NCBI Conserved Domain and Protein Classification](https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd_help.shtml)    

#### Glimmer3

[Glimmer3 Page at JHU](https://ccb.jhu.edu/software/glimmer/)    
[Glimmer3 Paper](https://ccb.jhu.edu/papers/glimmer3.pdf)    
[Glimmer3 Manual](https://ccb.jhu.edu/software/glimmer/glim302notes.pdf)    

## <a name="install"></a>Installing NLP Packages

Required software
+ Magic-BLAST (>= v1.3): [download](https://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/LATEST) [documentation](https://boratyng.github.io/magicblast/)
+ [BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
+ [Samtools](http://www.htslib.org/) (>= version 1.5)
+ [Prinseq](http://prinseq.sourceforge.net/)
+ [MEGAHIT](https://github.com/voutcn/megahit)
+ [Glimmer3](https://ccb.jhu.edu/software/glimmer/)


## <a name="usage"></a><a name="tutorial"></a>NLP Usage

### Tutorials
+ [Vectorizing Text](https://github.com/ucdenver-CPBS/NLP-and-Annotation/blob/master/notebooks/Vectorizing_Text.ipynb)



#### Example usage

```
viruspy.sh [-d] [-f viral_genomes.fasta/-b viral_db] -s SRR1553459 -o output_folder
```

#### Required arguments:

| Option     | Description                                     |
|------------|-------------------------------------------------|
| **-s**   | SRR acession number from SRA database           |
| **-o**   | Folder to be used for pipeline output |

#### Optional arguments:

| Option    | Description |
|-----------|-------------|
| **-f**    |FASTA file containing viral sequences to be used in construction of a BLAST database. If neither this argument nor -b are used, ViruSpy will default to using the Refseq viral genome database.|
| **-b**    |BLAST database with viral sequences to be used with Magic-BLAST. If neither this argument nor -f are used, ViruSpy will default to using the Refseq viral genome database.|
| **-d**    |Determines signature of viruses that are integrated into a host genome (runs the BUD algorithm)|


## <a name="additional"></a>Additional Functionality
