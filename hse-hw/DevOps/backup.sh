#!/bin/bash

BACKUPDIR=$1 #the directory to backup;
# test 
ALGONAME=$2 #the compression algorithm to use (none, gzip, bzip, etc; see tar for details);
# cvfz
OUTPUTFILENAME=$3 #the output file name.
# filename.tgz

# Print start status message.
echo "Backing up $BACKUPDIR to $OUTPUTFILENAME"
date
echo

# tar command compression_name BACKUPDIR

# bash backup.sh test cvfz my_test.tar.gz
tar $ALGONAME $OUTPUTFILENAME $BACKUPDIR


ERROR1=$($ALGONAME $OUTPUTFILENAME $BACKUPDIR 2> error.log)
echo $ERROR1

openssl enc -aes-256-cbc -in $OUTPUTFILENAME -out $OUTPUTFILENAME.enc

ERROR2 = $(openssl enc -aes-256-cbc -in $OUTPUTFILENAME -out $OUTPUTFILENAME.enc 2>> error.log)
echo $ERROR2
