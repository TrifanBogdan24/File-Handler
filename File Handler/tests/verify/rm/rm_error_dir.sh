#!/bin/bash
# 10

outputfile=../../outputfiles/rm/rm_error_dir.txt
testfile=../../testfiles/rm/rm_error_dir.txt

rm -f $outputfile $testfile
touch $outputfile $testfile

rm -rf goofy

mkdir goofy
touch pluto

python3 ../../../src/main.py rm goofy pluto &> $outputfile
scriptresult=$?

if [ $scriptresult != 186 ]
then
    echo "Command does not fail with exit code -70 when directory tries to be removed without -d or -r option." > $testfile
    rm -rf goofy pluto
    exit -1
else
    node verify/rm/rm.js pluto > $testfile 2>> $outputfile
    testresult=$?
    if [ $testresult != 0 ]
    then
        echo "File is not removed." > $testfile
        rm -rf goofy pluto
        exit -1
    else
        node verify/rm/rm.js goofy > $testfile 2>> $outputfile
        testresult=$?
        if [ $testresult == 0 ]
        then
            echo "Command did not fail to remove directory without -d or -r option." > $testfile
            rm -rf goofy pluto
            exit -1
        fi
    fi
fi

rm -rf goofy pluto

exit 0

