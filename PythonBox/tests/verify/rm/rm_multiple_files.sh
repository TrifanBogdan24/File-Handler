#!/bin/bash
# 5

outputfile=../../outputfiles/rm/rm_multiple_Files.txt
testfile=../../testfiles/rm/rm_multiple_files.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf mickey "minnie mouse"

touch mickey "minnie mouse"
python3 ../../../src/main.py rm mickey "minnie mouse" &> $outputfile
scriptresult=$?

node verify/rm/rm.js mickey "minnie mouse" > $testfile 2>> $outputfile
testresult=$?

rm -f mickey "minnie mouse"

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult


