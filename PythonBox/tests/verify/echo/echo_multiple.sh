#!/bin/bash
# 5

outputfile=../../outputfiles/echo/echo_multiple.txt
testfile=../../testfiles/echo/echo_multiple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

python3 ../../../src/main.py echo lorem ipsums &> $outputfile
scriptresult=$?
echo lorem ipsums > $testfile
testresult=$?
diff -q $outputfile $testfile
if [ $? != 0 ]
then
    echo 'echo does not print multiple arguments. Check output below.' > $testfile
    exit -1 
fi

if [ $scriptresult != $testresult ]
then
    echo "Echo does not return $testresult exit code." > $testfile
    exit -1  
fi

exit 0