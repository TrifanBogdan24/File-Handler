#!/bin/bash
# 5

outputfile=../../outputfiles/echo/echo_newline_multiple.txt
testfile=../../testfiles/echo/echo_newline_multiple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

python3 ../../../src/main.py echo -n ana are mere &> $outputfile
scriptresult=$?
echo -n ana are mere > $testfile
testresult=$?
diff -q $outputfile $testfile
if [ $? != 0 ]
then
    echo 'echo -n does not print multiple arguments correctly. Check output below.' > $testfile
    exit -1 
fi

if [ $scriptresult != $testresult ]
then
    echo "Echo does not return $testresult exit code." > $testfile
    exit -1  
fi

exit 0
