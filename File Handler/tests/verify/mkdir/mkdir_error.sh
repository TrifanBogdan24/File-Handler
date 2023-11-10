#!/bin/bash
# 5

outputfile=../../outputfiles/mkdir/mkdir_error.txt
testfile=../../testfiles/mkdir/mkdir_error.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

DIR=`pwd`

rm -rf /bla

python3 ../../../src/main.py mkdir /bla/bla/bla &> $outputfile
scriptresult=$?

if [ $scriptresult != 226 ]
then
    echo "Command does not fail with exit code -30." > $testfile
    exit -1 
fi

exit 0
