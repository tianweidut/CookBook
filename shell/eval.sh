#!/bin/sh
foo=10
x=foo
y='$'$x
echo y
echo "$y"

eval y='$'$x
echo "$y"

echo the date is $(date)
set $(date)
echo the month is $2
echo the day is $3
