#!/bin/bash

yes_or_no()
{
    echo "Is your name $* ?"
    while true
    do
        echo -n "Enter yes or no: "
        read x
        
        case "$x" in
            y|yes) return 0;;
            n|no) return 1;;
            *) echo "Answer yes or no";;
        esac
    done
}

echo "original parameters are $* "
if yes_or_no "$1"
then
    echo "Hi $1 ,nice name"
else
    echo "Never Mind"
fi

exit 0
