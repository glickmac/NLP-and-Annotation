# NLP: a Tutorial for Natural Language Processing 
<img src="https://github.com/ucdenver-CPBS/NLP-and-Annotation/blob/master/img/cloud.png" height="400" width="550">


## Table of Contents

[What is NLP?](#intro)    
[Why is this important?](#importance)    
[What Language?](#workflow)       
[Installing NLP Tools](#install)    
[NLP Usage](#usage)        
[Miscellaneous things you should know](#additional)    

## <a name="intro"></a>What is NLP?

NLP is blah

## <a name="importance"></a>Why is this important?

NLP can help you [classify a large number of documents into categories you defined](https://burakkanber.com/blog/machine-learning-naive-bayes-1/), using Naïve Bayes.

NLP can help you [find how a large number of documents cluster into different categories](http://scikit-learn.org/stable/auto_examples/text/document_clustering.html) automatically, using unsupervised machine learning.

NLP can help you generate synthetic text data to use for training or other purposes.

"NLP can destory the world" 

Sentiment Classification and Trump on Twitter



## <a name="workflow"></a>Languages Supporting NLP Packages

The majority of this tutorial is written in Python. Other languages that support NLP include R, Java, and PERL.



### Useful References

#### Wikipedia

[Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing)  
[Part-of-Speech Tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging)  
[Parsing](https://en.wikipedia.org/wiki/Parsing)  
[Stemming](https://en.wikipedia.org/wiki/Stemming)  
[Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)  

#### NLTK

This is one of the standard natural language processing libraries for Python. Keep in mind this is meant to deal with general language, so you may need to look for domain-specific (i.e. biomedicine) tools depending on your task.
[NLTK Website](http://www.nltk.org/)

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


## <a name="usage"></a><a name="quickstart"></a>NLP Usage

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

#### Dealing with Unicode and special characters

You will encounter special characters very often when dealing with biomedical data (e.g., "TNF1-α"). This could cause several of the common functions in NLP Python libraries to fail. In order to ensure the highest level of safety, you can add this at the very top of your Python script to interpret all text inputs as UTF-8:

```
# -*- coding: utf-8 -*-
```

... and include this as your last `import`:

```
import sys
reload(sys)
sys.setdefaultencoding('utf8')
```

If you want to just ignore some of the special characters (especially those that may be just control characters), you could convert your `some_string_var` variable to UTF-8 by:

```
some_string_var.decode('utf8', 'ignore')
```


