# -*- coding:utf-8 -*-
'''
download sequences from ncbi by accession number
python3
'''
__author__ = "LiYiming"
__date__ = '2018-6-3'
from Bio import Entrez      # need package：Biopython
Entrez.email = 'liym@ioz.ac.cn'   # tell NCBI who you are

# accesion number file and output file
accession_file = 'C:\\Users\\ll\\Desktop\\TEMP.txt'
file_out_name = '1.fasta'

# read accession number from file
def read_id(file_name):
    id_array = []
    fh = open(file_name, 'r')
    lines = fh.readlines()
    for line in lines:
        id = line.strip()
        id_array.append(id)
    fh.close()
    #id_array = list(set(id_array))    # quchong
    id_array = ','.join(id_array)
    return id_array

# download sequences by accession number
def download_seq(id_array):
    result_handle = Entrez.efetch(db="nucleotide", rettype="FASTA", id=id_array)
    result = result_handle.read()
    return result

# write sequences to file
def write_to_file(file_out_name, content):
    fh = open(file_out_name, 'w')
    fh.write(content)
    fh.close()

id_array = read_id(accession_file)
result = download_seq(id_array)
write_to_file(file_out_name, result)