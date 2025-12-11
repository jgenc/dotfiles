import json
import os
import shutil

data = json.load(open("./data.json", "r"))
config_files = data.get("config_files", [])
home_files = data["home_files"]
special_dirs = data.get("special_directories", {})
backup_directory = f"{os.environ['HOME']}/.cache/dotfiles-backup"


def create_backup():
    if not os.path.isdir(backup_directory):
        cache_directory = backup_directory.replace("/dotfiles-backup", "")
        if not os.path.isdir(cache_directory):
            print("Cache directory does not exist. Creating it.")
            os.mkdir(cache_directory)
        print("Backup directory does not exist. Creating it.")
        os.mkdir(backup_directory)


def copy_file(file, src):
    shutil.copy(src, f"{os.environ['HOME']}/{file}")


def copy_config_file(file, src):
    dst = f"{os.environ['HOME']}/.config/{file}"
    # Create parent directory if needed
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)
    print(f"Copied {file} to ~/.config successfully!")


def copy_config_file(file, src):
    dst = f"{os.environ['HOME']}/.config/{file}"
    # Create parent directory if needed
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)
    print(f"Copied {file} to ~/.config successfully!")


def copy_dir(dir, src, dst):
    if os.path.isdir(dst):
        print(f"Directory '{dir}' already exists at .config/. Making a backup...")
        user_backup_dir = os.path.join(backup_directory, dir)
        if os.path.isdir(user_backup_dir):
            print(
                f"Oh, there exists a previous backup from this script for '{dir}'. Overwriting.."
            )
            shutil.rmtree(user_backup_dir)
        shutil.move(dst, backup_directory)

    shutil.copytree(src, dst)
    print(f"Copied {dir} to ~/.config successfully!")


def copy_special_directories_to_system():
    for name, config in special_dirs.items():
        src = os.path.join(os.getcwd().replace("/scripts", ""), config["repo_path"])
        dst = f"{os.environ['HOME']}/{config['system_path']}"

        if not os.path.exists(src):
            print(f"Warning: {name} directory not found in repo at {src}")
            continue

        if os.path.isdir(dst):
            print(f"{name} already exists. Making a backup...")
            user_backup_dir = os.path.join(backup_directory, name)
            if os.path.isdir(user_backup_dir):
                print(f"Overwriting previous {name} backup...")
                shutil.rmtree(user_backup_dir)
            shutil.move(dst, user_backup_dir)

        shutil.copytree(src, dst)
        print(f"Copied {name} to {dst} successfully!")


create_backup()
for dir in os.listdir("../.config/"):
    dst = f"{os.environ['HOME']}/.config/{dir}"
    src = os.path.join(os.getcwd(), f".config/{dir}")
    src = src.replace("/scripts", "")
    copy_dir(dir, src, dst)

for file in config_files:
    src = os.path.join(os.getcwd().replace("/scripts", ""), ".config", file)
    copy_config_file(file, src)

for file in home_files:
    src = os.getcwd().replace("/scripts", "") + "/" + file
    copy_file(file, src)

# Copy special directories to system
copy_special_directories_to_system()
