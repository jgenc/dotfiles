import os
import shutil
import json


backup_directory = f"{os.environ['HOME']}/.cache/dotfiles-backup"


def create_backup():
    if not os.path.isdir(backup_directory):
        cache_directory = backup_directory.replace("/dotfiles-backup", "")
        if not os.path.isdir(cache_directory):
            print('Cache directory does not exist. Creating it.')
            os.mkdir(cache_directory)
        print('Backup directory does not exist. Creating it.')
        os.mkdir(backup_directory)


def copy_file(file, src):
    shutil.copy(src, f"{os.environ['HOME']}/{file}")


def copy_dir(dir, src, dst):
    if os.path.isdir(dst):
        print(
            f'Directory \'{dir}\' already exists at .config/. Making a backup...')
        user_backup_dir = os.path.join(backup_directory, dir)
        if os.path.isdir(user_backup_dir):
            print(
                f'Oh, there exists a previous backup from this script for \'{dir}\'. Overwriting..')
            shutil.rmtree(user_backup_dir)
        shutil.move(dst, backup_directory)

    shutil.copytree(src, dst)
    print(f'Copied {dir} to ~/.config successfully!')


create_backup()
for dir in os.listdir('../.config/'):
    dst = f"{os.environ['HOME']}/.config/{dir}"
    src = os.path.join(os.getcwd(), f".config/{dir}")
    src = src.replace("/scripts", "")
    copy_dir(dir, src, dst)

home_files = json.load(open("./data.json", "r"))["home_files"]
for file in home_files:
    src = os.getcwd().replace("/scripts", "") + "/" + file
    copy_file(file, src)