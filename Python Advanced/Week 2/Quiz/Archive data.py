"""
The system administrator remembered that he had not archived user files for a long time and decided to do it right now. 
However, the size of the disk where he can place the archive, may be less than the total amount of archived files. 
Therefore, the system administrator wants to archive the data of as many users as possible.

It is known how much disk space each user's files occupy. 
Write a program that will find the maximum number of users whose data can be archived

Input data:
100 2
200
50

Program output:
1

"""
total_disk = 0
user_num = 0 
count = 0
disk_details = []
input_str = input()
if len(input_str.split()) == 2:
    total_disk = int(input_str.split()[0])
    user_num =  int(input_str.split()[1])
for i in range(user_num):
    disk_details.append(int(input()))

disk_details.sort()
for x in disk_details:
    if total_disk - x > 0:
        count += 1
        total_disk -= x
    else:
        break
print(count) 