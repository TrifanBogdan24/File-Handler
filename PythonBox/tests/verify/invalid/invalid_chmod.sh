#!/bin/bash
# 10

outputfile=../../outputfiles/invalid/invalid_chmod.txt
testfile=../../testfiles/invalid/invalid_chmod.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

python3 ../../../src/main.py chmod -a file &> $outputfile
scriptresult=$?

echo "Invalid command" > $testfile

diff -q $outputfile $testfile
if [ $? != 0 ]
then
    echo 'Script does not print Invalid command when command is not correct.' > $testfile
    exit -1
else
    if [ $scriptresult != 255 ]
    then
        echo 'Script does not return -1 when command is not correct.' > $testfile
        exit -1
    fi
fi

exit 0


