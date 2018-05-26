#!/bin/bash

pyVMTrans="../pyVMTranslator/VMTranslator.py"

folders=( "SimpleAdd" "StackTest" )
for folder in ${folders[@]}
do
    for infile in $(find $folder -type f -name "*.vm")
    do
        name=$(basename -- "$infile")
        name=${name%.*}
        outfile="$folder/$name.asm"
        echo "Process $infile and output to $outfile ..."
        $pyVMTrans -o $outfile $infile
    done
done
