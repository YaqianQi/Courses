#!/bin/bash
####################################
#
# Backup dir script 
#
# The script requires three parameters
# the directory to backup;
# the compression algorithm to use (none, gzip, bzip, etc; see tar for details);
# the output file name.
# 
# All output except errors will be written to the error.log file instead of stderr.
#
# ./backup.sh <BACKUP_DIR>  <COMPRESSION_ALGO>  <OUTPUT_FILE_NAME>
# 
# decrypt file
# openssl aes-256-cbc -salt -a -d -in $OUTPUT_FILE_NAME.aes128 -out $ARCHIVE_FILE
####################################

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
	echo "You have failed to pass a parameter."
	echo "USAGE: ./backup.sh BACKUP_DIR COMPRESSION_ALGO OUTPUT_FILE_NAME"
	exit 255;
fi

# Accept three parameters
BACKUP_DIR=$1
COMPRESSION_ALGO=$2
OUTPUT_FILE_NAME=$3

# Set the path to the error log file
ERROR_LOG="error.log"

# Output compression output name with file file type 
ARCHIVE_FILE=""

# Supported compression algo
TAR="tar"
BZIP="bzip"
BZIP2="bzip2"
XZ="xz"


if [ ! -d $BACKUP_DIR ]; then
	(echo "directory not exist") >& $LOGFILE
	echo "exit"
	exit 1
fi


# Create the backup archive with the specified compression algorithm
if [[ "$COMPRESSION_ALGO" == "$TAR"  ]]; then
  ARCHIVE_FILE="$OUTPUT_FILE_NAME.tar.gz"
  tar  -czvf ARCHIVE_FILE $BACKUP_DIR 2>> $ERROR_LOG; 

elif [[ "$COMPRESSION_ALGO" == "$BZIP" ]] || [[ "$COMPRESSION_ALGO" == "$BZIP2" ]]; then
  ARCHIVE_FILE="$OUTPUT_FILE_NAME.tar.bz2"
  tar  -czvf ARCHIVE_FILE $BACKUP_DIR 2>> $ERROR_LOG; 

elif [[ "$COMPRESSION_ALGO" == "$XZ"  ]]; then
  ARCHIVE_FILE="$OUTPUT_FILE_NAME.tar.xz"
  tar -cJvf ARCHIVE_FILE $BACKUP_DIR 2>> $ERROR_LOG; 

else 
  echo "Invalid compression option." 2>> $ERROR_LOG;
fi 


# Encryption
openssl aes-256-cbc -salt -a -e -in $ARCHIVE_FILE -out $OUTPUT_FILE_NAME.aes128 2>> $ERROR_LOG;

# Check if the backup archive was created successfully
if [ $? -eq 0 ]; then
  echo "Backup archive:$ARCHIVE_FILE created successfully"; 
else
  echo "Error creating backup archive. Please check $ERROR_LOG for more information." 2>> $ERROR_LOG;
fi
