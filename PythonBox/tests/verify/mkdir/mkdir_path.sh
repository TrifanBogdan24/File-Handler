#!/bin/bash
# 5

outputfile=../../outputfiles/mkdir/mkdir_path.txt
testfile=../../testfiles/mkdir/mkdir_path.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf output/*

python3 ../../../src/main.py mkdir output/harry &> $outputfile
scriptresult=$?

node verify/mkdir/mkdir.js output/harry > $testfile
testresult=$?

rm -df output/harry $DIR/output/potter

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct mkdir does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


