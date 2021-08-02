#! /bin/bash

export RECREL=CMSSW_10_6_12
export SCRAM_ARCH=slc7_amd64_gcc700

export FILE1=file:root://se01.indiacms.res.in:1094//cms/store/user/moameen/BcDsMuMu_mc_miniAOD_7jul2021/$1
#export FILE2="BCToDSMuMu-2018B_MINIAOD_$1.root"
export FILE2="BcToDsMuMu-Ntuple_newMC_$2.root"


echo "========================"
echo "====> SGE  wrapper <===="
echo "========================"

echo "--> Running SGE digi-reco job wrapper"

echo $FILE1
echo $FILE2


# ----------------------------------------------------------------------
# -- The Basics
# ----------------------------------------------------------------------
echo "--> Environment"
date
hostname
uname -a
df -kl
limit coredumpsize 0

source /cvmfs/cms.cern.ch/cmsset_default.sh
echo "-> which edg-gridftp-ls"
which edg-gridftp-ls
echo "-> which globus-url-copy"
which globus-url-copy
echo "-> which srmcp"
which srmcp

pwd
echo "--> End of env testing"

# BATCH START

# ----------------------------------------------------------------------
# -- Setup CMSSW
# ----------------------------------------------------------------------
echo "--> Setup CMSSW"
pwd
date
eval `scramv1 project CMSSW CMSSW_10_6_12`
#cmsrel CMSSW_10_6_12

cd CMSSW_10_6_12/src/
#tar -zxvf ../../bctodsmumu_analysis.tar.gz
tar -zxvf ../../bctodsmumu-analysis.tar.gz


ls -ltr
eval `scramv1 runtime -sh`
pwd

scramv1 b ProjectRename
#scramv1 b clean
#scramv1 b myanalyzer
#cmsenv

scramv1 b

cd bctodsmumu_analysis/BcToDsMuMuPAT/test/
#cp ../../../../../BcToDsMuMuRootupler_mod.py
cp ../../../../../BcToDsMuMuRootupler_mod.py

cmsRun BcToDsMuMuRootupler_mod.py

ls -rtl

#xrdcp -f BCToDSMuMu-2018B_MINIAOD_$1.root root://cmseos.fnal.gov//eos/uscms/store/user/ckar/BsToJpsiPhi_Condor/BCToDSMuMu-2018B_MINIAOD_$1.root
xrdcp -f BcToDsMuMu-Ntuple_newMC_$2.root root://se01.indiacms.res.in:1094//cms/store/user/moameen/New_mc_Ntuple/BcToDsMuMu-Ntuple_newMC_$2.root


# BATCH END

echo "run: This is the end, my friend"
cd ${_CONDOR_SCRATCH_DIR}
rm -rf CMSSW_10_6_12
