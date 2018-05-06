#!/bin/bash

pyHAsm="./pyHackAssembler/scripts/pyHAsm"

folders=( "add" "max" "rect" "pong" )
for folder in ${folders[@]}
do
    for infile in $(find $folder -type f -name "*.asm")
    do
        name=$(basename -- "$infile")
        name=${name%.*}
        outfile="my_hack_file/$name.hack"
        echo "Process $infile and output to $outfile ..."
        pyHAsm -o $outfile $infile
    done
done
