if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Environment vars
set -gx EDITOR /usr/bin/vim
#set -gx FLYCTL_INSTALL "/home/jorgen/.fly" 
#set -gx DENO_INSTALL "/home/jorgen/.deno"

# ==================================
#           Aliases
# ==================================

#alias v="nvim"
#alias sv="sudo nvim"
alias r="ranger"

#alias ru="ranger ~/Workspace/university/"

# This is used to spawn a thin wrapper for SSH, as it barely works on its own 
# alias s="kitty +kitten ssh"

# Git
alias gst="git status"
alias gp="git push"
alias ga="git add"

# ls replacer
# exa is not maintained anymore!
alias ls="eza --icons --header"

# Python
#alias p="python"

# Docker
alias dcd="docker compose down"
alias dcu="docker compose up"
alias dcb="docker compose build"

# wakeonlan PCs
alias wakeniveus="wakeonlan 74:56:3C:6E:0F:62"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# if test -f /Users/jorgen/miniconda3/bin/conda
#     eval /Users/jorgen/miniconda3/bin/conda "shell.fish" "hook" $argv | source
# else
#     if test -f "/Users/jorgen/miniconda3/etc/fish/conf.d/conda.fish"
#         . "/Users/jorgen/miniconda3/etc/fish/conf.d/conda.fish"
#     else
#         set -x PATH "/Users/jorgen/miniconda3/bin" $PATH
#     end
# end
status is-interactive &&
    eval /Users/jorgen/miniconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

ulimit -Sn 4096

# Starship font
starship init fish | source
