import subprocess
import random
# import json
# import os

#config
# CONFIG_FILE = "config.json"


#file dump data
x=random.randint(1, 100)

try:
    with open("file.txt", "a") as f:
        f.write(str(x))
except FileNotFoundError:
    print("File not found")



def auto_commit():
    try:
        # Add all changes to staging
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit with a message
        commit_message = "changes"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        subprocess.run(['git', 'push'], check=True)
        
        print("Changes have been committed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

auto_commit()