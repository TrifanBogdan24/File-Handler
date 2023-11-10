#!/bin/bash
# 10

outputfile=../../outputfiles/grep/grep_simple.txt
testfile=../../testfiles/grep/grep_simpple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

examplefile=$outputfile.example

rm -rf output/*

python3 ../../../src/main.py grep www-data /etc/passwd &> $outputfile
scriptresult=$?

if [ $scriptresult == 0 ]
then
    grep www-data /etc/passwd &> $examplefile
    diff -y --suppress-common-lines $examplefile $outputfile &> $testfile
    testresult=$?

    rm -rf $examplefile

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