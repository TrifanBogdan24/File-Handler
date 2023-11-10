#!/bin/bash
# 10

outputfile=../../outputfiles/cp/cp_simple_file.txt
testfile=../../testfiles/cp/cp_simple_file.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf output
mkdir output


python3 ../../../src/main.py cp /etc/passwd output &> $outputfile
scriptresult=$?

ls output/passwd &> $testfile
testresult=$?

if [ $testresult == 0 ]
then
    diff -q /etc/passwd output/passwd
    testresult=$?
    
    rm -rf output/*

    if [ $testresult == 0 ]
    then
        if [ $scriptresult != 0 ]
        then
            echo "Correct ln command does not return 0 exit code." > $testfile
            exit -1 
        fi
    else
        echo "Destination file is different from output file." > $testfile
    fi
    exit $testresult

else
    rm -rf output/*
    echo "Destination file does not exist." > $testfile
    exit -1
fi
