# CS 1XA3 PROJECT01 - mooret12


## Usage

	Execute this script from project root with:
        chmod +x ./CS1XA3/Project01/project_analyze
        You will be prompted to enter either 1 , 2 or 3.
        entering 1 and hitting enter will execute feature 1 (file size list)
        entering 2 and hitting enter will execute feature 2 (file extension)
        entering 3 and hitting enter will execute feature 3 (FIXME log)
        entering 4 and hitting enter will execute feature 4 (Git Checkout)
        entering 5 and hitting enter will execute feature 5 (Find Tag)
        entering 6 and hitting enter will execute feature 6 (Backup/Restore)
        entering 7 and hitting enter will execute feature 7 (Mini Football Game)
        entering 8 and hitting enter will execute feature 8 (Delete duplicate files)
        the program will terminate after executing a feature,
        run it again to use other features


## Feature 01 - 6.4 File Size List 

This feature lists all the files in the repo in a human readable format
To execute this feature, just type 1 at the beginning prompt when you
first execute the file.
some code was taken from

[[https://stackoverflow.com/questions/60229408/can-i-use-stat-to-show-human-readable
-size-of-file/60230608#60230608]]

## Feature 02 - 6.5 File Type Count

This feature outputs the number of files with the extension that
the user inputs.
Execution
first input 2 at the start of the script. You will then be prompted
to enter a extension.
For example :
to get .sh files
enter: sh

code from
 
[[https://askubuntu.com/questions/333710/how-to-find-all-files-with-the-same-extension-within-a-directory]]
[[https://stackoverflow.com/questions/25693638/recursively-find-files-with-a-specific-extension/25694217]


## Feature 03 - 6.2 FIXME log

This feature will find every file in the repo that has the word
FIXME in the last line. It will list the files that contain the
message in a file named fixme.log
execution: just follow prompt at start of the script and enter
3

some code from [[https://stackoverflow.com/questions/60217860/how-to-find-
every-file-in-my-repo-that-has-a-specific-word-in-the-last-line]

## Feature 04 - Checkout Latest Merge 

This feature finds the most recent commit with the word merge in the commit message
it checkouts that commit
The code uses grep -i to make sure the word merge is case insensitive 
execution: just follow prompt at start of the script and enter
4

## Feature 05 - Find Tag 

This Feature prompts the user to input a Tag.
Input any single word.
it will make a log and for each python file that has comment lines with the tag
you put in it will include them in the tag.log.
The code finds all files with extension ".py" then uses grep to find
hashes and then the "tag" word. It uses >> to put the matches into the 
tag.log file
execution: just follow prompt at start of the script and enter
5

## Feature 06 - Backup and Delete/Restore (6.8)

execution: just follow prompt at start of the script and enter
6, then
Enter 1 for backup or 2 for restore
backup will find all .tmp files and put them in a restore.log
it will also delete them from original location 

restore will restore the files to their original files 


## Custom Feature 02 - Mini Football Game

Mini Interactive football game

Enter 7 from the intial script input to run this feature
The objective of the game is to gain 100 yards and score a touchdown to win the game. 
The user will choose the type of plays to be he/she wants to run (short/medium/long)
you have 9 plays to try and gain 100 yards
each type of play has a different success rate and number of yards that you can get
on each play

    Short pass : 85% completion rate and 1-13 yards per play
    medium pass : 57% completion rate and 8-22 yards per play
    long pass : 47 % completion rate and 15-40 yards per play


## Custom Feature 02 (8) - Delete duplicate files

Delete Replicate Files
 
From the script input hit 8 to run this feature.
It will show any duplicate files in your directory
it will ask you to input 1 to delete one of the duplicate files
inputting anything else will cancel it.
one of the pitfalls of this feature is that it only works in the directory you run it in


## Sources/References 

[https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself]

I used this code to get a absolute path

[https://stackoverflow.com/questions/1521462/looping-through-the-content-of-a-file-in-bash]

I used code from here to help with the restore feature

[https://superuser.com/questions/259148/bash-find-duplicate-files-mac-linux-compatible]

[https://superuser.com/questions/1363200/remove-duplicate-files-by-comparing-them-with-md5-recursively]

I used code from here in my custom feature 02 (delete duplicate files)
