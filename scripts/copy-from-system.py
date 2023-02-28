# A simple script to copy directories from dirs_to_copy to local git folder
import os
import shutil
import json

# "directories is the first object in the json"
dirs = json.load(open("./directories.json", "r"))["directories"]


for dir in dirs:
    src = f"{os.environ['HOME']}/.config/{dir}"
    # TODO:
    # Test if cwd is the dotfiles repository, don't just run anywhere. 
    dst = os.path.join(os.getcwd(), f".config/{dir}")
    dst = dst.replace("/scripts", "")

    print(dst)

    if not os.path.exists(src):
        continue

    shutil.copytree(src, dst,
                    ignore=shutil.ignore_patterns('.git*', 'watch_later*', '__pycache__'), dirs_exist_ok=True)
