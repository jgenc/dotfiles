import os
import shutil

src = f"{os.environ['HOME']}"
shutil.copy(src + "/.vimrc", os.getcwd())