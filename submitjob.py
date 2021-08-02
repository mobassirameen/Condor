
import os
from os import system, environ

#os.system("tar --exclude='tar' -zcf ./tar/CMSSW.tar.gz -C $CMSSW_BASE .")
#os.system("tar --exclude='tar' -zcf ./tar/bctodsmumu_analysis.tar.gz -C /uscms/home/ckar/nobackup/BCTODSMUMU/CMSSW_10_2_18/src/ .")
#os.system("tar --exclude='tar' -zcf ./tar/bctodsmumu-analysis.tar.gz -C /afs/cern.ch/user/m/moameen/CondorSubMCBcToDsMuMu/CMSSW_10_6_12/src/ .")
#print "...done."

submitFileTT="""
universe              = vanilla
Executable            = process_singlecandtree_phimm.sh
Requirements = OpSys=="LINUX"&&(Arch!="DUMMY")

Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files  = bctodsmumu-analysis.tar.gz, BcToDsMuMuRootupler_mod.py


x509userproxy         = x509up_u137722
request_cpus = 8
+JobFlavour = "tomorrow"

+maxWallTime          = 2880
RequestMemory         = 8000
RequestDisk           = 15000

"""
fileParts = [submitFileTT]

#system('mkdir -p logs')
system('mkdir -p Bsmini1')
#files = open("BcToDsMuMu_mc_miniAOD_v1.log","r")
files = open("test.log","r")
#count = 1
count = 0
#for ij in range(1,7):
for ij in files:
    #count = (ij-1)* 1e6
    #toProcess = 1e6
    #count += 1
    #fileParts.append("error = logs/postprocess_{}_$(Cluster)_$(Process).stderr\n".format(count))
    #fileParts.append("Log = logs/postprocess_{}_$(Cluster)_$(Process).log\n".format(count))
    #fileParts.append("Arguments ={} {}\n".format( count,toProcess))
    #fileParts.append("Arguments ={0} {1}\n".format(ij.strip(),count)) 
    #fileParts.append("Queue\n\n")

    #fout = open("condor_sub_Jpsi_{0}.txt".format(ij),"w")
    #fout.write(''.join(fileParts))
    #fout.close()
    #fileParts.pop(-1)
    #fileParts.pop(-1)
    #fileParts.pop(-1)
    #fileParts.pop(-1)
    #system('condor_submit condor_sub_Jpsi_%i.txt' % ij)
    #system('condor_submit condor_sub_Jpsi_%i.txt' % count)
    
#files.close()
    fileParts.append("error = Bsmini1/jobDs_{0}_$(Cluster)_$(Process).stderr\n".format(count))
    fileParts.append("Log = Bsmini1/jobDs_{0}_$(Cluster)_$(Process).log\n".format(count))
    fileParts.append("output = Bsmini1/jobDs_{0}_$(Cluster)_$(Process).stdout\n".format(count))
    fileParts.append("Arguments ={0} {1}\n".format(ij.strip(),count))
    fileParts.append("Queue\n\n")

    fout = open("condor_sub_Bs_{0}.txt".format(count),"w")
    fout.write(''.join(fileParts))
    fout.close()
    fileParts.pop(-1)
    fileParts.pop(-1)
    fileParts.pop(-1)
    fileParts.pop(-1)
    fileParts.pop(-1)
    system('condor_submit condor_sub_Bs_%i.txt' % count)

files.close()
