import os
import datetime

file_path = "my_file.txt" 

with open(file_path, "w") as f:
    f.write("Initial content")

mtime_timestamp = os.path.getmtime(file_path)
mtime_datetime = datetime.datetime.fromtimestamp(mtime_timestamp)

print(f"Modification time of '{file_path}': {mtime_datetime}")