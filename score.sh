#!/bin/bash

if [ -z $1 ]
then
    echo "Please input text file."
    exit 1
fi

grep ^D $1 | cut -f3- > /tmp/gen.out.sys
grep ^T $1 | cut -f2- > /tmp/gen.out.ref
fairseq-score --sys /tmp/gen.out.sys --ref /tmp/gen.out.ref --sentence-bleu