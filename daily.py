import os
from datetime import datetime

FILE_NAME = "daily_log.txt"  # file where we append today's entry

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(FILE_NAME, "a") as f:
	for i in range(3):  # number of commits
        	f.write(f"Daily contribution {i+1} on {today}\n")

os.system("git add .")
os.system(f'git commit -m "Daily contribution {today}"')
os.system("git push")

print("✅ Daily GitHub contribution successful!")
