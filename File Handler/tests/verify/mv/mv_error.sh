#!/bin/bash
# 5

outputfile=../../outputfiles/mv/mv_error.txt
testfile=../../testfiles/mv/mv_error.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf /bla

python3 ../../../src/main.py mv /bla/bla/bla file &> $outputfile
scriptresult=$?

if [ $scriptresult != 216 ]
then
    echo "Command does not fail with exit code -40." > $testfile
    exit -1 
fi

exit 0