import pandas as pd

# input
table = pd.read_csv(r"C:\Users\ll\Desktop\1538.csv",encoding='ISO-8859-1',header=0)
out = open(r"C:\Users\ll\Desktop\out.csv","w")

seq = table["clean_sequence"]
sub1 = [6,8,15,25,35,38,45,48,49,52]   # 氨基酸位点号
sub2 = [1,2,3,4,5,7,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34,36,37,39,40,41,42,43,44,46,47,50,51]

# 把氨基酸位点号转换成核苷酸序列号
sub11 = []
sub22 = []
for i in sub1:
    sub11 = sub11 + [(i-1)*3+1] + [(i-1)*3+2] + [(i-1)*3+3]
for i in sub2:
    sub22 = sub22 + [(i-1)*3+1] + [(i-1)*3+2] + [(i-1)*3+3]
sub1 = sub11
sub2 = sub22

for i in seq:
    sub_seq1 = ""
    sub_seq2 = ""
    for n in sub1:
        sub_seq1 = sub_seq1 + i[n - 1]
    for n2 in sub2:
        sub_seq2 = sub_seq2 + i[n2 - 1]

    out.writelines(sub_seq1 + "," + sub_seq2 + "\n")
out.close()