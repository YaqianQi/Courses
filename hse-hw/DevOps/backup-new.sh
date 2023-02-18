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
# ./backup.sh <backup_dir>  <compression_algorithm>  <output_file_name>
# decrypt file
# openssl aes-256-cbc -salt -a -d -in $output_file_name.aes128 -out $full_output_name
####################################

# Accept three parameters
backup_dir=$1
compression_algorithm=$2
output_file_name=$3
# Set the path to the error log file
error_log="error.log"
full_output_name=""

# Create the backup archive with the specified compression algorithm
TAR="tar"
BZIP="bzip"
BZIP2="bzip2"
XZ="xz"


if [[ "$compression_algorithm" == "$TAR"  ]]; then
  full_output_name="$output_file_name.tar.gz"
  tar  -czvf full_output_name $backup_dir 2>> $error_log; 
  echo "tar"
elif [[ "$compression_algorithm" == "$BZIP" ]] || [[ "$compression_algorithm" == "$BZIP2" ]]; then
  full_output_name="$output_file_name.tar.bz2"
  tar  -czvf full_output_name $backup_dir 2>> $error_log; 
  echo "biz"
elif [[ "$compression_algorithm" == "$XZ"  ]]; then
  full_output_name="$output_file_name.tar.xz"
  tar -cJvf full_output_name $backup_dir 2>> $error_log; 
  echo "xz"
else 
echo "Invalid compression option." 2>> $error_log;
fi 



openssl aes-256-cbc -salt -a -e -in $full_output_name -out $output_file_name.aes128 2>> $error_log;
# openssl aes-256-cbc -salt -a -d -in $output_file_name.aes128 -out $full_output_name 2>> $error_log;

# Check if the backup archive was created successfully
if [ $? -eq 0 ]; then
  echo "Backup archive:$full_output_name created successfully"; 
else
  echo "Error creating backup archive. Please check $error_log for more information."
fi
