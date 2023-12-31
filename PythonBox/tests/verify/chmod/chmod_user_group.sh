#!/bin/bash
# 20

outputfile=../../outputfiles/chmod/chmod_user_group.txt
testfile=../../testfiles/chmod/chmod_user_group.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf my_super_file my_ref_file
touch my_super_file
touch my_ref_file

chmod ug+x my_ref_file

python3 ../../../src/main.py chmod ug+x my_super_file &> $outputfile
scriptresult=$?

node verify/chmod/chmod.js my_super_file my_ref_file > $testfile 2>> $outputfile
testresult=$?

rm -rf my_super_file my_ref_file

if [ $testresult == 0 ]
then
    if [ $scriptresult != 0 ]
    then
        echo "Correct chmod command does not return 0 exit code." > $testfile
        exit -1 
    fi
else
    echo "Chmod does not set correct permissions." > $testfile
    exit -1
fi

exit $testresult


