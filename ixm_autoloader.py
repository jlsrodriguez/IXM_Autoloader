
#The purpose of this script is to check for a completed run every 30 seconds, then report that a folder is ready for upload using Rsync

import time
import os

#source = "H:\IXM-data-SSD1"
#Temp directory
source = os.getcwd()

print(source)
#Move to that directory
os.chdir(source)
#Every 30 seconds
while True:
      #Get list of current MMAP directories
      files = os.listdir(source)
      #For each file in that directory
      for MMAP in range(len(files)):
          #If MMAP substring in one of the folder names
          if "MMAP" in str(files[MMAP]):
              #Change directory to that one
              os.chdir(source + "/" + str(files[MMAP]))
              #Create list of files within single MMAP directory
              sub_files = os.listdir(str(os.getcwd()))
              
              sub_files_quad4 = filter(lambda a: 'P24' in a, sub_files)

              sub_files_quad3 = filter(lambda a: 'P23' in a, sub_files)

              sub_files_quad2 = filter(lambda a: 'O24' in a, sub_files)

              sub_files_quad1 = filter(lambda a: 'O23' in a, sub_files)
              
              while True:

              
                    if len(str(sub_files_quad4)) >= 4:

                        print("sick")
                        break
                    elif len(str(sub_files_quad3)) >= 4:

                        print("sick3")
                        break
                    elif len(str(sub_files_quad2)) >= 4:

                        print("sick2")
                        break
                    elif len(str(sub_files_quad1)) >= 4:

                        print("sick1")
                        break
                    else:

                        time.sleep(60)
              print("Loop completed")

      time.sleep(60)

source = "H:\IXM-data-SSD1\MMAP00003"

destination = "Destination on big drive"

os.chdir(source)






