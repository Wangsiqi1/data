# join coords and biomcode into each single file by species
# __author__ "chengchaoyuan"
###### 每次运行要把输出文件夹清空，否则结果会合并进去 ######
import os
import pandas as pd
import os
# input
#######################################################
# normal
frame = pd.read_csv(r"C:\Users\ll\Desktop\2.csv",sep =",",header= 0 )
#output_biom = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\biomes\\"
#output_anthrome = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\anthromes\\"
#output_litter_size = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\litter_size\\"
#output_bodymass = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\bodymass\\"
#output_lifespan = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\lifespan\\"
#output_order = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\order\\"
#output_iucn = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values\\iucn\\"
output_population = "C:\\Users\\ll\\Desktop\\2out1\\"
seq = frame["clean_sequence"]

# abs seq
# frame = pd.read_csv(r"C:\Users\40506\OneDrive\MHC\final_data\total\DRB_final.csv",sep =",",header= 0 )
# output_biom = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\biomes\\"
# output_anthrome = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\anthromes\\"
# output_litter_size = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\litter_size\\"
# output_bodymass = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\bodymass\\"
# output_lifespan = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\lifespan\\"
# output_order = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\order\\"
# output_iucn = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\iucn\\"
# output_population = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_ABS\\populations\\"
# seq = frame["abs_seq"]

# # noabs_seq
# frame = pd.read_csv(r"C:\Users\40506\OneDrive\MHC\final_data\total\DRB_final.csv",sep =",",header= 0 )
# output_biom = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\biomes\\"
# output_anthrome = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\anthromes\\"
# output_litter_size = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\litter_size\\"
# output_bodymass = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\bodymass\\"
# output_lifespan = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\lifespan\\"
# output_order = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\order\\"
# output_iucn = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\iucn\\"
# output_population = "C:\\Users\\40506\\OneDrive\\MHC\\calculate_values_noABS\\populations\\"
# seq = frame["noabs_seq"]


######################################################
# extract columns that needed
accn = frame["ACCN"]
name = frame["binomial_name"]
lat = frame["latitude"]
lon = frame["longitude"]

#biom = frame["bioms"]
#anthrome = frame["anthromes"]
#litter_size = frame["litter_size"]
#bodymass = frame["adult_body_mass_g"]
#lifespan = frame["max_life_span_m"]
#order = frame["order_cat"]
#iucn = frame["IUCN_cat"]
pop = frame["group"]

# grouping by biom
#for i in range(len(name)):
    #name0 = name[i]
    #lat0 = lat[i]
    #lon0 = lon[i]
    #biom0 = biom[i]
    #out = open("%s%s.coords"%(output_biom,name0),"a")
    #out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%biom0 + "\n")
    #out.close()
#
# # grouping by anthrome
#for i in range(len(name)):
    #name0 = name[i]
    #lat0 = lat[i]
    #lon0 = lon[i]
    #anthrome0 = anthrome[i]
    #out = open("%s%s.coords"%(output_anthrome,name0),"a")
    #out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%anthrome0 + "\n")
    #out.close()

# # grouping by littersize
#for i in range(len(name)):
    #name0 = name[i]
    #lat0 = lat[i]
    #lon0 = lon[i]
    #litter_size0 = litter_size[i]
    #out = open("%s%s.coords"%(output_litter_size,name0),"a")
    #out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%litter_size + "\n")
    #out.close()
#
# # grouping by bodymass
#for i in range(len(name)):
 #   name0 = name[i]
  #  lat0 = lat[i]
   # lon0 = lon[i]
    #bodymass0 = bodymass[i]
    #out = open("%s%s.coords"%(output_bodymass,name0),"a")
    #out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%bodymass0 + "\n")
    #out.close()
#
# # grouping by lifespan
#for i in range(len(name)):
 #   name0 = name[i]
  #  lat0 = lat[i]
   # lon0 = lon[i]
    #lifespan0 = lifespan[i]
    #out = open("%s%s.coords"%(output_lifespan,name0),"a")
    #out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%lifespan0 + "\n")
    #out.close()

# grouping by iucn
#for i in range(len(name)):
 #   name0 = name[i]
  #  lat0 = lat[i]
   # lon0 = lon[i]
    #iucn0 = iucn[i]
    #out = open("%s%s.coords"%(output_iucn,name0),"a")
    #out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%iucn0 + "\n")
    #out.close()
#
# # grouping by order
#for i in range(len(name)):
 #   name0 = name[i]
  #  lat0 = lat[i]
   # lon0 = lon[i]
   # order0 = order[i]
    #out = open("%s%s.coords"%(output_order,name0),"a")
    #out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%order0 + "\n")
    #out.close()

# grouping by population
for i in range(len(name)):
    name0 = name[i]
    lat0 = lat[i]
    lon0 = lon[i]
    pop0 = pop[i]
    out = open("%spop\\%s.coords"%(output_population,name0),"a")
    out.writelines("%s"%lat0 + "\t" + "%s"%lon0 + "\t" + "%s"%pop0 + "\n")
    out.close()

# # group by latitude
# out1 = open("lat1.fasta","w")
# out2 = open("lat2.fasta","w")
# out3 = open("lat3.fasta","w")
# out4 = open("lat4.fasta","w")
# out5 = open("lat5.fasta","w")
# out6 = open("lat6.fasta","w")
# out7 = open("lat7.fasta","w")
# out8 = open("lat8.fasta","w")
# out9 = open("lat9.fasta","w")
# out10 = open("lat10.fasta","w")
# out11 = open("lat11.fasta","w")
# out12 = open("lat12.fasta","w")
# out13 = open("lat13.fasta","w")
# out14 = open("lat14.fasta","w")
# out15 = open("lat15.fasta","w")
# out16 = open("lat16.fasta","w")
# out17 = open("lat17.fasta","w")
# out18 = open("lat18.fasta","w")
#
# for i in range(len(name)):
#     latnum = lat[i]//10 + 10
#     if latnum == 1:
#         out1.writelines(">%s_%s"%(name[i],accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 2:
#         out2.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 3:
#         out3.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 4:
#         out4.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 5:
#         out5.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 6:
#         out6.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 7:
#         out7.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 8:
#         out8.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 9:
#         out9.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 10:
#         out10.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 11:
#         out11.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 12:
#         out12.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 13:
#         out13.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 14:
#         out14.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 15:
#         out15.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 16:
#         out16.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 17:
#         out17.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#     elif latnum == 18:
#         out18.writelines(">%s_%s" % (name[i], accn[i]) + "\n" + seq[i] + "\n")
#
# out1.close()
# out2.close()
# out3.close()
# out4.close()
# out5.close()
# out6.close()
# out7.close()
# out8.close()
# out9.close()
# out10.close()
# out11.close()
# out12.close()
# out13.close()
# out14.close()
# out15.close()
# out16.close()
# out17.close()
# out18.close()