#!/bin/bash
# 5

outputfile=../../outputfiles/ls/ls_err.txt
testfile=../../testfiles/ls/ls_err.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf /bla

python3 ../../../src/main.py ls /bla/bla/bla &> $outputfile
scriptresult=$?

if [ $scriptresult != 176 ]
then
    echo "Command does not fail with exit code -80." > $testfile
    exit -1 
fi

exit 0