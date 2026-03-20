import subprocess
import random
import time
# import json
# import os
import sys

#config
# CONFIG_FILE = "config.json"


#file dump data
def write_file():
    x=random.randint(1, 100)

    try:
        with open("file.txt", "a") as f:
            print("writing to file")
            f.write(str(x))
    except FileNotFoundError:
        print("File not found")



def auto_commit():
    try:
        write_file()
        subprocess.run(['git', 'add', '.'], check=True)
        print("Running git add .")
        
        commit_message = "changes"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print("Running git commit -m 'changes'")

        subprocess.run(['git', 'push'], check=True)
        print("Running git push")
        
        print("Changes have been committed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


#main

print("welcome to auto commit script")
print("this script will automatically commit changes to your git repository every 10 seconds")
print("press 1 to start the script \n press 2 to exit")
y = int(input("enter your choice: "))
if y == 1:
    print("starting the script")
    print("commiting changes every 10 seconds till 5 commits are made")
    print("1st commit")
    auto_commit()
    time.sleep(10)
    print("2nd commit")
    auto_commit()
    time.sleep(10)
    print("3rd commit")
    auto_commit()
    time.sleep(10)
    print("4th commit")
    auto_commit()
    time.sleep(10)
    print("5th commit")
    auto_commit()
    print("script has finished commiting changes")
elif y == 2:
    print("exiting the script")
    sys.exit()
else:
    print("invalid choice")