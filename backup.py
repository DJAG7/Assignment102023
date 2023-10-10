import shutil
#library to copy files/directories
import sys
#library to accept file path as an argument
from datetime import datetime
#datetime object to import datetime data
import os
#OS function to compare and work with path data


#Function to get help for commands used
def gethelp():
    print("Enter python backup.py <source_directory> <destination_directory>")

#Main Backup Function
def backup():
    
    #source and destination path 
    source = sys.argv[1]
    destination = sys.argv[2]

    #if source path does not exist
    if not os.path.exists(source):
        print("Error: Source Directory not found")
        return

    #if source is same as destination folder
    if source == destination:
        print("Error: Copying to the same destination")
        return
    
    #For new directory
    if not os.path.exists(destination):
        try:
            print("Backing up files from", sys.argv[1], "to new directory", sys.argv[2])
            #copytree to create a new directory and copy
            shutil.copytree(source, destination, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)
            print("Files copied successfully to", destination)
        except:
            print("Error: Copying File")
    else:
        try:
            #To backup to an existing directory
            print("Backing up files from", sys.argv[1], "to existing directory", sys.argv[2])

            #Timestamp to generate current date and time in Hour.Minute.Second_Day.Month.Year format
            timestamp = datetime.now().strftime("%H.%M.%S_%d.%m.%y")

            #iterates to rename over multiple files
            for filename in os.listdir(source):
                src_path = os.path.join(source, filename)
                filename, file_extension = os.path.splitext(filename)
                new_filename = f"{filename}_{timestamp}{file_extension}" 
                dst_path = os.path.join(destination, new_filename)
                shutil.copy2(src_path, dst_path)
            print("Files copied successfully to", destination)
        except:
            print("Error: Copying File")


#main function

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] == "-h":
        print("Error: Required Arguments not given")
        gethelp()
    else:
        try:
            backup()
        except Exception as e:
            print("Error Occured")