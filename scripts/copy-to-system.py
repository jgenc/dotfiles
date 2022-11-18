import os
import shutil

# Creating backup directory
#   Get backup_directory name
backup_directory = f"{os.environ['HOME']}/.config/.dotfiles-backup"

if not os.path.isdir(backup_directory):
    print('Backup directory does not exist. Creating it.')
    os.mkdir(backup_directory)
    
for dir in os.listdir('.config/'):
    # Find the absolute path of repository directory and .config directory
    user_dir = f"{os.environ['HOME']}/.config/{dir}"
    cur_dir = os.path.join(os.getcwd(), f".config/{dir}")

    # If .config dir exists, make a backup of it 
    if os.path.isdir(user_dir):
        print(f'Directory \'{dir}\' already exists at .config. Making a backup...')
        # If there is a backup of it already, replace it
        user_backup_dir = os.path.join(backup_directory, dir)
        if os.path.isdir(user_backup_dir):
            print(f'Oh, there exists a previous backup from this script for \'{dir}\'. Overwriting..')
            shutil.rmtree(user_backup_dir)
        # Move original directory to backup
        shutil.move(user_dir, backup_directory)
    # Copy repo dir to .config dir
    print(f'Copied {dir} to ~/.config successfully!')
    shutil.copytree(cur_dir, user_dir)
