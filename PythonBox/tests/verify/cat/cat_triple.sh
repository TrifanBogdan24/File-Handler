#!/bin/bash
# 5

outputfile=../../outputfiles/cat/cat_triple.txt
testfile=../../testfiles/pwd/cat_trile.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf output/* 

echo "donuts" > output/homer
echo "ay caramba" > output/bart
echo "donuts" > output/cat_reference
echo "ay caramba" >> output/cat_reference
cat /etc/passwd >> output/cat_reference

python3 ../../../src/main.py cat output/homer output/bart /etc/passwd &> $outputfile
scriptresult=$?

if [ $scriptresult == 0 ]
then
    diff -y --suppress-common-lines output/cat_reference $outputfile &>> $testfile
    testresult=$?

    rm -rf output/*

    if [ $testresult != 0 ]
    then
        echo "Incorrect output."
        exit -1
    fi
else
    rm -rf output/*
    echo "Command does not return 0 ($scriptresult)." >> $testfile
    exit -1
fi