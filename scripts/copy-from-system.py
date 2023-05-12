# A simple script to copy directories from dirs_to_copy to local git folder
import os
import shutil
import json

dirs = json.load(open("./data.json", "r"))["directories"]
home_files = json.load(open("./data.json", "r"))["home_files"]


def copy_dir(dir):
    src = f"{os.environ['HOME']}/.config/{dir}"
    dst = os.path.join(os.getcwd().replace(
        "/scripts", ""), f".config/{dir}")

    if not os.path.exists(src):
        return

    shutil.copytree(src, dst,
                    ignore=shutil.ignore_patterns(
                        '.git*', 'watch_later*', '__pycache__'),
                    dirs_exist_ok=True)


def copy_file(name):
    src = f"{os.environ['HOME']}/{name}"
    dst = os.getcwd().replace("/scripts", "")
    shutil.copy(src, dst)


def main():
    print("I am going to copy configuration files from the following directori\
          es:")
    for dir in dirs:
        print("Copying", dir)
        copy_dir(dir)
    for file in home_files:
        print("Copying", file)
        copy_file(file)


main()
