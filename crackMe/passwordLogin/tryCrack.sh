#!/bin/bash

declare -a lines=()
mapfile -t lines < <(strings crackme |  egrep -r "\n"* )
for i in lines
do
   : ./crackme "${lines[$i]}"
done
