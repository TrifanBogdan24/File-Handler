#!/bin/bash
# 5

outputfile=../../outputfiles/touch/touch_simple.txt
testfile=../../testfiles/touch/touch_simple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf my_super_file
python3 ../../../src/main.py touch my_super_file > $outputfile 2>&1
scriptresult=$?

ls my_super_file > $testfile 2>&1
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
    echo "Touch on new file does not create it." > $testfile
    exit -1
fi

exit $testresult


