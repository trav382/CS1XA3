# CS 1XA3 PROJECT01 - mooret12


### Usage

	Execute this script from project root with:
        chmod +x ./CS1XA3/Project01/project_analyze
        You will be prompted to enter either 1 , 2 or 3.
        entering 1 and hitting enter will execute feature 1
        entering 2 and hitting enter will execute feature 1
        entering 3 and hitting enter will execute feature 1
        the program will terminate after executing a feature,
        run it again to use other features


### Feature 01 - 6.4 File Size List 

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


## Custom Feature 01 -

Delete Replicate Files


    The plan with this custom feature is to make a script that will find files
    with the same name in different directories and delete one of them. Also if the 
    contents of a file are the exact same a duplicate will be deleted, regardless if the
    name of the files are the same or not.


## Custom Feature 02

Mini Interactive football game

    The objective of the game is to gain 100 yards and score a touchdown to win the game in overtime. 
    The user will choose the type of plays to be he/she wants to run (short/medium/long pass, run)
    and the outcome of each play will be calculated based on the play chosen by the user
