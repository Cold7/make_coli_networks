#to run the script you need to start pathway tools form the command line using the -lisp -python options
#example (form the pathwway tools folder)
# ./pathway-tools -lisp -python

import pythoncyc


ecoli = pythoncyc.select_organism('ecoli')

#getting genes of ecoli
ecoliGenes = ecoli.Genes

flag = True
i = 0
#creating a gene list, because  from the pythoncyc is not an iterable object
geneList = []
while flag:
	try:
		if str(ecoliGenes[i]).split("|")[1] not in geneList:
			geneList.append(str(ecoliGenes[i]).split("|")[1])
		i+=1
	except:
		flag = False

regulatingDict = {}

#for ech gene in geneList, Im going to look wich genes are regulated by the current gene, and it will be saved in a dictionary (regulatingDict)
for gene in geneList:
	genesRegulatedByThis=[]
	for item in pythoncyc.PGDB.genes_regulated_by_gene(ecoli, gene):
		genesRegulatedByThis.append(str(item)[1:-1])
	regulatingDict[gene]=genesRegulatedByThis

#file to save results
savingFile=open("name.tsv","w")
savingFile.write("TF\tTU_TF\tTU_TARGET\tGENE_LIST\n")

#aux vars are to do not write a line twice
aux=[]
tuGeneList={}

#looping the dictionary gene=[genes regulated by the first one]
for item in regulatingDict.items():
	#first part of text to write, that is TF and then the TU ID where the TF gene is present
	toWritte=item[0]+"\t"+str(pythoncyc.PGDB.gene_transcription_units(ecoli,item[0])).replace("u'","").replace("'","").replace("|","")+"\t"
	
	if len(item[1])!=0:
		#for the gene list regulated by the TF
		for item2 in item[1]:
			#getting the TU ID of the gene regulated by the TF and then write it toghether with genes forming the TU
			for some in pythoncyc.PGDB.gene_transcription_units(ecoli,item2):
				toWritte2=some.replace("|","")+"\t"+str(pythoncyc.PGDB.transcription_unit_genes(ecoli,some)).replace("u'","").replace("'","").replace("|","")
				
				#to not write the same twice
				if toWritte+toWritte2 not in aux:
					savingFile.write(toWritte+toWritte2+"\n")
					aux.append(toWritte+toWritte2)
				



savingFile.close()

