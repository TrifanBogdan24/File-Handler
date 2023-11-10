#!/bin/bash
# 15

outputfile=../../outputfiles/rm/rm_cascade.txt
testfile=../../testfiles/rm/rm_cascade.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf disney

mkdir disney
mkdir disney/mickey
touch disney/mickey/mouse
touch "disney/minnie mouse"
touch pixar

python3 ../../../src/main.py rm -R -d disney pixar &> $outputfile
scriptresult=$?

node verify/rm/rm.js disney/mickey/mouse disney/mickey "disney/minnie mouse" disney pixar> $testfile 2>> $outputfile
testresult=$?

rm -rf disney pixar

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct rm does not return 0 exit code." > $testfile
        exit -1 
    fi
fi

exit $testresult