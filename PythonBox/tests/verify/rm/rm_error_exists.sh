#!/bin/bash
# 5

outputfile=../../outputfiles/rm/rm_error_exists.txt
testfile=../../testfiles/rm/rm_error_exists.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf mickey

python3 ../../../src/main.py rm mickey &> $outputfile
scriptresult=$?


if [ $scriptresult != 186 ]
then
    echo "Command does not fail with exit code -70 when trying to remove a non-existing file/directory." > $testfile
    exit -1 
fi

exit 0


