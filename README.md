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

Natural Language Processing ([NLP](https://www.google.com/search?rlz=1C5CHFA_enUS727US727&biw=893&bih=927&ei=AWsoWuShBM-YjwPYyK-QDQ&q=what+is+natural+language+processing&oq=what+is+natural+language+processing&gs_l=psy-ab.3..0j0i20i263k1j0l7.5493.9709.0.9834.29.28.1.0.0.0.156.2686.21j7.28.0....0...1.1.64.psy-ab..0.29.2687...0i131i67k1j0i20i264k1j0i131k1j0i67k1j0i131i20i264k1j0i13k1.0.AE1jefbB4Mo) was born as the intersection of artificial intelligence and computational linguistics and focuses on human language-computer interactions. More specifically, NLP provides a means for developing applications that leverage linguistic structure to help computers derive meaning from human language [Cohen et al., 2014](https://books.google.com/books?hl=en&lr=&id=vXvPAgAAQBAJ&oi=fnd&pg=PR1&dq=natural+language+processing,+kevin+cohen&ots=ZG5jQaAmMO&sig=l8YRe4YXml_ceCJwnisYL6RLZ38#v=onepage&q=natural%20language%20processing%2C%20kevin%20cohen&f=false). 

## <a name="importance"></a>Why is this important?

  * NLP can help you [classify a large number of documents into categories you defined](https://burakkanber.com/blog/machine-learning-naive-bayes-1/), using Naïve Bayes.

  * NLP can help you [find how a large number of documents cluster into different categories](http://scikit-learn.org/stable/auto_examples/text/document_clustering.html) automatically, using unsupervised machine learning.

  * NLP can help you generate synthetic text data to use for training or other purposes.

  * "NLP can destory the world" 

  * Sentiment Classification and Trump on Twitter



## <a name="workflow"></a>Languages Supporting NLP Packages

The majority of this tutorial is written in Python. Other languages that support NLP include R, Java, and PERL.



### Useful Resources

#### Jupyter Tutorials in Respository

* [Jupytercon](https://github.com/ucdenver-CPBS/NLP-and-Annotation/tree/master/notebooks/jupytercon-2017)
* [NLTK Intro](https://github.com/ucdenver-CPBS/NLP-and-Annotation/blob/master/notebooks/nltk_Intro.ipynb) 
* [Vectorizing Text](https://github.com/ucdenver-CPBS/NLP-and-Annotation/blob/master/notebooks/Vectorizing_Text.ipynb) 
* [Making Word Clouds](https://github.com/ucdenver-CPBS/NLP-and-Annotation/blob/master/notebooks/Word_Clouds.ipynb)
* [NLP with SpaCy](https://github.com/ucdenver-CPBS/NLP-and-Annotation/blob/master/notebooks/spaCy_Intro/spacy_intro.ipynb)

#### Books

* Jurafsky & Martin's NLP book [is available online in PDF format](https://web.stanford.edu/~jurafsky/slp3/)
* [Foundations of Statistical Natural Language Processing (Manning, Schuetze)](https://smile.amazon.com/Foundations-Statistical-Natural-Language-Processing-ebook/dp/B007L7LUKO/ref=mt_kindle?_encoding=UTF8&me=)
* [Natural Language Processing with Python](https://smile.amazon.com/Natural-Language-Processing-Python-Analyzing/dp/0596516495/ref=sr_1_1?ie=UTF8&qid=1512597647&sr=8-1&keywords=natural+language+processing+with+python)

 
#### Wikipedia

  * [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing)  
  * [Part-of-Speech Tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging)  
  * [Parsing](https://en.wikipedia.org/wiki/Parsing)  
  * [Stemming](https://en.wikipedia.org/wiki/Stemming)  
  * [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)  

#### NLTK

* [NLTK](http://www.nltk.org/) is one of the standard natural language processing libraries for Python. Keep in mind this is meant to deal with general language, so you may need to look for domain-specific (i.e. biomedicine) tools depending on your task.
* For our particular domain, there are tools beyond NLTK that might perform better: 
 * [BioLemmatizer](http://biolemmatizer.sourceforge.net) can help you find the "lemma" of a term, within the context of biology. 

#### SpaCy

See the [jupyter notebook](https://github.com/ucdenver-CPBS/NLP-and-Annotation/blob/master/notebooks/spaCy_Intro/spacy_intro.ipynb) in this repository for more information.    
  

## <a name="install"></a>Installing NLP Packages

Required software
  * NLTK:   
  ```
pip install nltk
```


## <a name="usage"></a><a name="quickstart"></a>NLP Usage

#### Handy command-line tool examples

You will find it very beneficial to become acquainted with tools like `awk`, `sed`, and `sort`, among others. Here's a snapshot of things you could do with various Unix command-line tools:

| You're trying to...     | You can use:                  |
|------------|-------------------------------------------------|
| ... count how many lines are in a document | `wc -l INPUT_FILE` |
| ... perform fast & loose tokenization (i.e. to establish a baseline or perform quick stats) splitting on anything that is not a letter | `tr -sc ’A-Za-z’ ’\n’ < INPUT_FILE > OUTPUT_FILE` |
| ... swap columns 1 and 2, separated by a ":" | `awk -F: -v OFS=":" '{print $2,$1}' INPUT_FILE`  |
| ... keep only the first 3 columns from a tab-separated file | `awk -F\t -v OFS="\t" '{print $1,$2,$3}' INPUT_FILE > OUTPUT_FILE` |
| ... remove duplicate lines from a file | `awk '!seen[$0]++' INPUT_FILE > OUTPUT_FILE` |
| ... sort REALLY LARGE files (ideally in a cluster) | `sort --buffer-size=4G -k1,1 -k2,2n -i INPUT_FILE > OUTPUT_FILE` |
| ... replace any instance of string `This is foo` with string `This is bar` | `sed 's/^\(This is \).*$/\1bar/'` |


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


# TODO

How to obtain a corpora of text (searching and mass downloading from Pubmed)
