#!/bin/bash
# 25

outputfile=../../outputfiles/ls/ls_l_r.txt
testfile=../../testfiles/ls/ls_l_r.txt

rm -f $outputfile $testfile
touch $outputfile $testfile


python3 ../../../src/main.py ls -R -l verify &> $outputfile
scriptresult=$?

ls -R -l verify | tr -s ' ' | cut -d ' ' -f 1,3,4,5,7,8,9 | grep -v total > output/ls_out

node verify/ls/ls.js output/ls_out $outputfile > $testfile 2>> $outputfile
testresult=$?

rm -f output/.ls_out

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct ls does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult

