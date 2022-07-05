# A simple script to copy directories from dirs_to_copy to local git folder
import os
import shutil

repo_dir = './.config/'
dirs_to_copy = [
        'kitty',
        'mpv',
        'ranger',
        'fish',
        'nvim'
        ]

for dir in dirs_to_copy:
    user_dir = f"{os.environ['HOME']}/.config/{dir}"
    cur_dir = os.path.join(os.getcwd(), f".config/{dir}")
    
    shutil.copytree(user_dir, cur_dir, shutil.ignore_patterns('objects*'), dirs_exist_ok=True)
