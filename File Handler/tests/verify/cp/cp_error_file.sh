#!/bin/bash
# 5

outputfile=../../outputfiles/cp/cp_error_file.txt
testfile=../../testfiles/cp/cp_error_file.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

python3 ../../../src/main.py cp planet express &> $outputfile
scriptresult=$?

if [ $scriptresult != 166 ]
then
    echo "cp command does not return -90 when trying to copy a non-existent file." > $testfile
    exit -1
fi