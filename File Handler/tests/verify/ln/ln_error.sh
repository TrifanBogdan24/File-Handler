#!/bin/bash
# 5

outputfile=../../outputfiles/ln/ln_error.txt
testfile=../../testfiles/ln/ln_error.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf lndir
mkdir lndir

python3 ../../../src/main.py ln lndir ln_lndir &> $outputfile
scriptresult=$?

rmdir lndir

if [ $scriptresult != 206 ]
then
    echo "Command does not fail with exit code -50." > $testfile
    exit -1 
fi

exit 0