# dotfiles

*This repository exists to store my configuration files, notes, recommendations, etc.*

## Notes

* **Fonts:** The code font I use is [Caskaydia Cove NF](https://github.com/ryanoasis/nerd-fonts)
* **Schedule Jobs:** I was looking for a way to run some tasks on specific intervals and I stumbled upon cron, more specifically [cronnie](https://archlinux.org/packages/core/x86_64/cronie/). I have made a new folder, ~/.startup/ where I save all the .sh files I need for the tasks. Syntax is pretty simple, easily found on the Arch wiki.

## Gnome Configuration

### Extensions

1. [Caffeine](https://extensions.gnome.org/extension/517/caffeine/)
    * This is a **musthave** for any GNOME user. Nice quick settings integration in GNOME 43
2. [Just Perfection](https://extensions.gnome.org/extension/3843/just-perfection/)
3. [Unite](https://extensions.gnome.org/extension/1287/unite/)
4. [GSConnect](https://extensions.gnome.org/extension/1319/gsconnect/)

## Fish Shell

### Functions

1. `goodnight` updates systems, saves `dnf` logs to a hidden directory in the Documents folder. Some time in the future I will do something wiht that data, but for now I am just harvesting it.
2. `kitty-theme` changes the `kitty` terminal theme. Position argument is needed; `l` for the light theme and `d` for the dark theme
3. `codeh` code here. Opens VSCode in cwd and dies
4. `minecraft` Opens a Minecraft Launcher. Machine specific, not really useful

### Extensions

Through the [fisher](https://github.com/jorgebucaran/fisher) package manager you can download the following extensions.

1. [tide](https://github.com/IlanCosman/tide) The *ULTIMATE* prompt for fish! It's good.
2. [fzf](https://github.com/PatrickF1/fzf.fish), A **very** helpful extensions, provides the follwing:
    1. Search Directory (`F` for file)
        * <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd>
    2. Git Log (`L` for log)
        * <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd>
    3. Git Status (`S` for status)
        * <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>S</kbd>
    4. Search History (`R` for reverse-i-search)
        * <kbd>Ctrl</kbd> + <kbd>R</kbd>
    5. There are also some for variables and processes, I do not use them at all for now, they might be useful later on.
