# dotfiles

This repository exists to store my configuration files, notes, recommendations, etc. I'll probably make it public in the future, when I feel confident in my configurations.

# Notes
* **Nautilus Default Terminal** To properly change default terminal in nautilus install https://github.com/Stunkymonkey/nautilus-open-any-terminal and then change the default value with dconf-edit. Pretty easy and straightforward, but most importantly, it works flawlessly.
* **Fonts:** A really good UI font is Source Code Pro and also, a really good font for terminal/coding is FantasqueSansMono Nerd Font. I also like JetBrains Mono, both as a UI font and a coding font.
* **Lutris:** ((This is kindof useless now, since I can easily select a custom executable with the advanced option. lmao)) --> To properly install and use a custom Proton version, I need to extract only the files contained in the dist folder of the tarball to ~/.local/lutris/runners/wine/<\name of proton version>.
* **Schedule Jobs: (Not using this anymore)** I was looking for a way to run some tasks on specific intervals and I stumbled upon cron, more specifically [cronnie](https://archlinux.org/packages/core/x86_64/cronie/). I have made a new folder, ~/.startup/ where I save all the .sh files I need for the tasks. Syntax is pretty simple, easily found on the Arch wiki. 
* **RazerGenie:** This is a musthave app for everyone who owns Razer mice/keyboards. Without this, they're pretty much stuck on default settings. 

# Recommended Apps
* PDF Viewer with tabs: **qpdfviewer**
* Music app: **Tauon Music**
* Application Launcher: **Rofi**
* Photo app with good exif tab: **pix** (check optional dependacies on the AUR)
* Wallpaper Changer: **nitrogen** typically used for WMs, but I like it for randomly changing wallpapers.

# Gnome Configuration
* **Shell:** [Flat-remix-blue](https://www.gnome-look.org/p/1013030/)
* **GTK Theme:** [Cloudy-Dark-Grey](https://www.gnome-look.org/p/1242416/)
* **Icons:** For now Papirus, until I find better ones.
* **Extensions:**
    1. [Activities configurator](https://extensions.gnome.org/extension/358/activities-configurator/) This is to be able and modify the ugly default panel to sweet perfection.
    2. [Animation Tweaks](https://extensions.gnome.org/extension/1680/animation-tweaks/) I haven't really changed much, but I might in the future, who knows?
    3. [Dash To Dock](https://extensions.gnome.org/extension/307/dash-to-dock/) Default dock like Ubuntu's, but configured to be at the bottom, it's really beautiful.
    4. [Dynamic Panel transparency](https://extensions.gnome.org/extension/1011/dynamic-panel-transparency/) To make the activities panel transparent when something is close to it. Really clean.
    5. [Gtile](https://extensions.gnome.org/extension/28/gtile/) Title speaks for itself. One thing I would like is if it had automatic tiling, unless it has and I am dumb af.
    6. [Audio Switcher](https://extensions.gnome.org/extension/1092/audio-switcher/) Why isn't this included in GNOME?
    7. [Application Volume Mixer](https://extensions.gnome.org/extension/3499/application-volume-mixer/) Why isn't this also included in GNOME?
    8. [Tray Icons: Reloaded](https://extensions.gnome.org/extension/2890/tray-icons-reloaded/) Part 3 of: Why isn't this included in GNOME?
    9. [Pop-OS Tiling](https://aur.archlinux.org/packages/gnome-shell-extension-pop-shell-git/) Literally Pop-OS tiling, nothing fancy. Might switch to a WM 

# Fish shell
* **Fisher:** It's a package manager for the fish shell.
    1. [hydro](https://github.com/jorgebucaran/hydro) This is a simple fish prompt, seems cool.

# WM
**Regolith**
I really like i3, but the combination of i3+Gnome is superb. Also, I use the ayu-dark theme, pretty cool!
