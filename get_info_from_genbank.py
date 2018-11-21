# -*- encoding : utf-8 -*-
'''
__author__ = "LiYiming"
python3
get seqs info from ncbi by key words
'''

from Bio import Entrez
import re
Entrez.email = "liym@ioz.ac.cn"

# search Entrez
result = Entrez.esearch(db="nucleotide", term="(MHC[TITL] OR Major histocompatibility complex[TITL] OR major histocompatibility complex[TITL])  AND Mammalia[ORGN]", retmax="1000000", usehistory="n")
IDrecord = Entrez.read(result)

gi_list = IDrecord["IdList"]     # GI
count = int(IDrecord["Count"])
webenv = IDrecord["WebEnv"]
query_key = IDrecord["QueryKey"]

# download info
num = 0
pubnum = 0
doinum = 0

file = open('output_plant.csv','w')    # make a file to which you can save your results
file.writelines("cn_number"+"\t"+"GI"+"\t"+"product"+"\t"+"definition"+"\t"+"taxon_number"+"\t"+"taxon"+"\t"+"length"+"\t"+"type"+"\t"+"submit_date"+"\t"+"paper_title"+"\t"+"pubmed"+"\t"+"DOI"+"\t"+"Journal"+"\t"+"Country"+"\t"+"LAT"+"\t"+"LON"+"\n")

for i in range(int(count/10000)+1):
    ret = i*10000
    handle = Entrez.efetch(db="nucleotide",rettype="gb", retmode="xml", webenv=webenv,query_key=query_key, retmax="10000", retstart="%s"%ret)   # the max retmax is 10000
    record = Entrez.read(handle)
    print("---------------------starting--------------------------" )
# analysis results
    for index in range(len(record)):
        product = "no_data"    # protein product
        accession = record[index]["GBSeq_primary-accession"]    # NC number of seqs
        gi = record[index]["GBSeq_other-seqids"][len(record[index]["GBSeq_other-seqids"])-1]
        gi = gi[3:]
        for ij in range(3):
            try:
                for j in record[index]["GBSeq_feature-table"][ij]["GBFeature_quals"]:
                    if j[list(j.keys())[0]] == "product":
                        product = j[list(j.keys())[1]]
                    else:
                        pass
            except:
                pass
        #protein_id = "no_data"  # protein product
        defi = record[index]["GBSeq_definition"]    # definition of seqs
        for i in record[index]["GBSeq_feature-table"][0]["GBFeature_quals"]:    # the ID of taxon
            if i[list(i.keys())[0]] == "db_xref":
                taxonnumer = i[list(i.keys())[1]]
            else:
                pass
        taxon = record[index]["GBSeq_taxonomy"]    # taxon
        seqlen = record[index]["GBSeq_length"]    # the length of seqs
        seqtype = record[index]["GBSeq_moltype"]    # DNA or RMA or something else
        date = record[index]["GBSeq_create-date"]    # submit date
        try:    # title of the papers
            title = record[index]["GBSeq_references"][0]["GBReference_title"]
        except:
            title = "no_data"
        try:    # PUBMED number
            pubmed = record[index]["GBSeq_references"][0]["GBReference_pubmed"]
            pubnum = pubnum + 1
        except:
            pubmed = "no_data"
        try:    # DOI
            doi = record[index]["GBSeq_references"][0]["GBReference_xref"][0]["GBXref_id"]
            doinum = doinum + 1
        except:
            doi = "no_data"
        try:    # journal
            journal = record[index]["GBSeq_references"][0]["GBReference_journal"]
        except:
            journal = "no_data"
        latlon = "none"
        for i in record[index]["GBSeq_feature-table"][0]["GBFeature_quals"]:  # latitude and longtitude
            if i[list(i.keys())[0]] == "lat_lon":
                latlon = i[list(i.keys())[1]]
            else:
                pass
        if latlon == "none":
            lat = "none"
            lon = "none"
        else:
            try:
                lat = re.findall(r"\d+\.\d+\s\D",latlon)[0]
                lon = re.findall(r"\d+\.\d+\s\D", latlon)[1]
            except:
                pass
        country = "none"
        for i in record[index]["GBSeq_feature-table"][0]["GBFeature_quals"]:  # country
            if i[list(i.keys())[0]] == "country":
                country = i[list(i.keys())[1]]
            else:
                pass

        num = num + 1
        print("---------------------get :%s seqs--------------------------"%num)

# save results to txt
        file.writelines("%s"%accession+"\t"+"%s"%gi+"\t"+"%s"%product+"\t"+"%s"%defi+"\t"+"%s"%taxonnumer+"\t"+"%s"%taxon+"\t"+"%s"%seqlen+"\t"+"%s"%seqtype+"\t"+"%s"%date+"\t"+"%s"%title+"\t"+"%s"%pubmed+"\t"+"%s"%doi+"\t"+"%s"%journal+"\t"+"%s"%country+"\t"+"%s"%lat+"\t"+"%s"%lon+"\n")
file.close()

# supervise
print("total number of seqs:",count,"we get the number of seqs:",len(gi_list))
print("PUBMED has",pubnum)
print("DOI has",doinum)
