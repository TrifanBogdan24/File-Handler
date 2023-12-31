#!/bin/bash
# 10

outputfile=../../outputfiles/touch/touch_a.txt
testfile=../../testfiles/touch/touch_a.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf my_super_file
touch my_super_file

sleep 2
python3 ../../../src/main.py touch -a my_super_file &> $outputfile
scriptresult=$?

node verify/touch/touch.js my_super_file a > $testfile 2>> $outputfile
testresult=$?

rm -rf my_super_file

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct touch command does not return 0 exit code." > $testfile
        exit -1 
    fi
else
    echo "Touch -a does not update access time correctly." > $testfile
    exit -1
fi

exit $testresult


