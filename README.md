# NLP: a Tutorial for Natural Language Processing 
<img src="https://github.com/NCBI-Hackathons/VirusCore/blob/master/input.png" height="400" width="550">


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

#### Books

Jurafsky & Martin's NLP book [is available online in PDF format](https://web.stanford.edu/~jurafsky/slp3/)
[Foundations of Statistical Natural Language Processing (Manning, Schuetze)](https://smile.amazon.com/Foundations-Statistical-Natural-Language-Processing-ebook/dp/B007L7LUKO/ref=mt_kindle?_encoding=UTF8&me=)
[Natural Language Processing with Python](https://smile.amazon.com/Natural-Language-Processing-Python-Analyzing/dp/0596516495/ref=sr_1_1?ie=UTF8&qid=1512597647&sr=8-1&keywords=natural+language+processing+with+python)

#### Wikipedia

[Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing)
[Part-of-Speech Tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging)
[Parsing](https://en.wikipedia.org/wiki/Parsing)
[Stemming](https://en.wikipedia.org/wiki/Stemming)
[Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)

#### NLTK

[NLTK](http://www.nltk.org/) is one of the standard natural language processing libraries for Python. Keep in mind this is meant to deal with general language, so you may need to look for domain-specific (i.e. biomedicine) tools depending on your task.

For our particular domain, there are tools beyond NLTK that might perform better:

[BioLemmatizer](http://biolemmatizer.sourceforge.net) can help you find the "lemma" of a term, within the context of biology.



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


#### Handy command-line tool examples:

You will find it very beneficial to become acquainted with tools like `awk`, `sed`, and `sort`, among others. Here's a snapshot of things you could do with various Unix command-line tools:

| You're trying to...     | You can use:                  |
|------------|-------------------------------------------------|
| ... count how many lines are in a document | `wc -l INPUT_FILE` |
| ... perform fast & loose tokenization (i.e. to establish a baseline or perform quick stats) splitting on anything that is not a letter | `tr -sc ’A-Za-z’ ’\n’ < INPUT_FILE > OUTPUT_FILE` |
| ... swap columns 1 and 2, separated by a ":" | `awk -F: -v OFS=":" '{print $2,$1}' INPUT_FILE`  |
| ... keep only the first 3 columns from a tab-separated file | `awk -F\t -v OFS="\t" '{print $1,$2,$3}' INPUT_FILE > OUTPUT_FILE` |
| ... remove duplicate lines from a file | `awk '!seen[$0]++' INPUT_FILE > OUTPUT_FILE` |
| ... sort REALLY LARGE files (ideally in a cluster) | `sort --buffer-size=4G -k1,1 -k2,2n -i $BEDFILE_HG19 > $BEDFILE_HG19_SORTED` |
| ... replace any instance of string `This is foo` with string `This is bar` | `sed 's/^\(This is \).*$/\1bar/'` |

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


