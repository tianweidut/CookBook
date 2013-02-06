#!/bin/bash

trap 'rm -f tmp_$$' INT
echo create the file tmp_$$
date > tmp_$$
while [ -f tmp_$$ ];do
    echo File Exists
    sleep 2
done
echo the file no longer exists 

trap INT
echo creatint the file tmp_$$
date > tmp_$$
while [ -f tmp_$$ ]; do
    echo File exist 
    sleep 3
done 
echo never here
exit 0
