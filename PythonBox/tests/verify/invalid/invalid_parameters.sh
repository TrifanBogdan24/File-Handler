#!/bin/bash
# 5

outputfile=../../outputfiles/invalid/invalid_parameters.txt
testfile=../../testfiles/invalid/invalid_parameters.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

python3 ../../../src/main.py ln -a file file &> $outputfile
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


