#!/bin/bash
# 5

outputfile=../../outputfiles/echo/echo_spaces.txt
testfile=../../testfiles/echo/echo_spaces.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

python3 ../../../src/main.py echo "lorem ipsum" &> $outputfile
scriptresult=$?
echo "lorem ipsum" > $testfile
testresult=$?
diff -q $outputfile $testfile

if [ $? != 0 ]
then
    echo 'echo does not print complex argument. Check output below.' > $testfile
    exit -1 
fi

if [ $scriptresult != $testresult ]
then
    echo "Echo does not return $testresult exit code." > $testfile
    exit -1  
fi

exit 0