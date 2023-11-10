#!/bin/bash
# 5

outputfile=../../outputfiles/mkdir/mkdir_simple.txt
testfile=../../testfiles/mkdir/mkdir_simple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf out_dir

python3 ../../../src/main.py mkdir out_dir &> $outputfile
scriptresult=$?

node verify/mkdir/mkdir.js out_dir > $testfile 2>> $outputfile
testresult=$?

rm -df out_dir

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct mkdir does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult