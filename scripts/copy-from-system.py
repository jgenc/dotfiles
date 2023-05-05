# A simple script to copy directories from dirs_to_copy to local git folder
import os
import shutil
import json

dirs = json.load(open("./directories.json", "r"))["directories"]


def copy(dir):
    src = f"{os.environ['HOME']}/.config/{dir}"
    # TODO: Test if cwd is the dotfiles repository, don't just run anywhere.
    dst = os.path.join(os.getcwd().replace(
        "/scripts", ""), f".config/{dir}")

    if not os.path.exists(src):
        return

    shutil.copytree(src, dst,
                    ignore=shutil.ignore_patterns(
                        '.git*', 'watch_later*', '__pycache__'),
                    dirs_exist_ok=True)


def main():
    print("I am going to copy configuration files from the following directori\
          es:")
    for dir in dirs:
        print("Copying", dir)
        copy(dir)


main()
