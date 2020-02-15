#!/bin/bash
cd ..
read -p "Which Feature Do You Want To Use?
Enter 1 for FileSize
Enter 2 for FileType
Enter 3 for FIXME.log  " command

if [ $command -eq "2" ]; then
	read -p "Enter a File Extension " type
	num1=$(find -type f -name "*.$type" | wc -l )
	echo "$num1 Files with the extension $type"
elif [ $command -eq "1" ]; then
	find . -type f -not -type d -printf '%s %f\n' |
     sort -nr -k1 |
     while read filesize filename
do
	printf '%s : %s\n' "$(numfmt --to=iec <<< $filesize)" "$filename"
done
elif [ $command -eq "3" ]; then
	find -type f -print0 | while IFS= read -rd '' file; do
	tail -n1 "$file" | grep -q FIXME && echo "$file" > fixme.log
	done

fi
