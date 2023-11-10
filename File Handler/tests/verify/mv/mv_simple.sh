#!/bin/bash
# 5

outputfile=../../outputfiles/mv/mv_simple.txt
testfile=../../testfiles/mv/mv_simple.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf output/*

echo "bender bending rodriguez" > mvbender
echo echo "bender bending rodriguez" > output/testmv

python3 ../../../src/main.py mv mvbender output/bender &> $outputfile
scriptresult=$?

ls mvbender &> $testfile
testresult=$?

rm -f mvbender

if [ $testresult != 0 ]
then
    ls output/bender &> $testfile
    testresult=$?
    if [ $testresult == 0 ]
    then
        diff -q output/testmv output/bender
        testresult=$?
            
        rm -f output/*

        if [ $testresult == 0 ]
        then
            if [ $scriptresult != 0 ]
            then
                echo "Correct mv command does not return 0 exit code." > $testfile
                 exit -1 
            fi
        else
            echo "Destination file does not match source file." > $testfile
        fi
    else
        rm -rf output/*
        echo "Destination file does not exist." > $testfile
        exit -1
    fi
else
    rm -rf output/*
    echo "Source file still exists." > $testfile
    exit -1
fi
