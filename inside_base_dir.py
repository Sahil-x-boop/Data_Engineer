import os 
from pathlib import Path

def get_project_base():
    return Path.cwd().parent

BASE_PATH = get_project_base()
print(BASE_PATH)
