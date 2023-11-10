#!/bin/bash
# 5

outputfile=../../outputfiles/rmdir/rmdir_empty_error.txt
testfile=../../testfiles/rmdir/rmdir_empty_error.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf futurama

mkdir futurama
touch futurama/bender

python3 ../../../src/main.py rmdir futurama &> $outputfile
scriptresult=$?

rm -rf futurama

if [ $scriptresult != 196 ]
then
    echo "Command does not fail with exit code -60 when trying to delete a folder that is not empty." > $testfile
    exit -1 
fi

exit 0


