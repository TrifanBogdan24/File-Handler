#!/bin/bash
# 5

outputfile=../../outputfiles/mkdir/mkdir_path_multiple.txt
testfile=../../testfiles/mkdir/mkdir_path_multiple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

DIR=`pwd`

rm -rf output/*
python3 ../../../src/main.py mkdir output/harry  $DIR/output/potter &> $outputfile
scriptresult=$?

node verify/mkdir/mkdir.js output/harry $DIR/output/potter > $testfile
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


