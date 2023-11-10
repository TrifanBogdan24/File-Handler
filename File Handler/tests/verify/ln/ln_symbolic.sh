#!/bin/bash
# 10

outputfile=../../outputfiles/ln/ln_symbolic.txt
testfile=../../testfiles/ln/ln_symbolic.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

echo "planet express" > lnfile

python3 ../../../src/main.py ln --symbolic lnfile ln_lnfile &> $outputfile
scriptresult=$?

node verify/ln/ln.js sym lnfile ln_lnfile > $testfile 2>> $outputfile
testresult=$?

rm -f lnfile
rm -f ln_lnfile

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct ln command does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult