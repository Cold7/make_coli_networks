# make_coli_networks

This script take information from pathway tools and create a gene regulatory network in tsv format for e coli. Info to save is:
Transcription Factor & its transcriptional units
Transcriptional units who is regulated by the TF and the gene list of this Transcriptional unit

Requirenments:

You need to have installed pathway tools and initialize it doing:
./pathway-tools -lisp -python

Also you need to have installed python librarie pythoncyc
