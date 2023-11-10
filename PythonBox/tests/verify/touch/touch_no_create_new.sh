#!/bin/bash
# 10

outputfile=../../outputfiles/touch/touch_no_create_new.txt
testfile=../../testfiles/touch/touch_no_create_new.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf my_super_file

python3 ../../../src/main.py touch my_super_file && rm my_super_file && python3 ../../../src/main.py touch -c my_super_file &> $outputfile
scriptresult=$?

ls my_super_file &> $testfile
testresult=$?

rm -rf my_super_file

if [ $testresult != 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct touch command does not return 0 exit code." > $testfile
        exit -1 
    fi
else
    echo "Touch -c creates new file." > $testfile
    exit -1
fi

exit 0


