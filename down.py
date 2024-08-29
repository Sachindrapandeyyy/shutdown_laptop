import os
import time

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

shutdown_time_seconds = 2* 60

print("apka laptop band hone mei itna samy shesh hai .")

for remaining_seconds in range(shutdown_time_seconds, 0, -1):
    print(f"Time remaining: {format_time(remaining_seconds)}", end="\r")
    time.sleep(1)

os.system("shutdown /s /t 1")
