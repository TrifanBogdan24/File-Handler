#!/bin/bash
# 15

outputfile=../../outputfiles/rm/rm_multiple_mixed.txt
testfile=../../testfiles/rm/rm_multiple_mixed.txt

rm -f $outputfile $testfile
touch $outputfile $testfile


touch mickey
mkdir pluto

python3 ../../../src/main.py rm -R mickey pluto &> $outputfile
scriptresult=$?

node verify/rm/rm.js mickey pluto > $testfile 2>> $outputfile
testresult=$?

rm -rf mickey pluto

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


