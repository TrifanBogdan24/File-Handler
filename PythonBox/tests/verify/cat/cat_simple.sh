#!/bin/bash
# 5

outputfile=../../outputfiles/cat/cat_simple.txt
testfile=../../testfiles/cat/cat_simple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf output/*

python3 ../../../src/main.py cat /etc/passwd &> $outputfile
scriptresult=$?

if [ $scriptresult == 0 ]
then
    diff -y --suppress-common-lines /etc/passwd $outputfile &> $testfile
    testresult=$?

    rm -rf output/*

    if [ $testresult != 0 ]
    then
        echo "Incorrect output."
        exit -1
    fi
else
    rm -rf output/*
    echo "Command does not return 0 ($scriptresult)." > $testfile
    exit -1
fi
