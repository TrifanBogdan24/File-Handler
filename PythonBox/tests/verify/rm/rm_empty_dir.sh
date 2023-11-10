#!/bin/bash
# 10

outputfile=../../outputfiles/rm/rm_empty_dir.txt
testfile=../../testfiles/rm/rm_empty_dir.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf disney
mkdir disney

python3 ../../../src/main.py rm -d disney &> $outputfile
scriptresult=$?

node verify/rm/rm.js disney > $testfile 2>> $outputfile
testresult=$?

rm -df disney

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


