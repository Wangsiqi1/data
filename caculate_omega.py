from Bio.Phylo.PAML import codeml
import os

# input dir
seqpath = "D:\\paml\\cal\\"
treepath = "D:\\paml\\cal_tree\\"
resultpath = "D:\\paml\\result\\"

# cal
names=os.listdir(seqpath)
cml = codeml.Codeml()

# options
cml.set_options(runmode = 0)
cml.set_options(verbose = 1)
cml.set_options(noisy = 4)
cml.set_options(seqtype = 1)
cml.set_options( CodonFreq = 0)
cml.set_options( model = 0)
cml.set_options(icode = 0)
cml.set_options(clock = 0)
cml.set_options(getSE = 0)
cml.set_options(RateAncestor = 0)
cml.set_options(fix_alpha = 1)
cml.set_options(fix_omega = 0)
cml.set_options(fix_kappa = 0)
cml.set_options(kappa = 2,omega = 0.4,alpha = 0,Malpha = 0,ncatG = 5,fix_blength = 0)
cml.set_options(Small_Diff = 5e-7)
cml.set_options(cleandata = 0)
cml.set_options(method = 0)
cml.set_options(Mgene = 0)
cml.set_options(ndata = 1)
cml.set_options(aaDist = 0)
cml.set_options(CodonFreq = 0)

ind = 0
for i in names:
    ind = ind + 1
    # m1,m2,m3
    cml.working_dir = "D:\\paml\\paml4.9g\\bin\\"
    cml.ctl_file = "D:\\paml\\ctl_file\\codeml.ctl"
    cml.alignment = "%s%s"%(seqpath,i)

    cml.tree = "%s%s.DND"%(treepath,i[:-6])    # 正常
    #cml.tree = "%s%s.DND" % (treepath, i[4:-6])    # abs

    cml.out_file = "%s123_%s.txt"%(resultpath,i[:-6])
    cml.set_options(NSsites=[0, 1, 2])  # m7 and m8 cannot cal at the same time
    results = cml.run(verbose=True)
    # m7
    cml.out_file = "%s7_%s.txt"%(resultpath,i[:-6])
    cml.set_options(NSsites=[7])  # m7 and m8 cannot cal at the same time
    results2 = cml.run(verbose=True)

    # m7
    cml.out_file = "%s8_%s.txt"%(resultpath,i[:-6])
    cml.set_options(NSsites=[8])  # m7 and m8 cannot cal at the same time
    results3 = cml.run(verbose=True)
    print("------------------------------------------finish %s--------------------------------------------------"%ind)








