# A simple script to copy directories from dirs_to_copy to local git folder
import json
import os
import shutil

data = json.load(open("./data.json", "r"))
config_dirs = data["config_directories"]
config_files = data.get("config_files", [])
home_files = data["home_files"]
special_dirs = data.get("special_directories", {})


def copy_dir(dir):
    src = f"{os.environ['HOME']}/.config/{dir}"
    dst = os.path.join(os.getcwd().replace("/scripts", ""), f".config/{dir}")

    if not os.path.exists(src):
        return

    shutil.copytree(
        src,
        dst,
        ignore=shutil.ignore_patterns(".git*", "watch_later*", "__pycache__"),
        dirs_exist_ok=True,
    )


def copy_file(name):
    src = f"{os.environ['HOME']}/{name}"
    dst = os.getcwd().replace("/scripts", "")
    shutil.copy(src, dst)


def copy_config_file(name):
    src = f"{os.environ['HOME']}/.config/{name}"
    dst = os.path.join(os.getcwd().replace("/scripts", ""), f".config/{name}")

    if not os.path.exists(src):
        return

    # Create parent directory if needed
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)


def copy_special_directories():
    for name, config in special_dirs.items():
        src = f"{os.environ['HOME']}/{config['system_path']}"
        dst = os.path.join(os.getcwd().replace("/scripts", ""), config["repo_path"])

        if not os.path.exists(src):
            print(f"Warning: {name} directory not found at {src}")
            continue

        print(f"Copying {name} from {src}")

        # For zsh_custom, ignore plugins and themes folders (3rd party repos)
        ignore_patterns = [".git*", "__pycache__"]
        if name == "zsh_custom":
            ignore_patterns.extend(["plugins", "themes"])

        shutil.copytree(
            src,
            dst,
            ignore=shutil.ignore_patterns(*ignore_patterns),
            dirs_exist_ok=True,
        )


def main():
    print("I am going to copy configuration files from the following directories:")
    for dir in config_dirs:
        print(f"Copying ~/.config/{dir}")
        copy_dir(dir)
    for file in config_files:
        print(f"Copying ~/.config/{file}")
        copy_config_file(file)
    for file in home_files:
        print(f"Copying ~/{file}")
        copy_file(file)

    # Copy special directories
    copy_special_directories()


main()
