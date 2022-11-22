import os
import shutil

# Creating backup directory
#   Get backup_directory name
backup_directory = f"{os.environ['HOME']}/.cache/dotfiles-backup"

if not os.path.isdir(backup_directory):
    print('Backup directory does not exist. Creating it.')
    os.mkdir(backup_directory)
    
# This is a simpler way to know how many directories the script is going to copy, just look at how many the repository has!
# I thought of how to implement this to the "copy-from", but it does not make that much sense. It kind of only works here

for dir in os.listdir('.config/'):
    # Find the absolute path of repository directory and .config directory
    dst = f"{os.environ['HOME']}/.config/{dir}"
    src = os.path.join(os.getcwd(), f".config/{dir}")

    # If .config dir exists, make a backup of it 
    if os.path.isdir(dst):
        print(f'Directory \'{dir}\' already exists at .config/. Making a backup...')
        # If there is a backup of it already, replace it
        user_backup_dir = os.path.join(backup_directory, dir)
        if os.path.isdir(user_backup_dir):
            print(f'Oh, there exists a previous backup from this script for \'{dir}\'. Overwriting..')
            shutil.rmtree(user_backup_dir)
        # Move original directory to backup
        shutil.move(dst, backup_directory)
    # Copy repo dir to .config dir
    print(f'Copied {dir} to ~/.config successfully!')
    shutil.copytree(src, dst)
