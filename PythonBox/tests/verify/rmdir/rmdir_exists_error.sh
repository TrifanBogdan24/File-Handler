#!/bin/bash
# 5

outputfile=../../outputfiles/rmdir/rmdir_exists_error.txt
testfile=../../testfiles/rmdir/rmdir_exists_error.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf futurama

python3 ../../../src/main.py rmdir futurama &> $outputfile
scriptresult=$?

if [ $scriptresult != 196 ]
then
    echo "Command does not fail with exit code -60 when trying to delete a folder that does not exist." > $testfile
    exit -1 
fi

exit 0


