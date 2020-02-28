#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd ..

read -p "Which Feature Do You Want To Use?
Enter 1 for FileSize

Enter 2 for FileType

Enter 3 for FIXME.log

Enter 4 for Git Checkout Latest Merge

Enter 5 for Find Tag

Enter 6 for Backup/Restore

Enter 7 For Football Mini Game

Enter 8 for Delete Duplicate File  " command

if [ $command -eq "2" ]; then
	read -p "Enter a File Extension " type
	num1=$(find  -type f -name "*.$type" | wc -l )
	echo "$num1 Files with the extension $type"
elif [ $command -eq "1" ]; then
	find . -type f -not -type d -printf '%s %f\n'|
        sort -nr -k1 |
        while read filesize filename
do
        printf '%s : %s\n' "$(numfmt --to=iec <<< $filesize)" "$filename"
done
elif [ $command -eq "3" ]; then
	if [ -f ~/CS1XA3/Project01/fixme.log ]; then
		rm ~/CS1XA3/Project01/fixme.log
		touch ~/CS1XA3/Project01/fixme.log
		echo ""
		echo "fixme.log Created"
		echo ""
	else
		touch ~/CS1XA3/Project01/fixme.log

	fi
	find  -type f -print0 | while IFS= read -rd '' file; do
	tail -n1 "$file" | grep -q FIXME && echo "$file" >> ~/CS1XA3/Project01/fixme.log
	done

elif [ $command -eq "4" ]; then

	tempfile1=$(mktemp)
	echo ""
	echo "Checking out latest merge..."
	echo ""
	git log --oneline | grep -i merge -m 1 | cut -d " " -f 1 >> $tempfile1
	git checkout $(cat "$tempfile1")

elif [ $command -eq "5" ]; then

	read -p "Please Enter a Tag (any single word) " tag
	newDIR=~/CS1XA3
	file2=~/CS1XA3/Project01/$tag.log

	if [ -f "$file2" ]; then
		rm $file2
		touch $file2
	else
		touch $file2
	fi

	find  -type f -name "*.py" -print0 | while IFS= read -rd '' file; do

	grep "#" $file | grep "$tag" >> $file2

	done

elif [ $command -eq "6" ]; then

	read -p "Please choose an option
	1 for backup
	2 for restore : " choice
	backupdir=~/CS1XA3/Project01/backup
	if [ $choice -eq "1" ]; then

		if [ -d "$backupdir" ]; then
			rm -r ~/CS1XA3/Project01/backup/*
			echo ""
			echo "backup Directory emptied"
		else

			mkdir $backupdir
			echo " "
			echo  "backup directory created"
		fi

	touch ~/CS1XA3/Project01/backup/restore.log

	find -type f -name "*.tmp" -print0 | while IFS= read -rd '' file; do

	echo "$file" >> ~/CS1XA3/Project01/backup/restore.log
	cp $file ~/CS1XA3/Project01/backup
	rm $file
	done

	elif [ $choice -eq "2" ]; then

		echo ""
		echo "Time to Restore..."
		echo ""

		if [ -f ~/CS1XA3/Project01/backup/restore.log ]; then

			cat ~/CS1XA3/Project01/backup/restore.log | while read line || [[ -n $line ]]; do

			touch "$line"
			done
		else
			echo""
			echo " ERROR: restore.log does not exist "
			echo ""
		fi



	fi

elif [ $command -eq "7" ]; then



	attempts=9
	total=0

	echo "1 for Long Pass"
	echo "2 for Medium Pass"
	echo "3 for Short Pass"

	while [ "$total" -le 100 ]; do

		counter=$(( 100 - total ))
		echo "$counter Yards until you win"
		echo ""
		read -p "Enter A Play " play

		if [ $play -eq "1" ]; then

			if [ $attempts -le 1 ]; then
				break
			else

				rand=$(( ( RANDOM % 100 ) + 1 ))

   				if [ "$rand" -ge 53 ]; then
        			pass1=$(( ( RANDOM % 25) + 15 ))
					total=$(( pass1 + total ))
					attempts=$(( attempts - 1 ))
					echo ""
					echo "Pass COMPLETE for $pass1 Yards!"
					echo ""
					echo "$attempts downs left!"
					echo  ""
				else
					attempts=$(( attempts - 1 ))
					echo ""
					echo "Pass Incomplete"
					echo ""
					echo "$attempts downs left!"
					echo ""
				fi
 			fi
		elif [ $play -eq "2" ]; then

			if [ $attempts -le 1 ]; then
				break
			else

				rand2=$(( ( RANDOM % 100 ) + 1 ))

				if [ $rand2 -ge 43 ]; then

					play2=$(( (RANDOM % 15) + 8 ))
					attempts=$((attempts - 1 ))
					total=$(( total + play2 ))
					echo ""
					echo "Pass COMPLETE!"
					echo "You Gained $play2 Yards!"
					echo ""
					echo "$attempts downs left!"
					echo ""

				else

					attempts=$(( attempts - 1 ))
					echo ""
					echo " Pass Incomplete "
					echo ""
					echo " $attempts downs left"
					echo ""
				fi



			fi

		elif [ $play -eq "3" ]; then

			if [ $attempts -le 1 ]; then
				break
			else

				rand3=$(( ( RANDOM % 100 ) + 1 ))

				if [ $rand3 -ge 15 ]; then

					play3=$(( ( RANDOM % 13 ) + 1 ))
					total=$(( total + play3 ))
					attempts=$(( attempts - 1 ))
					echo ""
					echo " Pass COMPLETE!"
					echo "You Gained $play3 yards!"
					echo "$attempts plays left!"
					echo ""
				else

					attempts=$(( attempts - 1 ))
					echo ""
					echo "Pass Incomplete"
					echo "$attempts plays left"
					echo ""
				fi

			fi
		fi

	done

	if [ $total -ge 99 ]; then

		echo ""
		echo " TOUCHDOWN !!!!!!!"
		echo " You win the game!"
	elif [ $attempts -le 1 ]; then

		echo ""
		echo ""
		echo " GAME OVER! BETTER LUCK NEXT TIME"
		echo " thanks for playing"

	fi


elif [ $command -eq "8" ]; then
	cd $DIR
	find . -type f | xargs md5sum | sort -k1,1 | uniq -Dw32

	echo ""
	echo "These are files that have duplicates"
	read -p "Please enter 1 IF and ONLY you want to delete one of the duplicates : " choice

	if [ $choice -eq "1" ]; then

		find  . -type f \
		    | xargs md5sum \
		    | sort -k1,1 \
                    | uniq -Dw32 \
		    | while read hash file; do
			[ "${prev_hash}" == "${hash}" ] && rm -v "${file}"
			prev_hash="${hash}";
		    done

	else

	echo "Cancelled"

	fi




fi
