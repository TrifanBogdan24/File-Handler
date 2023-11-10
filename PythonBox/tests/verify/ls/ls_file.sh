#!/bin/bash
# 5

outputfile=../../outputfiles/ls/ls_file.txt
testfile=../../testfiles/ls/ls_file.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf lstest
mkdir lstest
touch lstest/test

python3 ../../../src/main.py ls lstest/test &> $outputfile
scriptresult=$?

rm -rf lstest

echo "lstest/test" > $testfile

diff -q $outputfile $testfile
if [ $? != 0 ]
then
    echo 'ls does not print file passed as parameter' > $testfile
    exit -1 
fi

exit 0


