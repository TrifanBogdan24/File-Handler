#!/bin/bash
# 10

outputfile=../../outputfiles/cp/cp_error_dir.txt
testfile=../../testfiles/cp/cp_error_dir.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf output
mkdir output

mkdir planet

python3 ../../../src/main.py cp planet output/express &> $outputfile
scriptresult=$?

rm -rf planet

if [ $scriptresult != 166 ]
then
    echo "cp command does not return -90 when trying to copy a directory without -r parameter." > $testfile
    exit -1
fi