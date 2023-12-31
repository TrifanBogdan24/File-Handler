#!/bin/bash
# 10

outputfile=../../outputfiles/touch/touch_m.txt
testfile=../../testfiles/touch/touch_m.txt

rm -f $outputfile $testfile
touch $outputfile $testfile


rm -rf my_super_file
touch my_super_file

sleep 2
python3 ../../../src/main.py touch -m my_super_file &> $outputfile
scriptresult=$?

node verify/touch/touch.js my_super_file m > $testfile 2>> $outputfile
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
    echo "Touch -m does not update modify time correctly." > $testfile
    exit -1
fi

exit $testresult


