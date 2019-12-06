# put seqs and coords into format matrics
# __author__ "chengchaoyuan"
# 表格需要先根据变量“binomial_name”进行排序

import pandas as pd


# input
###################################################
# normal
frame = pd.read_csv(r"C:\Users\ll\Desktop\2-order.csv", sep=",", header=0)
output_d = "C:\\Users\\ll\\Desktop\\2out1\\"
seq = frame["clean_sequence"]

# abs
#frame = pd.read_csv(r"C:\Users\ll\Desktop\DQB_1.csv", sep=",", header=0)
#output_d = "C:\\Users\\ll\\Desktop\\out2\\"
#seq = frame["abs_seq"]

# noabs seq
#frame = pd.read_csv(r"C:\Users\ll\Desktop\DQB_1.csv",sep =",",header= 0 )
#output_d = "C:\\Users\\ll\\Desktop\\out3\\"
#seq = frame["noabs_seq"]

#####################################################



def readcsv(filepath):
    outlist=[]
    try:
        file=open(filepath,"r",encoding="utf-8-sig").readlines()
    except:
        file=open(filepath,"r",encoding="utf-8").readlines()
    for i in file:
        i=i[:-1]
        outlist=outlist+[i]
    return outlist

# extract columns that needed
name = frame["binomial_name"]
lat = frame["latitude"]
lon = frame["longitude"]


ind = name[0]
outlat = open("123.txt","w")
outseq = open("356.txt","w")

for i in range(len(name)):
    name0 = name[i]
    lat0 = lat[i]
    lon0 =lon[i]
    seq0 = seq[i]

    if name0 == ind:
        if i ==0:
            outseq = open("%s%s.fasta" %(output_d,name0), "w")
            outlat = open("%s%s.coords" %(output_d,name0), "w")
        else:
            pass
        seq0 = seq0.replace("A","1").replace("T","2").replace("G","3").replace("C","4").replace("-","0").replace("N","0").replace("Y","0").replace("D","0").replace("B","0").replace("R","0").replace("W","0").replace("S","0").replace("K","0").replace("V","0").replace("H","0").replace("M","0")     # trans ATGC into 1234
        index = 0
        for j in seq0:
            index = index + 1
            if index != len(seq0):
                outseq.writelines(j + ",")
            else:
                outseq.writelines(j + "\n")
        outlat.writelines(str(lat0) + ","+ str(lon0) + "\n")
    else:
        outlat.close()
        outseq.close()
        outseq = open("%s%s.fasta" %(output_d,name0), "w")
        outlat = open("%s%s.coords" %(output_d,name0), "w")
        seq0 = seq0.replace("A", "1").replace("T", "2").replace("G", "3").replace("C", "4").replace("-", "0").replace(
            "N", "0").replace("Y", "0").replace("D", "0").replace("B", "0").replace("R", "0").replace("W", "0").replace(
            "S", "0").replace("K", "0").replace("V", "0").replace("H", "0").replace("M", "0")  # trans ATGC into 1234
        index = 0
        for j in seq0:
            index = index + 1
            if index != len(seq0):
                outseq.writelines(j + ",")
            else:
                outseq.writelines(j + "\n")
        outlat.writelines(str(lat0) + "," + str(lon0) + "\n")
        ind = name0
