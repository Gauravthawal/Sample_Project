import os
from datetime import datetime

FILE_NAME = "daily_log.txt"  # file where we append today's entry

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(FILE_NAME, "a") as f:
    f.write(f"Daily contribution on {today}\n")

os.system("git add .")
os.system(f'git commit -m "Daily contribution {today}"')
os.system("git push")

print("✅ Daily GitHub contribution successful!")
