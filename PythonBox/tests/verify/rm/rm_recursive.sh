#!/bin/bash
# 15

outputfile=../../outputfiles/rm/rm_recursive.txt
testfile=../../testfiles/rm/rm_recursive.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf mickey
mkdir mickey
touch mickey/mouse
touch minnie

python3 ../../../src/main.py rm --recursive mickey minnie &> $outputfile
scriptresult=$?

node verify/rm/rm.js mickey/mouse mickey minnie > $testfile 2>> $outputfile
testresult=$?

rm -rf mickey minnie

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


