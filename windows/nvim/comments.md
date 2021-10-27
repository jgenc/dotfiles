### This is a file with some notes on the Windows config folder for neovim
- First of all, to install neovim on Windows one should use the chocolatey package manager and use the command `choco install neovim` (you can also use the -y flag to accept terms of installation)
- The package is bundled with neovim-qt, really useful for Windows, as the usage of the OS is not geared towards terminal usage. **Very useful** if used for some quick editing.
- The folder for the configuration is located at `~\AppData\Local\nvim` and works exactly like on Linux. Be careful when typing down directory paths, Windows uses back slashes (\) and not forward slashes (/), like on Linux.
- Finally, for everything to work correctly I used the command `PlugInstall`.
- As of writing this, I copied the Linux configuration and just fixed the sources on `init.vim` and everything **I tested** worked very nicely. However, I need to say that, I'm not sure what changes happen in the folders when I run the PlugInstall command, so there might be a chance that the configuration directory changes. I say this because the files might be different from what they are on the repo.

***    

#### 
- Coc will probably *not* work on most machines, as node is not a program tha all programmers install on their machines. As of writing this, I have not fixed it because I do not need it on Windows. It shouldn't be hard to fix.
