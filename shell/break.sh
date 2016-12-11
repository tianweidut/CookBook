#!/bin/bash
rm -rf frad*
echo test > frad1
echo test > frad2
mkdir frad3
echo test > frad4

for file in fra*
do
    if [ -d "$file" ];then
        break
    fi
done

echo Now the delete file "$file"

rm -rf frad*

exit 0
