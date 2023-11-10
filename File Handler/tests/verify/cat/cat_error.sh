#!/bin/bash
# 5

outputfile=../../outputfiles/cat/cat_error.txt
testfile=../../testfiles/cat/cat_error.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf /fake

python3 ../../../src/main.py cat /fake &> $outputfile
scriptresult=$?

if [ $scriptresult != 236 ]
then
    echo "cat command does not return -20 when trying to print a non-existing file." > $testfile
    exit -1
fi