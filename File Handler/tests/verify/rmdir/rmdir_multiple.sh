#!/bin/bash
# 5

outputfile=../../outputfiles/rmdir/rmdir_multiple.txt
testfile=../../testfiles/rmdir/rmdir_multiple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf futurama fry bender

mkdir futurama fry bender

python3 ../../../src/main.py rmdir futurama fry bender &> $outputfile
scriptresult=$?

node verify/rmdir/rmdir.js futurama fry bender > $testfile 2>> $outputfile
testresult=$?

rm -df futurama fry bender

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rmdir command does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


